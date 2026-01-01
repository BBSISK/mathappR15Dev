"""
ADAPTIVE QUESTION GENERATOR
============================
Generates progressively difficult questions for the adaptive learning system.
Uses Claude API to create questions with proper difficulty scaling and skill tagging.

Usage:
    from question_generator_adaptive import register_adaptive_generator_routes
    register_adaptive_generator_routes(app, db)

Admin endpoints:
    POST /api/admin/generate-questions-adaptive
    GET /api/admin/adaptive-question-counts/<topic>
    GET /api/admin/adaptive-progressions/<topic>
"""

import os
import json
from flask import jsonify, request
from sqlalchemy import text
from functools import wraps
from datetime import datetime

# Try to import anthropic
try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    anthropic = None


def register_adaptive_generator_routes(app, db):
    """Register adaptive question generator routes"""
    
    def get_api_key():
        return os.environ.get('ANTHROPIC_API_KEY', '')
    
    def admin_required_api(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            from flask import session
            if 'user_id' not in session:
                return jsonify({'error': 'Not logged in'}), 401
            from app import User
            user = User.query.get(session['user_id'])
            if not user or user.role != 'admin':
                return jsonify({'error': 'Admin access required'}), 403
            return f(*args, **kwargs)
        return decorated_function
    
    # =========================================================================
    # TOPIC PROGRESSION DEFINITIONS
    # =========================================================================
    
    TOPIC_PROGRESSIONS = {
        'solving_equations': {
            'name': 'Solving Equations',
            'strand': 'Algebra',
            'levels': {
                1: {
                    'name': 'Foundation',
                    'description': 'Single-step equations with positive integers, small numbers (1-10)',
                    'example': 'x + 3 = 7',
                    'constraints': {
                        'num_range': (1, 10),
                        'operations': ['addition'],
                        'has_negatives': False,
                        'has_fractions': False,
                        'has_brackets': False,
                        'steps': 1
                    }
                },
                2: {
                    'name': 'Subtraction Equations',
                    'description': 'Single-step with subtraction, positive numbers (1-15)',
                    'example': 'x - 5 = 8',
                    'constraints': {
                        'num_range': (1, 15),
                        'operations': ['addition', 'subtraction'],
                        'has_negatives': False,
                        'has_fractions': False,
                        'has_brackets': False,
                        'steps': 1
                    }
                },
                3: {
                    'name': 'Multiplication Equations',
                    'description': 'Equations with multiplication, e.g., 3x = 12',
                    'example': '4x = 20',
                    'constraints': {
                        'num_range': (1, 20),
                        'operations': ['multiplication'],
                        'has_negatives': False,
                        'has_fractions': False,
                        'has_brackets': False,
                        'steps': 1
                    }
                },
                4: {
                    'name': 'Two-Step Equations',
                    'description': 'Combine addition/subtraction with multiplication',
                    'example': '2x + 5 = 13',
                    'constraints': {
                        'num_range': (1, 25),
                        'operations': ['addition', 'subtraction', 'multiplication'],
                        'has_negatives': False,
                        'has_fractions': False,
                        'has_brackets': False,
                        'steps': 2
                    }
                },
                5: {
                    'name': 'Negative Numbers',
                    'description': 'Equations with negative coefficients or solutions',
                    'example': '-3x + 4 = -8',
                    'constraints': {
                        'num_range': (-20, 25),
                        'operations': ['addition', 'subtraction', 'multiplication'],
                        'has_negatives': True,
                        'has_fractions': False,
                        'has_brackets': False,
                        'steps': 2
                    }
                },
                6: {
                    'name': 'Simple Brackets',
                    'description': 'Expand single brackets before solving',
                    'example': '2(x + 3) = 14',
                    'constraints': {
                        'num_range': (-25, 30),
                        'operations': ['addition', 'subtraction', 'multiplication'],
                        'has_negatives': True,
                        'has_fractions': False,
                        'has_brackets': True,
                        'bracket_complexity': 'single',
                        'steps': 3
                    }
                },
                7: {
                    'name': 'Variables Both Sides',
                    'description': 'x terms on both sides of equation',
                    'example': '3x + 5 = x + 13',
                    'constraints': {
                        'num_range': (-30, 35),
                        'operations': ['addition', 'subtraction', 'multiplication'],
                        'has_negatives': True,
                        'has_fractions': False,
                        'has_brackets': True,
                        'variables_both_sides': True,
                        'steps': 3
                    }
                },
                8: {
                    'name': 'Complex Brackets',
                    'description': 'Multiple brackets, negative multipliers',
                    'example': '3(x - 2) - 2(x + 1) = 5',
                    'constraints': {
                        'num_range': (-40, 40),
                        'operations': ['addition', 'subtraction', 'multiplication'],
                        'has_negatives': True,
                        'has_fractions': False,
                        'has_brackets': True,
                        'bracket_complexity': 'multiple',
                        'steps': 4
                    }
                },
                9: {
                    'name': 'Fractional Coefficients',
                    'description': 'Equations with fractions (halves, thirds, quarters)',
                    'example': '½x + 3 = 7',
                    'constraints': {
                        'num_range': (-50, 50),
                        'operations': ['addition', 'subtraction', 'multiplication', 'division'],
                        'has_negatives': True,
                        'has_fractions': True,
                        'fraction_complexity': 'simple',
                        'has_brackets': True,
                        'steps': 4
                    }
                },
                10: {
                    'name': 'Challenge Level',
                    'description': 'Multi-step with all complexity factors combined',
                    'example': '-2(x + 3) + ½x = 3(1 - x) + 5',
                    'constraints': {
                        'num_range': (-100, 100),
                        'operations': ['addition', 'subtraction', 'multiplication', 'division'],
                        'has_negatives': True,
                        'has_fractions': True,
                        'has_brackets': True,
                        'bracket_complexity': 'multiple',
                        'variables_both_sides': True,
                        'steps': 5
                    }
                }
            }
        },
        
        'fractions': {
            'name': 'Fractions',
            'strand': 'Number',
            'levels': {
                1: {
                    'name': 'Understanding Fractions',
                    'description': 'Identify, read and compare unit fractions',
                    'example': 'Which is larger: ½ or ⅓?',
                    'constraints': {'type': 'comparison', 'denominators': [2, 3, 4, 5]}
                },
                2: {
                    'name': 'Equivalent Fractions',
                    'description': 'Find equivalent fractions by multiplying/dividing',
                    'example': 'Find a fraction equivalent to 2/4',
                    'constraints': {'type': 'equivalence', 'denominators': [2, 3, 4, 5, 6, 8, 10]}
                },
                3: {
                    'name': 'Adding Like Denominators',
                    'description': 'Add fractions with the same denominator',
                    'example': '1/5 + 2/5 = ?',
                    'constraints': {'type': 'addition', 'same_denominator': True}
                },
                4: {
                    'name': 'Subtracting Like Denominators',
                    'description': 'Subtract fractions with the same denominator',
                    'example': '5/8 - 2/8 = ?',
                    'constraints': {'type': 'subtraction', 'same_denominator': True}
                },
                5: {
                    'name': 'Simple Unlike Denominators',
                    'description': 'Add/subtract where one denominator is multiple of other',
                    'example': '1/2 + 1/4 = ?',
                    'constraints': {'type': 'mixed_ops', 'lcd_simple': True}
                },
                6: {
                    'name': 'Finding LCD',
                    'description': 'Add/subtract requiring LCD calculation',
                    'example': '2/3 + 3/5 = ?',
                    'constraints': {'type': 'mixed_ops', 'lcd_required': True}
                },
                7: {
                    'name': 'Multiplying Fractions',
                    'description': 'Multiply fractions and simplify results',
                    'example': '2/3 × 3/4 = ?',
                    'constraints': {'type': 'multiplication'}
                },
                8: {
                    'name': 'Dividing Fractions',
                    'description': 'Divide fractions using reciprocal method',
                    'example': '3/4 ÷ 2/5 = ?',
                    'constraints': {'type': 'division'}
                },
                9: {
                    'name': 'Mixed Numbers',
                    'description': 'All operations with mixed numbers',
                    'example': '2½ + 1¾ = ?',
                    'constraints': {'type': 'mixed_numbers'}
                },
                10: {
                    'name': 'Complex Fraction Operations',
                    'description': 'Multi-step problems with order of operations',
                    'example': '(2/3 + 1/4) × 2½ = ?',
                    'constraints': {'type': 'complex', 'multi_step': True}
                }
            }
        },
        
        'percentages': {
            'name': 'Percentages',
            'strand': 'Number',
            'levels': {
                1: {
                    'name': 'Understanding Percentages',
                    'description': 'Recognize percentages, convert simple fractions',
                    'example': 'What is 50% as a fraction?',
                    'constraints': {'type': 'conversion', 'percentages': [10, 25, 50, 75, 100]}
                },
                2: {
                    'name': 'Percentage of Amount (Simple)',
                    'description': 'Find 10%, 25%, 50% of amounts',
                    'example': 'Find 25% of €80',
                    'constraints': {'type': 'of_amount', 'percentages': [10, 25, 50]}
                },
                3: {
                    'name': 'Percentage of Amount (Any)',
                    'description': 'Find any percentage of an amount',
                    'example': 'Find 35% of €120',
                    'constraints': {'type': 'of_amount', 'any_percentage': True}
                },
                4: {
                    'name': 'Percentage Increase',
                    'description': 'Calculate amount after percentage increase',
                    'example': 'Increase €50 by 20%',
                    'constraints': {'type': 'increase'}
                },
                5: {
                    'name': 'Percentage Decrease',
                    'description': 'Calculate amount after percentage decrease/discount',
                    'example': 'A €80 item has 15% off. What is the sale price?',
                    'constraints': {'type': 'decrease'}
                },
                6: {
                    'name': 'Finding the Percentage',
                    'description': 'Express one quantity as a percentage of another',
                    'example': 'What percentage is 15 of 60?',
                    'constraints': {'type': 'find_percentage'}
                },
                7: {
                    'name': 'Reverse Percentages',
                    'description': 'Find original amount given final and percentage',
                    'example': 'After 20% increase, price is €60. Original price?',
                    'constraints': {'type': 'reverse'}
                },
                8: {
                    'name': 'Percentage Change',
                    'description': 'Calculate percentage change between values',
                    'example': 'Price went from €40 to €52. What % increase?',
                    'constraints': {'type': 'change'}
                },
                9: {
                    'name': 'Compound Percentages',
                    'description': 'Multiple successive percentage changes',
                    'example': 'Price increases 10% then decreases 10%. Net effect?',
                    'constraints': {'type': 'compound'}
                },
                10: {
                    'name': 'Complex Applications',
                    'description': 'Multi-step real-world percentage problems',
                    'example': 'VAT, profit margins, depreciation calculations',
                    'constraints': {'type': 'complex', 'real_world': True}
                }
            }
        },
        
        'probability': {
            'name': 'Probability',
            'strand': 'Statistics and Probability',
            'levels': {
                1: {
                    'name': 'Probability Language',
                    'description': 'Understand certain, likely, unlikely, impossible',
                    'example': 'Is it certain, likely, unlikely or impossible that...',
                    'constraints': {'type': 'language'}
                },
                2: {
                    'name': 'Simple Probability',
                    'description': 'Calculate probability of single events',
                    'example': 'Probability of rolling a 4 on a fair die?',
                    'constraints': {'type': 'single_event', 'denominators': [2, 4, 6]}
                },
                3: {
                    'name': 'Probability from Experiments',
                    'description': 'Calculate probability from frequency data',
                    'example': 'In 50 coin flips, 28 were heads. Estimate P(heads)',
                    'constraints': {'type': 'experimental'}
                },
                4: {
                    'name': 'Probability Scales',
                    'description': 'Place probabilities on 0-1 scale, convert forms',
                    'example': 'Convert 3/8 to decimal and percentage',
                    'constraints': {'type': 'conversion'}
                },
                5: {
                    'name': 'Expected Frequency',
                    'description': 'Calculate expected outcomes over trials',
                    'example': 'How many 6s expected in 120 dice rolls?',
                    'constraints': {'type': 'expected'}
                },
                6: {
                    'name': 'Complementary Events',
                    'description': 'P(not A) = 1 - P(A)',
                    'example': 'If P(rain) = 0.3, what is P(no rain)?',
                    'constraints': {'type': 'complement'}
                },
                7: {
                    'name': 'Combined Events (OR)',
                    'description': 'Probability of A or B (mutually exclusive)',
                    'example': 'P(rolling 2 or 5) on a die?',
                    'constraints': {'type': 'or_events'}
                },
                8: {
                    'name': 'Independent Events (AND)',
                    'description': 'Probability of A and B (independent)',
                    'example': 'P(two heads in two coin flips)?',
                    'constraints': {'type': 'and_events'}
                },
                9: {
                    'name': 'Tree Diagrams',
                    'description': 'Use tree diagrams for sequential events',
                    'example': 'Draw tree for 2 draws from bag, find P(both red)',
                    'constraints': {'type': 'tree_diagram'}
                },
                10: {
                    'name': 'Complex Probability',
                    'description': 'Without replacement, conditional, multi-stage',
                    'example': '3 red, 2 blue balls. P(both red without replacement)?',
                    'constraints': {'type': 'complex'}
                }
            }
        },
        
        'introductory_algebra': {
            'name': 'Introductory Algebra',
            'strand': 'Algebra',
            'levels': {
                1: {
                    'name': 'Algebraic Notation',
                    'description': 'Understand what letters represent, write expressions',
                    'example': 'Write "5 more than x" as an expression',
                    'constraints': {'type': 'notation'}
                },
                2: {
                    'name': 'Substitution (Positive)',
                    'description': 'Substitute positive values into expressions',
                    'example': 'If x = 3, find 2x + 5',
                    'constraints': {'type': 'substitution', 'values': 'positive'}
                },
                3: {
                    'name': 'Substitution (Any)',
                    'description': 'Substitute any integer values',
                    'example': 'If a = -2, find 3a - 4',
                    'constraints': {'type': 'substitution', 'values': 'any'}
                },
                4: {
                    'name': 'Collecting Like Terms',
                    'description': 'Simplify by combining like terms',
                    'example': '3x + 5y + 2x - y = ?',
                    'constraints': {'type': 'simplify', 'like_terms': True}
                },
                5: {
                    'name': 'Multiplying Terms',
                    'description': 'Multiply algebraic terms',
                    'example': '3x × 4y = ?',
                    'constraints': {'type': 'multiply_terms'}
                },
                6: {
                    'name': 'Expanding Single Bracket',
                    'description': 'Expand expressions like a(b + c)',
                    'example': '3(2x + 5) = ?',
                    'constraints': {'type': 'expand', 'brackets': 'single'}
                },
                7: {
                    'name': 'Expanding Double Brackets',
                    'description': 'Expand (a + b)(c + d)',
                    'example': '(x + 3)(x + 2) = ?',
                    'constraints': {'type': 'expand', 'brackets': 'double'}
                },
                8: {
                    'name': 'Factorising (Common Factor)',
                    'description': 'Take out common factors',
                    'example': 'Factorise 6x + 9',
                    'constraints': {'type': 'factorise', 'method': 'common'}
                },
                9: {
                    'name': 'Factorising Quadratics',
                    'description': 'Factorise x² + bx + c',
                    'example': 'Factorise x² + 5x + 6',
                    'constraints': {'type': 'factorise', 'method': 'quadratic'}
                },
                10: {
                    'name': 'Complex Expressions',
                    'description': 'Multi-step simplification and manipulation',
                    'example': 'Expand and simplify (2x + 1)² - x(x + 2)',
                    'constraints': {'type': 'complex'}
                }
            }
        }
    }
    
    # =========================================================================
    # MAIN GENERATION ENDPOINT
    # =========================================================================
    
    @app.route('/api/admin/generate-questions-adaptive', methods=['POST'])
    @admin_required_api
    def generate_questions_adaptive():
        """Generate adaptive questions for a topic at specified levels"""
        
        if not ANTHROPIC_AVAILABLE:
            return jsonify({'error': 'Anthropic library not installed'}), 400
        
        api_key = get_api_key()
        if not api_key:
            return jsonify({'error': 'ANTHROPIC_API_KEY not configured'}), 400
        
        data = request.json
        topic = data.get('topic')
        levels = data.get('levels', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Default: all levels
        questions_per_level = data.get('questions_per_level', 15)
        
        if topic not in TOPIC_PROGRESSIONS:
            return jsonify({
                'error': f'Topic "{topic}" not found',
                'available_topics': list(TOPIC_PROGRESSIONS.keys())
            }), 400
        
        topic_config = TOPIC_PROGRESSIONS[topic]
        
        try:
            client = anthropic.Anthropic(api_key=api_key)
            all_questions = []
            errors = []
            
            for level in levels:
                if level not in topic_config['levels']:
                    errors.append(f"Level {level} not defined for {topic}")
                    continue
                
                level_config = topic_config['levels'][level]
                print(f"Generating Level {level}: {level_config['name']}...")
                
                # Determine difficulty band
                if level <= 3:
                    band = 'beginner'
                elif level <= 7:
                    band = 'intermediate'
                else:
                    band = 'advanced'
                
                prompt = f"""Generate exactly {questions_per_level} multiple choice mathematics questions for Irish Junior Cycle students (14 year olds).

TOPIC: {topic_config['name']}
LEVEL: {level} of 10
LEVEL NAME: {level_config['name']}
LEVEL DESCRIPTION: {level_config['description']}
EXAMPLE QUESTION AT THIS LEVEL: {level_config['example']}

CONSTRAINTS FOR THIS LEVEL:
{json.dumps(level_config.get('constraints', {}), indent=2)}

CRITICAL REQUIREMENTS:
1. ALL questions must match the difficulty level described above - not easier, not harder
2. Each question must have exactly 4 options (A, B, C, D)
3. Only ONE option should be correct
4. Include a clear explanation for the correct answer
5. Use Irish/European conventions (€ for currency, metres for distance)
6. Make wrong options plausible but clearly wrong when understood
7. Vary the specific numbers but maintain the SAME complexity level
8. For Level {level}, students should have mastered Levels 1-{level-1}

OUTPUT FORMAT - Return ONLY a JSON array:
[
  {{
    "question_text": "The question text",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "correct": 0,
    "explanation": "Clear explanation of why the answer is correct",
    "question_type": "calculation|word_problem|conceptual",
    "skill_tags": ["tag1", "tag2"],
    "estimated_seconds": 30
  }}
]

SKILL TAGS to use (pick relevant ones):
- positive_integers, negative_numbers, fractions, decimals
- addition, subtraction, multiplication, division
- single_step, multi_step, brackets
- word_problem, pure_calculation, mental_math

IMPORTANT: Return ONLY valid JSON, no markdown, no explanation outside the array."""

                try:
                    response = client.messages.create(
                        model="claude-sonnet-4-20250514",
                        max_tokens=8000,
                        messages=[{"role": "user", "content": prompt}]
                    )
                    
                    response_text = response.content[0].text.strip()
                    
                    # Clean markdown if present
                    if response_text.startswith('```'):
                        lines = response_text.split('\n')
                        response_text = '\n'.join(lines[1:-1])
                    if response_text.startswith('```json'):
                        response_text = response_text[7:]
                    if response_text.endswith('```'):
                        response_text = response_text[:-3]
                    
                    questions = json.loads(response_text.strip())
                    
                    # Add level metadata to each question
                    for q in questions:
                        q['topic'] = topic
                        q['difficulty_level'] = level
                        q['difficulty_band'] = band
                        q['level_name'] = level_config['name']
                    
                    all_questions.extend(questions)
                    print(f"   ✓ Generated {len(questions)} questions for Level {level}")
                    
                except json.JSONDecodeError as e:
                    errors.append(f"Level {level}: JSON parse error - {str(e)}")
                    print(f"   ✗ JSON error for Level {level}")
                except Exception as e:
                    errors.append(f"Level {level}: {str(e)}")
                    print(f"   ✗ Error for Level {level}: {e}")
            
            # Save to database
            saved = 0
            skipped = 0
            
            for q in all_questions:
                # Check for duplicate
                existing = db.session.execute(text("""
                    SELECT id FROM questions_adaptive 
                    WHERE topic = :topic 
                    AND difficulty_level = :level 
                    AND question_text = :text
                """), {
                    'topic': q['topic'],
                    'level': q['difficulty_level'],
                    'text': q['question_text']
                }).fetchone()
                
                if existing:
                    skipped += 1
                    continue
                
                # Insert question
                complexity_factors = json.dumps({
                    'level_name': q.get('level_name', ''),
                    'skill_tags': q.get('skill_tags', []),
                    'question_type': q.get('question_type', 'calculation')
                })
                
                db.session.execute(text("""
                    INSERT INTO questions_adaptive 
                    (topic, question_text, option_a, option_b, option_c, option_d,
                     correct_answer, explanation, difficulty_level, difficulty_band,
                     complexity_factors, estimated_time_seconds, question_type)
                    VALUES 
                    (:topic, :text, :a, :b, :c, :d, :correct, :explanation,
                     :level, :band, :complexity, :time, :qtype)
                """), {
                    'topic': q['topic'],
                    'text': q['question_text'],
                    'a': q['options'][0],
                    'b': q['options'][1],
                    'c': q['options'][2],
                    'd': q['options'][3],
                    'correct': q['correct'],
                    'explanation': q['explanation'],
                    'level': q['difficulty_level'],
                    'band': q['difficulty_band'],
                    'complexity': complexity_factors,
                    'time': q.get('estimated_seconds', 30),
                    'qtype': q.get('question_type', 'calculation')
                })
                saved += 1
            
            db.session.commit()
            
            # Get final counts per level
            counts = {}
            for level in range(1, 11):
                result = db.session.execute(text("""
                    SELECT COUNT(*) FROM questions_adaptive 
                    WHERE topic = :topic AND difficulty_level = :level
                """), {'topic': topic, 'level': level}).fetchone()
                counts[level] = result[0] if result else 0
            
            return jsonify({
                'success': True,
                'topic': topic,
                'saved': saved,
                'skipped': skipped,
                'errors': errors,
                'counts_by_level': counts,
                'total': sum(counts.values())
            })
            
        except Exception as e:
            import traceback
            traceback.print_exc()
            return jsonify({'error': str(e)}), 500
    
    # =========================================================================
    # HELPER ENDPOINTS
    # =========================================================================
    
    @app.route('/api/admin/adaptive-topics', methods=['GET'])
    @admin_required_api
    def get_adaptive_topics():
        """Get available topics for adaptive generation"""
        topics = []
        for key, config in TOPIC_PROGRESSIONS.items():
            topics.append({
                'topic_id': key,
                'name': config['name'],
                'strand': config['strand'],
                'levels': len(config['levels'])
            })
        return jsonify({'topics': topics})
    
    @app.route('/api/admin/adaptive-progression/<topic>', methods=['GET'])
    @admin_required_api
    def get_adaptive_progression(topic):
        """Get the level progression for a topic"""
        if topic not in TOPIC_PROGRESSIONS:
            return jsonify({'error': 'Topic not found'}), 404
        
        config = TOPIC_PROGRESSIONS[topic]
        levels = []
        for level_num, level_config in config['levels'].items():
            # Get current question count
            result = db.session.execute(text("""
                SELECT COUNT(*) FROM questions_adaptive 
                WHERE topic = :topic AND difficulty_level = :level
            """), {'topic': topic, 'level': level_num}).fetchone()
            
            levels.append({
                'level': level_num,
                'name': level_config['name'],
                'description': level_config['description'],
                'example': level_config['example'],
                'question_count': result[0] if result else 0
            })
        
        return jsonify({
            'topic': topic,
            'name': config['name'],
            'strand': config['strand'],
            'levels': levels
        })
    
    @app.route('/api/admin/adaptive-question-counts/<topic>', methods=['GET'])
    @admin_required_api
    def get_adaptive_question_counts(topic):
        """Get question counts per level for a topic"""
        counts = {}
        for level in range(1, 11):
            result = db.session.execute(text("""
                SELECT COUNT(*) FROM questions_adaptive 
                WHERE topic = :topic AND difficulty_level = :level
            """), {'topic': topic, 'level': level}).fetchone()
            counts[level] = result[0] if result else 0
        
        # Also get by band
        band_counts = {}
        for band in ['beginner', 'intermediate', 'advanced']:
            result = db.session.execute(text("""
                SELECT COUNT(*) FROM questions_adaptive 
                WHERE topic = :topic AND difficulty_band = :band
            """), {'topic': topic, 'band': band}).fetchone()
            band_counts[band] = result[0] if result else 0
        
        return jsonify({
            'topic': topic,
            'by_level': counts,
            'by_band': band_counts,
            'total': sum(counts.values())
        })
    
    @app.route('/api/admin/adaptive-sample/<topic>/<int:level>', methods=['GET'])
    @admin_required_api
    def get_adaptive_sample(topic, level):
        """Get sample questions for a topic/level"""
        result = db.session.execute(text("""
            SELECT id, question_text, option_a, option_b, option_c, option_d,
                   correct_answer, explanation, question_type
            FROM questions_adaptive 
            WHERE topic = :topic AND difficulty_level = :level
            ORDER BY RANDOM()
            LIMIT 5
        """), {'topic': topic, 'level': level}).fetchall()
        
        questions = [{
            'id': r[0],
            'question_text': r[1],
            'options': [r[2], r[3], r[4], r[5]],
            'correct': r[6],
            'explanation': r[7],
            'question_type': r[8]
        } for r in result]
        
        return jsonify({
            'topic': topic,
            'level': level,
            'count': len(questions),
            'questions': questions
        })
    
    print("✓ Adaptive question generator routes registered")
    return True

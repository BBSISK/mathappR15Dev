#!/usr/bin/env python3
"""
GENERATE ADAPTIVE QUESTIONS
===========================
Standalone script to generate adaptive questions directly.
Run this on PythonAnywhere to populate your questions_adaptive table.

Usage:
    python generate_adaptive_questions_standalone.py

This will generate 15 questions per level for key topics.
"""

import os
import sys
import json
import sqlite3

# Check for API key first
API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
if not API_KEY:
    print("=" * 60)
    print("ERROR: ANTHROPIC_API_KEY not set!")
    print("=" * 60)
    print("\nTo set it, run:")
    print("  export ANTHROPIC_API_KEY='your-key-here'")
    print("\nOr add it to your PythonAnywhere environment variables.")
    sys.exit(1)

# Try to import anthropic
try:
    import anthropic
except ImportError:
    print("=" * 60)
    print("ERROR: anthropic library not installed!")
    print("=" * 60)
    print("\nTo install, run:")
    print("  pip install anthropic --user")
    sys.exit(1)

# Database path
DB_PATH = 'instance/mathquiz.db'

# Topic progressions (same as in question_generator_adaptive.py)
TOPIC_PROGRESSIONS = {
    'solving_equations': {
        'name': 'Solving Equations',
        'levels': {
            1: {'name': 'Foundation', 'description': 'Single-step equations with positive integers, small numbers (1-10)', 'example': 'x + 3 = 7'},
            2: {'name': 'Subtraction Equations', 'description': 'Single-step with subtraction, positive numbers (1-15)', 'example': 'x - 5 = 8'},
            3: {'name': 'Multiplication Equations', 'description': 'Equations with multiplication, e.g., 3x = 12', 'example': '4x = 20'},
            4: {'name': 'Two-Step Equations', 'description': 'Combine addition/subtraction with multiplication', 'example': '2x + 5 = 13'},
            5: {'name': 'Negative Numbers', 'description': 'Equations with negative coefficients or solutions', 'example': '-3x + 4 = -8'},
            6: {'name': 'Simple Brackets', 'description': 'Expand single brackets before solving', 'example': '2(x + 3) = 14'},
            7: {'name': 'Variables Both Sides', 'description': 'x terms on both sides of equation', 'example': '3x + 5 = x + 13'},
            8: {'name': 'Complex Brackets', 'description': 'Multiple brackets, negative multipliers', 'example': '3(x - 2) - 2(x + 1) = 5'},
            9: {'name': 'Fractional Coefficients', 'description': 'Equations with fractions (halves, thirds, quarters)', 'example': '½x + 3 = 7'},
            10: {'name': 'Challenge Level', 'description': 'Multi-step with all complexity factors combined', 'example': '-2(x + 3) + ½x = 3(1 - x) + 5'},
        }
    },
    'fractions': {
        'name': 'Fractions',
        'levels': {
            1: {'name': 'Understanding Fractions', 'description': 'Identify and compare unit fractions', 'example': 'Which is larger: ½ or ⅓?'},
            2: {'name': 'Equivalent Fractions', 'description': 'Find equivalent fractions by multiplying/dividing', 'example': 'Find a fraction equivalent to 2/4'},
            3: {'name': 'Adding Like Denominators', 'description': 'Add fractions with the same denominator', 'example': '1/5 + 2/5 = ?'},
            4: {'name': 'Subtracting Like Denominators', 'description': 'Subtract fractions with the same denominator', 'example': '5/8 - 2/8 = ?'},
            5: {'name': 'Simple Unlike Denominators', 'description': 'Add/subtract where one denominator is multiple of other', 'example': '1/2 + 1/4 = ?'},
            6: {'name': 'Finding LCD', 'description': 'Add/subtract requiring LCD calculation', 'example': '2/3 + 3/5 = ?'},
            7: {'name': 'Multiplying Fractions', 'description': 'Multiply fractions and simplify results', 'example': '2/3 × 3/4 = ?'},
            8: {'name': 'Dividing Fractions', 'description': 'Divide fractions using reciprocal method', 'example': '3/4 ÷ 2/5 = ?'},
            9: {'name': 'Mixed Numbers', 'description': 'All operations with mixed numbers', 'example': '2½ + 1¾ = ?'},
            10: {'name': 'Complex Fraction Operations', 'description': 'Multi-step problems with order of operations', 'example': '(2/3 + 1/4) × 2½ = ?'},
        }
    },
    'percentages': {
        'name': 'Percentages',
        'levels': {
            1: {'name': 'Understanding Percentages', 'description': 'Recognize percentages, convert simple fractions', 'example': 'What is 50% as a fraction?'},
            2: {'name': 'Percentage of Amount (Simple)', 'description': 'Find 10%, 25%, 50% of amounts', 'example': 'Find 25% of €80'},
            3: {'name': 'Percentage of Amount (Any)', 'description': 'Find any percentage of an amount', 'example': 'Find 35% of €120'},
            4: {'name': 'Percentage Increase', 'description': 'Calculate amount after percentage increase', 'example': 'Increase €50 by 20%'},
            5: {'name': 'Percentage Decrease', 'description': 'Calculate amount after percentage decrease/discount', 'example': 'A €80 item has 15% off. Sale price?'},
            6: {'name': 'Finding the Percentage', 'description': 'Express one quantity as a percentage of another', 'example': 'What percentage is 15 of 60?'},
            7: {'name': 'Reverse Percentages', 'description': 'Find original amount given final and percentage', 'example': 'After 20% increase, price is €60. Original?'},
            8: {'name': 'Percentage Change', 'description': 'Calculate percentage change between values', 'example': 'Price went from €40 to €52. What % increase?'},
            9: {'name': 'Compound Percentages', 'description': 'Multiple successive percentage changes', 'example': 'Price increases 10% then decreases 10%. Net effect?'},
            10: {'name': 'Complex Applications', 'description': 'Multi-step real-world percentage problems', 'example': 'VAT, profit margins, depreciation'},
        }
    },
}


def generate_questions_for_level(client, topic, topic_name, level, level_config, count=15):
    """Generate questions for a specific level"""
    
    # Determine difficulty band
    if level <= 3:
        band = 'beginner'
    elif level <= 7:
        band = 'intermediate'
    else:
        band = 'advanced'
    
    prompt = f"""Generate exactly {count} multiple choice mathematics questions for Irish Junior Cycle students (14 year olds).

TOPIC: {topic_name}
LEVEL: {level} of 10
LEVEL NAME: {level_config['name']}
LEVEL DESCRIPTION: {level_config['description']}
EXAMPLE QUESTION AT THIS LEVEL: {level_config['example']}

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
    "question_type": "calculation"
  }}
]

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
        
        # Add metadata
        for q in questions:
            q['topic'] = topic
            q['difficulty_level'] = level
            q['difficulty_band'] = band
            q['level_name'] = level_config['name']
        
        return questions
        
    except json.JSONDecodeError as e:
        print(f"   ✗ JSON parse error: {e}")
        return []
    except Exception as e:
        print(f"   ✗ API error: {e}")
        return []


def save_questions_to_db(questions):
    """Save questions to the database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    saved = 0
    skipped = 0
    
    for q in questions:
        # Check for duplicate
        cursor.execute("""
            SELECT id FROM questions_adaptive 
            WHERE topic = ? AND difficulty_level = ? AND question_text = ?
        """, (q['topic'], q['difficulty_level'], q['question_text']))
        
        if cursor.fetchone():
            skipped += 1
            continue
        
        # Insert
        complexity_factors = json.dumps({
            'level_name': q.get('level_name', ''),
            'question_type': q.get('question_type', 'calculation')
        })
        
        cursor.execute("""
            INSERT INTO questions_adaptive 
            (topic, question_text, option_a, option_b, option_c, option_d,
             correct_answer, explanation, difficulty_level, difficulty_band,
             complexity_factors, question_type, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
        """, (
            q['topic'],
            q['question_text'],
            q['options'][0],
            q['options'][1],
            q['options'][2],
            q['options'][3],
            q['correct'],
            q['explanation'],
            q['difficulty_level'],
            q['difficulty_band'],
            complexity_factors,
            q.get('question_type', 'calculation')
        ))
        saved += 1
    
    conn.commit()
    conn.close()
    
    return saved, skipped


def get_current_counts(topic):
    """Get current question counts per level"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    counts = {}
    for level in range(1, 11):
        cursor.execute("""
            SELECT COUNT(*) FROM questions_adaptive 
            WHERE topic = ? AND difficulty_level = ?
        """, (topic, level))
        counts[level] = cursor.fetchone()[0]
    
    conn.close()
    return counts


def main():
    print("=" * 60)
    print("ADAPTIVE QUESTION GENERATOR")
    print("=" * 60)
    
    # Initialize client
    client = anthropic.Anthropic(api_key=API_KEY)
    print("✓ Anthropic client initialized")
    
    # Show available topics
    print("\nAvailable topics:")
    for i, topic in enumerate(TOPIC_PROGRESSIONS.keys(), 1):
        print(f"  {i}. {topic}")
    
    print("\nWhich topic? (Enter number or 'all' for all topics)")
    choice = input("> ").strip().lower()
    
    if choice == 'all':
        topics_to_generate = list(TOPIC_PROGRESSIONS.keys())
    else:
        try:
            idx = int(choice) - 1
            topics_to_generate = [list(TOPIC_PROGRESSIONS.keys())[idx]]
        except (ValueError, IndexError):
            print("Invalid choice!")
            return
    
    print("\nQuestions per level? (default: 15)")
    count_input = input("> ").strip()
    questions_per_level = int(count_input) if count_input else 15
    
    print("\nWhich levels? (e.g., '1-5' or '1,3,5,7' or 'all')")
    levels_input = input("> ").strip().lower()
    
    if levels_input == 'all' or not levels_input:
        levels = list(range(1, 11))
    elif '-' in levels_input:
        start, end = levels_input.split('-')
        levels = list(range(int(start), int(end) + 1))
    else:
        levels = [int(x.strip()) for x in levels_input.split(',')]
    
    print("\n" + "=" * 60)
    print("GENERATING QUESTIONS")
    print("=" * 60)
    
    total_saved = 0
    total_skipped = 0
    
    for topic in topics_to_generate:
        topic_config = TOPIC_PROGRESSIONS[topic]
        print(f"\n📚 {topic_config['name']}")
        print("-" * 40)
        
        # Show current counts
        counts = get_current_counts(topic)
        print(f"Current counts: {counts}")
        
        for level in levels:
            if level not in topic_config['levels']:
                continue
            
            level_config = topic_config['levels'][level]
            print(f"\n  Level {level}: {level_config['name']}")
            print(f"  Example: {level_config['example']}")
            print(f"  Generating {questions_per_level} questions...")
            
            questions = generate_questions_for_level(
                client, topic, topic_config['name'], 
                level, level_config, questions_per_level
            )
            
            if questions:
                saved, skipped = save_questions_to_db(questions)
                total_saved += saved
                total_skipped += skipped
                print(f"  ✓ Saved: {saved}, Skipped (duplicates): {skipped}")
            else:
                print(f"  ✗ No questions generated")
    
    # Final summary
    print("\n" + "=" * 60)
    print("GENERATION COMPLETE")
    print("=" * 60)
    print(f"\nTotal saved: {total_saved}")
    print(f"Total skipped: {total_skipped}")
    
    # Show final counts
    print("\nFinal question counts:")
    for topic in topics_to_generate:
        counts = get_current_counts(topic)
        total = sum(counts.values())
        print(f"\n{topic}: {total} total")
        for level, count in counts.items():
            bar = "█" * min(count, 20)
            print(f"  Level {level:2d}: {count:3d} {bar}")


if __name__ == '__main__':
    main()

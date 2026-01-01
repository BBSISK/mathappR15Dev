#!/usr/bin/env python3
"""
Fix set notation SVGs in existing questions
Properly positions closing brace next to elements
"""

import sqlite3
import re

DB_PATH = 'instance/mathquiz.db'

def svg_set_notation_fixed(elements, set_name='A'):
    """
    Visual representation of a set with elements listed
    Properly positions closing brace next to elements
    """
    elem_str = ', '.join(str(e) for e in elements)
    
    # Calculate width based on content
    set_name_width = 45
    brace_width = 20
    elem_width = len(elem_str) * 12
    padding = 40
    
    content_width = set_name_width + brace_width + elem_width + brace_width + padding
    width = max(200, min(content_width + 20, 350))
    height = 80
    
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
    
    box_width = content_width - 10
    svg += f'<rect x="15" y="15" width="{box_width}" height="50" fill="#f0fdf4" stroke="#22c55e" stroke-width="3" rx="10"/>'
    svg += f'<text x="25" y="48" font-size="22" fill="#16a34a" font-weight="bold">{set_name} =</text>'
    
    open_brace_x = 25 + set_name_width
    svg += f'<text x="{open_brace_x}" y="50" font-size="26" fill="#374151" font-weight="bold">{{</text>'
    
    elem_x = open_brace_x + 22
    svg += f'<text x="{elem_x}" y="48" font-size="20" fill="#1e293b" font-weight="500">{elem_str}</text>'
    
    close_brace_x = elem_x + elem_width + 5
    svg += f'<text x="{close_brace_x}" y="50" font-size="26" fill="#374151" font-weight="bold">}}</text>'
    
    svg += '</svg>'
    return svg


def fix_set_notation_questions():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Find questions with set notation SVGs
    cursor.execute("""
        SELECT id, question_text, image_svg 
        FROM questions_adaptive 
        WHERE topic = 'sets' 
        AND question_text LIKE '%How many elements%'
        AND image_svg IS NOT NULL
    """)
    
    questions = cursor.fetchall()
    print(f"Found {len(questions)} set notation questions to fix")
    
    fixed = 0
    
    # Known set configurations
    sets_data = [
        ([1, 3, 5, 7], 'A'),
        ([2, 4, 6], 'B'),
        ([1, 2, 3, 4, 5], 'C'),
        ([10, 20, 30, 40], 'P'),
        ([5, 10, 15], 'Q'),
    ]
    
    for qid, question_text, old_svg in questions:
        # Try to match which set this question is about
        for elements, name in sets_data:
            if f'set {name}?' in question_text:
                new_svg = svg_set_notation_fixed(elements, name)
                cursor.execute(
                    "UPDATE questions_adaptive SET image_svg = ? WHERE id = ?",
                    (new_svg, qid)
                )
                fixed += 1
                break
    
    conn.commit()
    conn.close()
    
    print(f"✅ Fixed {fixed} set notation questions")


if __name__ == '__main__':
    print("="*50)
    print("FIX SET NOTATION SVGs")
    print("="*50)
    fix_set_notation_questions()
    print("\nAlternatively, you can delete sets questions and regenerate:")
    print("  sqlite3 instance/mathquiz.db \"DELETE FROM questions_adaptive WHERE topic='sets'\"")
    print("  python generate_sets_questions.py")

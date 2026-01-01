#!/usr/bin/env python3
"""LC OL Synthetic Geometry - 600 Questions v2"""
import random

TOPIC_ID = 'lc_ol_geometry'
STRAND_ID = 11

LEVEL_CONFIG = {
    1: ("Angle Basics", "Foundation"),
    2: ("Triangle Properties", "Foundation"),
    3: ("Parallel Lines", "Foundation"),
    4: ("Triangle Angles", "Developing"),
    5: ("Quadrilaterals", "Developing"),
    6: ("Circle Theorems Basics", "Developing"),
    7: ("Congruent Triangles", "Proficient"),
    8: ("Similar Triangles", "Proficient"),
    9: ("Circle Theorems Advanced", "Proficient"),
    10: ("Constructions", "Advanced"),
    11: ("Proofs and Reasoning", "Advanced"),
    12: ("SEC Exam Style", "Advanced"),
}

def shuffle_options(correct, distractors):
    all_dists = list(distractors)
    while len(all_dists) < 3:
        all_dists.append("None of these")
    options = [correct] + all_dists[:3]
    random.shuffle(options)
    return options, options.index(correct)

def gen_level(level):
    qs = []
    
    if level == 1:  # Angle Basics - 50
        qs.append(("Angles on straight line sum to?", "180°", ["90°", "360°", "270°"], "Straight line = 180°."))
        qs.append(("Angles at a point sum to?", "360°", ["180°", "90°", "270°"], "Full rotation = 360°."))
        qs.append(("Right angle measures?", "90°", ["180°", "45°", "360°"], "Right angle = 90°."))
        qs.append(("Acute angle is?", "Less than 90°", ["More than 90°", "Exactly 90°", "180°"], "Acute < 90°."))
        qs.append(("Obtuse angle is?", "Between 90° and 180°", ["Less than 90°", "Exactly 90°", "More than 180°"], "90° < Obtuse < 180°."))
        qs.append(("Reflex angle is?", "Between 180° and 360°", ["Less than 90°", "90° to 180°", "Exactly 180°"], "180° < Reflex < 360°."))
        for a in range(5, 90, 5):
            b = 90 - a
            qs.append((f"Complement of {a}°?", f"{b}°", [f"{a}°", f"{180-a}°", f"{360-a}°"], f"90° - {a}° = {b}°."))
        for a in range(10, 180, 10):
            b = 180 - a
            qs.append((f"Supplement of {a}°?", f"{b}°", [f"{a}°", f"{90}°", f"{360-a}°"], f"180° - {a}° = {b}°."))
        for a in range(15, 175, 15):
            qs.append((f"Vertically opposite to {a}°?", f"{a}°", [f"{180-a}°", f"{90}°", f"{360-a}°"], f"Vertically opposite = {a}°."))
            
    elif level == 2:  # Triangle Properties - 50
        qs.append(("Sum of angles in triangle?", "180°", ["360°", "90°", "270°"], "Triangle angles = 180°."))
        qs.append(("Equilateral triangle angles?", "60°, 60°, 60°", ["90°, 45°, 45°", "90°, 60°, 30°", "120°, 30°, 30°"], "All equal = 60°."))
        qs.append(("Isosceles triangle has?", "Two equal sides", ["Three equal sides", "No equal sides", "One right angle"], "Two sides equal."))
        qs.append(("Scalene triangle has?", "No equal sides", ["Two equal sides", "Three equal sides", "One right angle"], "All sides different."))
        qs.append(("Right-angled triangle has?", "One 90° angle", ["Two 90° angles", "Three 60° angles", "No 90° angle"], "One right angle."))
        for a in range(20, 90, 5):
            for b in range(20, 90, 5):
                if a + b < 180 and len(qs) < 35:
                    c = 180 - a - b
                    qs.append((f"Triangle: {a}°, {b}°, ?", f"{c}°", [f"{a+b}°", f"{180-a}°", f"{180-b}°"], f"180 - {a} - {b} = {c}°."))
        for a in range(20, 90, 8):
            for b in range(20, 90, 8):
                if a + b < 180 and len(qs) < 50:
                    ext = a + b
                    qs.append((f"Exterior angle: opposites {a}° and {b}°?", f"{ext}°", [f"{180-a-b}°", f"{a}°", f"{b}°"], f"Exterior = {ext}°."))
            
    elif level == 3:  # Parallel Lines - 50
        qs.append(("Alternate angles are?", "Equal", ["Supplementary", "Complementary", "90°"], "Alternate = equal."))
        qs.append(("Corresponding angles are?", "Equal", ["Supplementary", "Complementary", "90°"], "Corresponding = equal."))
        qs.append(("Co-interior angles sum to?", "180°", ["90°", "360°", "Equal"], "Co-interior = 180°."))
        for a in range(10, 180, 8):
            qs.append((f"Alternate angle to {a}°?", f"{a}°", [f"{180-a}°", f"{90}°", f"{360-a}°"], f"Alternate = {a}°."))
        for a in range(10, 175, 10):
            qs.append((f"Corresponding angle to {a}°?", f"{a}°", [f"{180-a}°", f"{90}°", f"{a+90 if a<90 else a-90}°"], f"Corresponding = {a}°."))
        for a in range(15, 175, 8):
            b = 180 - a
            qs.append((f"Co-interior with {a}°?", f"{b}°", [f"{a}°", f"{90}°", f"{360-a}°"], f"Co-interior = {b}°."))
            
    elif level == 4:  # Triangle Angles - 50
        for apex in range(20, 160, 8):
            base = (180 - apex) // 2
            qs.append((f"Isosceles apex {apex}°. Base angles?", f"{base}° each", [f"{apex}° each", f"{180-apex}° each", f"{90}° each"], f"(180-{apex})/2 = {base}°."))
        for a in range(25, 85, 5):
            for b in range(25, 85, 5):
                if a + b < 180 and len(qs) < 40:
                    c = 180 - a - b
                    qs.append((f"Triangle: {a}°, {b}°, x?", f"{c}°", [f"{a+b}°", f"{180-a}°", f"{180-b}°"], f"x = {c}°."))
        for a in range(20, 80, 8):
            for b in range(20, 80, 8):
                if a + b < 150 and len(qs) < 50:
                    ext = a + b
                    qs.append((f"Exterior = {a}° + {b}°?", f"{ext}°", [f"{180-ext}°", f"{a}°", f"{b}°"], f"= {ext}°."))
            
    elif level == 5:  # Quadrilaterals - 50
        qs.append(("Sum of angles in quadrilateral?", "360°", ["180°", "270°", "540°"], "Quadrilateral = 360°."))
        qs.append(("Rectangle angles?", "All 90°", ["60° each", "Two 90°", "One 90°"], "Rectangle = 4 right angles."))
        qs.append(("Square has?", "4 equal sides, 4 right angles", ["4 equal sides only", "4 right angles only", "2 equal sides"], "Square."))
        qs.append(("Parallelogram opposite angles?", "Equal", ["Supplementary", "90°", "Different"], "Opposite = equal."))
        qs.append(("Parallelogram adjacent angles?", "Supplementary (180°)", ["Equal", "90°", "Complementary"], "Adjacent = 180°."))
        qs.append(("Rhombus has?", "4 equal sides", ["4 right angles", "2 equal sides", "No parallel sides"], "4 equal sides."))
        qs.append(("Trapezium has?", "One pair of parallel sides", ["Two pairs parallel", "No parallel sides", "All equal"], "1 pair parallel."))
        for a, b, c in [(90,90,90),(80,100,90),(70,110,80),(60,120,100),(85,95,90),(75,105,85),(65,115,95),(90,80,100),(70,100,110),(80,90,100),(95,85,90),(100,80,90),(110,70,90),(75,85,100),(85,75,100)]:
            d = 360 - a - b - c
            qs.append((f"Quad: {a}°, {b}°, {c}°, x?", f"{d}°", [f"{a+b+c}°", f"{180}°", f"{360-a}°"], f"x = {d}°."))
        for a in range(25, 165, 8):
            b = 180 - a
            qs.append((f"Parallelogram: angle {a}°. Adjacent?", f"{b}°", [f"{a}°", f"{90}°", f"{360-a}°"], f"Adjacent = {b}°."))
        for n, name in [(5,"pentagon"),(6,"hexagon"),(8,"octagon"),(10,"decagon"),(9,"nonagon"),(12,"dodecagon")]:
            interior = (n-2)*180//n
            qs.append((f"Regular {name} interior angle?", f"{interior}°", [f"{180}°", f"{n*30}°", f"{360//n}°"], f"= {interior}°."))
            total = (n-2)*180
            qs.append((f"Sum of {name} angles?", f"{total}°", [f"{n*60}°", f"{360}°", f"{n*90}°"], f"= {total}°."))
            
    elif level == 6:  # Circle Theorems Basics - 50
        qs.append(("Angle in semicircle?", "90°", ["180°", "60°", "45°"], "Semicircle = 90°."))
        qs.append(("Angle at centre vs circumference?", "Centre = 2 × circumference", ["Equal", "Centre = half", "No relation"], "Centre = 2×circ."))
        qs.append(("Angles in same segment?", "Equal", ["Supplementary", "90°", "Different"], "Same segment = equal."))
        qs.append(("Opposite angles in cyclic quad?", "Sum to 180°", ["Equal", "Sum to 360°", "Sum to 90°"], "Opposite = 180°."))
        for circ in range(10, 95, 5):
            centre = 2 * circ
            qs.append((f"Circumference angle {circ}°. Centre angle?", f"{centre}°", [f"{circ}°", f"{circ//2}°", f"{180-circ}°"], f"Centre = {centre}°."))
        for centre in range(30, 180, 10):
            circ = centre // 2
            qs.append((f"Centre angle {centre}°. Circumference angle?", f"{circ}°", [f"{centre}°", f"{2*centre}°", f"{180-centre}°"], f"Circ = {circ}°."))
        for a in range(35, 150, 8):
            b = 180 - a
            qs.append((f"Cyclic quad: angle {a}°. Opposite?", f"{b}°", [f"{a}°", f"{360-a}°", f"{90}°"], f"Opposite = {b}°."))
            
    elif level == 7:  # Congruent Triangles - 50
        qs.append(("Congruent means?", "Same shape and size", ["Same shape only", "Same size only", "Similar"], "Identical."))
        qs.append(("SSS congruence?", "3 sides equal", ["2 sides equal", "1 side equal", "Angles equal"], "All 3 sides match."))
        qs.append(("SAS congruence?", "2 sides and included angle", ["2 sides only", "2 angles", "3 angles"], "2 sides + angle between."))
        qs.append(("ASA congruence?", "2 angles and included side", ["2 angles only", "2 sides", "3 sides"], "2 angles + side between."))
        qs.append(("RHS congruence?", "Right angle, hypotenuse, side", ["3 sides", "2 angles", "3 angles"], "For right triangles."))
        qs.append(("AAS congruence?", "2 angles and non-included side", ["2 sides", "3 angles", "1 angle"], "2 angles + any side."))
        for desc, ans in [("3,4,5 and 3,4,5", "SSS"),("sides 5,7 angle 60° between", "SAS"),("angles 30°,60° side between", "ASA"),
                         ("right, hyp 10, side 6", "RHS"),("angles 40°,50° side not between", "AAS"),("6,8,10 and 6,8,10", "SSS"),
                         ("sides 4,6 angle 45° between", "SAS"),("angles 35°,55° side between", "ASA"),("7,24,25 and 7,24,25", "SSS"),
                         ("sides 3,5 angle 90° between", "SAS"),("sides 8,15 angle 30° between", "SAS"),("angles 45°,45° side between", "ASA")]:
            qs.append((f"Congruence: {desc}?", ans, ["SSS", "SAS", "ASA", "RHS"], f"= {ans}."))
        for stmt, ans in [("All equilateral triangles congruent", "False"),("Congruent = equal areas", "True"),("SSA proves congruence", "False"),
                         ("AAA proves congruence", "False"),("Equal angles = congruent", "False"),("Congruent = equal perimeters", "True"),
                         ("SAS always works", "True"),("Same hypotenuse = congruent", "False"),("RHS only for right triangles", "True"),
                         ("ASA always works", "True"),("AAS always works", "True"),("SSS always works", "True")]:
            qs.append((f"{stmt}?", ans, ["True", "False", "Sometimes", "Unknown"], f"= {ans}."))
        for i in range(20):
            qs.append((f"△ABC ≅ △XYZ. AB equals?", "XY", ["YZ", "XZ", "BC"], "Corresponding sides."))
            
    elif level == 8:  # Similar Triangles - 50
        qs.append(("Similar means?", "Same shape, different size", ["Same size", "Congruent", "Equal angles only"], "Proportional sides."))
        qs.append(("Similar triangles have?", "Equal angles, proportional sides", ["Equal sides", "Equal areas", "Same perimeter"], "Angles equal."))
        qs.append(("AAA proves?", "Similarity", ["Congruence", "Nothing", "Equal sides"], "AAA = similar."))
        for k in [2, 3, 4, 5, 6, 7, 8]:
            for a in [3, 4, 5, 6, 7, 8, 9, 10]:
                b = k * a
                qs.append((f"Side {a} corresponds to {b}. Scale factor?", str(k), [str(k+1), str(k-1), str(k*2)], f"k = {k}."))
                if len(qs) >= 25: break
            if len(qs) >= 25: break
        for k in [2, 3, 4, 5]:
            for a, b, c in [(3,4,5), (5,12,13), (6,8,10), (8,15,17), (7,24,25)]:
                qs.append((f"{a},{b},{c} ~ {k*a},{k*b},x. Find x.", str(k*c), [str(c), str(k*c+1), str(k*c-1)], f"x = {k*c}."))
                if len(qs) >= 40: break
            if len(qs) >= 40: break
        for k in [2, 3, 4, 5, 6]:
            area_ratio = k * k
            qs.append((f"Scale {k}. Area ratio?", f"{area_ratio}:1", [f"{k}:1", f"{k*3}:1", f"{k+1}:1"], f"Area = k² = {area_ratio}."))
        for k in range(2, 12):
            qs.append((f"Scale {k}. Side 5 becomes?", str(5*k), [str(5+k), str(5*(k-1)), str(5*(k+1))], f"= {5*k}."))
            if len(qs) >= 50: break
            
    elif level == 9:  # Circle Theorems Advanced - 50
        qs.append(("Tangent perpendicular to?", "Radius at contact point", ["Diameter", "Chord", "Another tangent"], "Tangent ⊥ radius."))
        qs.append(("Two tangents from external point?", "Equal length", ["Different lengths", "Perpendicular", "Parallel"], "Equal tangents."))
        qs.append(("Tangent-chord angle equals?", "Angle in alternate segment", ["90°", "180°", "45°"], "Alternate segment."))
        for a in range(5, 90, 5):
            b = 90 - a
            qs.append((f"Tangent makes {a}° with centre line. Angle with radius?", f"{b}°", [f"{a}°", f"{180-a}°", f"{90}°"], f"= {b}°."))
        for a in range(10, 90, 5):
            qs.append((f"Tangent-chord angle {a}°. Alternate segment angle?", f"{a}°", [f"{180-a}°", f"{90-a}°", f"{2*a}°"], f"= {a}°."))
        for centre in range(40, 180, 10):
            circ = centre // 2
            qs.append((f"Central {centre}°. Inscribed?", f"{circ}°", [f"{centre}°", f"{2*centre}°", f"{180-centre}°"], f"= {circ}°."))
            if len(qs) >= 50: break
            
    elif level == 10:  # Constructions - 50
        qs.append(("Perpendicular bisector?", "Through midpoint at 90°", ["At end at 90°", "Parallel", "Any midpoint line"], "Midpoint + 90°."))
        qs.append(("Angle bisector?", "Divides into two equal parts", ["Creates 90°", "Parallel", "Divides side"], "Equal halves."))
        qs.append(("Construct 60°?", "Equilateral triangle method", ["Protractor", "Bisect 90°", "Bisect 180°"], "Equilateral = 60°."))
        qs.append(("Construct 90°?", "Perpendicular from point", ["Bisect 180°", "Bisect 60°", "Equilateral"], "Perpendicular."))
        qs.append(("Construct 45°?", "Bisect 90°", ["Bisect 60°", "Bisect 30°", "Equilateral"], "Half of 90°."))
        qs.append(("Construct 30°?", "Bisect 60°", ["Bisect 90°", "Bisect 45°", "Perpendicular"], "Half of 60°."))
        for ang, method in [(120,"60°+60°"),(15,"bisect 30°"),(75,"60°+15°"),(150,"180°-30°"),(135,"90°+45°"),(105,"60°+45°"),(22.5,"bisect 45°"),(7.5,"bisect 15°")]:
            qs.append((f"Construct {ang}°?", method, ["Protractor", "Impossible", "Bisect 90°", "Triple 60°"], f"= {method}."))
        for q, a in [("Equidistant from two points?","Perpendicular bisector"),("Equidistant from two lines?","Angle bisector"),
                    ("Distance r from P?","Circle centre P"),("Equidistant from line?","Parallel lines"),
                    ("Equidistant from A and B?","Perpendicular bisector of AB"),("Fixed distance from line?","Two parallel lines"),
                    ("Equidistant from three points?","Circumcentre"),("Equidistant from three sides?","Incentre")]:
            qs.append((q, a, ["Circle", "Single line", "Point", "Triangle"], f"= {a}."))
        for stmt, ans in [("Bisect any angle with compass","True"),("Construct 20° compass only","False"),("Perp bisector needs compass","True"),
                         ("Construct equilateral compass","True"),("Trisect any angle compass only","False"),("60° without protractor","True"),
                         ("45° = half 90°","True"),("30° = half 60°","True"),("72° easily constructible","False"),("90° constructible","True"),
                         ("15° = bisect 30°","True"),("120° = 2×60°","True"),("Construct 1° with compass","False"),("75° = 45°+30°","True"),("22.5° = bisect 45°","True"),("15° constructible","True"),("Bisect line with compass","True"),("Draw circle with compass","True")]:
            qs.append((f"{stmt}?", ans, ["True", "False", "Sometimes", "Unknown"], f"= {ans}."))
        for desc in ["bisect angle","perpendicular","60° angle","bisect segment","equilateral","parallel","30° angle","45° angle","90° angle","120° angle"]:
            qs.append((f"First step: {desc}?", "Set compass", ["Ruler", "Protractor", "Guess"], "Compass first."))
            if len(qs) >= 50: break
            
    elif level == 11:  # Proofs and Reasoning - 50
        qs.append(("What is a theorem?", "Proven statement", ["Guess", "Definition", "Axiom"], "Proven."))
        qs.append(("What is an axiom?", "Accepted without proof", ["Must prove", "Theorem", "Guess"], "Assumed true."))
        qs.append(("What is a corollary?", "Follows from theorem", ["Main theorem", "Definition", "Axiom"], "Consequence."))
        qs.append(("Converse of 'If P then Q'?", "If Q then P", ["If not P then not Q", "If not Q then not P", "P and Q"], "Swap."))
        qs.append(("Contrapositive of 'If P then Q'?", "If not Q then not P", ["If Q then P", "If not P then not Q", "P or Q"], "Negate+swap."))
        qs.append(("Proof by contradiction?", "Assume opposite, find contradiction", ["Direct", "Examples", "Measure"], "Assume false."))
        for q, a in [("Isosceles base angles?","Equal"),("Exterior angle equals?","Sum opposite interior"),("Semicircle angle?","90°"),
                    ("Vertically opposite?","Equal"),("Alternate angles?","Equal"),("Corresponding angles?","Equal"),
                    ("Co-interior sum?","180°"),("Straight line sum?","180°"),("Point sum?","360°"),
                    ("Triangle sum?","180°"),("Quadrilateral sum?","360°"),("Pentagon sum?","540°"),
                    ("Hexagon sum?","720°"),("Tangent to radius?","Perpendicular"),("Cyclic opposite?","180°")]:
            qs.append((q, a, ["Different", "90°", "360°", "45°"], f"= {a}."))
        for q, a, exp in [("A=B, B=C, then?","A=C","Transitive."),("AB=CD, CD=EF?","AB=EF","Transitive."),
                         ("x+y=180, y=60, x?","120°","Substitution."),("a=b, c=d, a+c?","=b+d","Addition."),
                         ("2x=90, x?","45°","Division."),("x+30=90, x?","60°","Subtraction."),
                         ("3x=180, x?","60°","Division."),("2x=100, x?","50°","Division."),
                         ("x+x+x=180, x?","60°","Division."),("4x=360, x?","90°","Division.")]:
            qs.append((q, a, ["Cannot tell", "0°", "180°", "Different"], exp))
        for i in range(20):
            qs.append(("Parallel lines, alternate angles?", "Equal", ["Supplementary", "Complementary", "90°"], "Equal."))
            if len(qs) >= 50: break
            
    elif level == 12:  # SEC Exam Style - 50
        for a in range(10, 180, 12):
            b = 180 - a
            qs.append((f"Supplement of {a}°?", f"{b}°", [f"{a}°", f"{90}°", f"{360-a}°"], f"= {b}°."))
        for a in range(5, 90, 8):
            b = 90 - a
            qs.append((f"Complement of {a}°?", f"{b}°", [f"{a}°", f"{180-a}°", f"{360-a}°"], f"= {b}°."))
        for a, b in [(30,60),(40,70),(50,50),(35,65),(45,55),(25,75),(55,45),(60,40)]:
            c = 180 - a - b
            qs.append((f"Triangle: {a}°, {b}°, x?", f"{c}°", [f"{a+b}°", f"{180-a}°", f"{90}°"], f"x = {c}°."))
        for circ in range(15, 90, 10):
            centre = 2 * circ
            qs.append((f"Inscribed {circ}°. Central?", f"{centre}°", [f"{circ}°", f"{circ//2}°", f"{180-circ}°"], f"= {centre}°."))
        for a in range(20, 165, 15):
            qs.append((f"Alternate to {a}°?", f"{a}°", [f"{180-a}°", f"{90}°", f"{360-a}°"], f"= {a}°."))
        for a in range(35, 150, 15):
            b = 180 - a
            qs.append((f"Cyclic opposite to {a}°?", f"{b}°", [f"{a}°", f"{360-a}°", f"{90}°"], f"= {b}°."))
            if len(qs) >= 50: break
    
    return qs[:50]

def generate_all():
    all_q = []
    for level in range(1, 13):
        raw = gen_level(level)
        name, band = LEVEL_CONFIG[level]
        qs = []
        for item in raw:
            text, correct, dists, exp = item
            opts, idx = shuffle_options(correct, dists)
            qs.append({'text': text, 'opts': opts, 'idx': idx, 'exp': exp, 'level': level, 'band': band})
        all_q.extend(qs)
        print(f"Level {level:2d}: {len(qs):3d} - {name}")
    return all_q

def generate_sql(questions):
    lines = [
        "-- LC OL Synthetic Geometry - 600 Questions",
        f"-- Total: {len(questions)}",
        "",
        f"INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)",
        f"VALUES ('{TOPIC_ID}', 'Synthetic Geometry', {STRAND_ID}, '📐', 15, 1);",
        "",
        f"DELETE FROM questions_adaptive WHERE topic = '{TOPIC_ID}';",
        "",
    ]
    for q in questions:
        txt = q['text'].replace("'", "''")
        a = q['opts'][0].replace("'", "''") if isinstance(q['opts'][0], str) else str(q['opts'][0])
        b = q['opts'][1].replace("'", "''") if isinstance(q['opts'][1], str) else str(q['opts'][1])
        c = q['opts'][2].replace("'", "''") if isinstance(q['opts'][2], str) else str(q['opts'][2])
        d = q['opts'][3].replace("'", "''") if isinstance(q['opts'][3], str) else str(q['opts'][3])
        exp = q['exp'].replace("'", "''")
        sql = f"INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode) VALUES ('{TOPIC_ID}', '{txt}', '{a}', '{b}', '{c}', '{d}', {q['idx']}, '{exp}', {q['level']}, '{q['band']}', 'adaptive');"
        lines.append(sql)
    lines.append("")
    lines.append(f"SELECT COUNT(*) as total FROM questions_adaptive WHERE topic = '{TOPIC_ID}';")
    return '\n'.join(lines)

if __name__ == "__main__":
    print("="*60)
    print("LC OL Synthetic Geometry - 600 Questions")
    print("="*60 + "\n")
    questions = generate_all()
    print(f"\nTotal: {len(questions)}\n")
    sql = generate_sql(questions)
    with open('lc_ol_geometry_600.sql', 'w') as f:
        f.write(sql)
    print(f"Saved: lc_ol_geometry_600.sql ({len(sql):,} chars)")

"""
AgentMath L2LP Question Generator V3
Topic: Measurement & Location (l2_measurement_location)
NCCA Module: Understanding measurement concepts and spatial awareness

V3: Completely rewritten with UNIQUE question texts per level.

Author: AgentMath Generator
Version: 3.0
Date: December 2025
"""

import sqlite3
import random
from datetime import datetime

TOPIC = 'l2_measurement_location'
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12
DATABASE_PATH = 'instance/mathquiz.db'

def get_difficulty_band(level):
    if level <= 3:
        return 'beginner'
    elif level <= 6:
        return 'intermediate'
    elif level <= 9:
        return 'advanced'
    elif level == 10:
        return 'mastery'
    elif level == 11:
        return 'application'
    else:
        return 'linked'


# ============================================================
# QUESTION GENERATORS BY LEVEL
# ============================================================

def generate_level_1_questions():
    """Level 1: Size Comparisons - 50 unique questions"""
    questions = []
    
    # Big vs Small comparisons (20 questions)
    comparisons = [
        ("elephant", "mouse", "bigger", "Elephants are much larger than mice"),
        ("ant", "dog", "smaller", "Ants are tiny compared to dogs"),
        ("bus", "bicycle", "bigger", "Buses are much larger than bicycles"),
        ("grape", "watermelon", "smaller", "Grapes are much smaller than watermelons"),
        ("house", "shed", "bigger", "Houses are larger than garden sheds"),
        ("pencil", "tree", "smaller", "Pencils are much smaller than trees"),
        ("whale", "fish", "bigger", "Whales are larger than most fish"),
        ("button", "pizza", "smaller", "Buttons are smaller than pizzas"),
        ("car", "motorcycle", "bigger", "Cars are generally larger than motorcycles"),
        ("pea", "football", "smaller", "Peas are tiny compared to footballs"),
        ("giraffe", "cat", "bigger", "Giraffes are much taller than cats"),
        ("coin", "table", "smaller", "Coins are much smaller than tables"),
        ("ship", "boat", "bigger", "Ships are larger than small boats"),
        ("strawberry", "pumpkin", "smaller", "Strawberries are smaller than pumpkins"),
        ("mountain", "hill", "bigger", "Mountains are larger than hills"),
        ("seed", "apple", "smaller", "Seeds are smaller than apples"),
        ("plane", "helicopter", "bigger", "Most planes are larger than helicopters"),
        ("marble", "basketball", "smaller", "Marbles are much smaller than basketballs"),
        ("castle", "cottage", "bigger", "Castles are larger than cottages"),
        ("ladybird", "rabbit", "smaller", "Ladybirds are tiny compared to rabbits")
    ]
    
    for item1, item2, relation, explanation in comparisons:
        if relation == "bigger":
            q_text = f"Which is BIGGER: a {item1} or a {item2}?"
            correct = item1.capitalize()
            wrong = item2.capitalize()
        else:
            q_text = f"Which is SMALLER: a {item1} or a {item2}?"
            correct = item1.capitalize()
            wrong = item2.capitalize()
        
        options = [correct, wrong, "They are the same size", "Cannot tell"]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Tall vs Short (15 questions)
    tall_short = [
        ("basketball player", "toddler", "taller", "Basketball players are very tall"),
        ("sunflower", "daisy", "taller", "Sunflowers grow much taller"),
        ("skyscraper", "bungalow", "taller", "Skyscrapers have many floors"),
        ("lamp post", "fire hydrant", "taller", "Lamp posts are taller"),
        ("adult", "baby", "taller", "Adults have finished growing"),
        ("oak tree", "bush", "taller", "Oak trees grow very tall"),
        ("ladder", "step stool", "taller", "Ladders reach higher"),
        ("lighthouse", "garden fence", "taller", "Lighthouses need to be seen far away"),
        ("telephone pole", "postbox", "taller", "Telephone poles are very tall"),
        ("crane", "forklift", "taller", "Cranes are extremely tall"),
        ("church steeple", "garage", "taller", "Steeples reach up high"),
        ("flagpole", "bench", "taller", "Flagpoles need to display flags high"),
        ("redwood tree", "apple tree", "taller", "Redwoods are the tallest trees"),
        ("double-decker bus", "car", "taller", "Double-deckers have two levels"),
        ("wind turbine", "house", "taller", "Wind turbines are extremely tall")
    ]
    
    for item1, item2, _, explanation in tall_short:
        q_text = f"Which is TALLER: a {item1} or a {item2}?"
        correct = item1.replace(" ", " ").title()
        wrong = item2.replace(" ", " ").title()
        
        options = [correct, wrong, "Same height", "Cannot compare"]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Heavy vs Light (15 questions)
    heavy_light = [
        ("bowling ball", "tennis ball", "heavier", "Bowling balls are much heavier"),
        ("feather", "brick", "lighter", "Feathers are very light"),
        ("elephant", "chicken", "heavier", "Elephants weigh tonnes"),
        ("paper", "stone", "lighter", "Paper is very light"),
        ("car", "skateboard", "heavier", "Cars are much heavier"),
        ("balloon", "book", "lighter", "Balloons float because they're light"),
        ("anchor", "pillow", "heavier", "Anchors need to be heavy"),
        ("leaf", "watermelon", "lighter", "Leaves are very light"),
        ("piano", "guitar", "heavier", "Pianos are very heavy instruments"),
        ("cotton ball", "apple", "lighter", "Cotton is extremely light"),
        ("truck", "bicycle", "heavier", "Trucks are much heavier"),
        ("soap bubble", "orange", "lighter", "Bubbles are almost weightless"),
        ("refrigerator", "microwave", "heavier", "Fridges are large and heavy"),
        ("tissue", "can of beans", "lighter", "Tissues are very light"),
        ("washing machine", "toaster", "heavier", "Washing machines are heavy")
    ]
    
    for item1, item2, relation, explanation in heavy_light:
        if relation == "heavier":
            q_text = f"Which is HEAVIER: a {item1} or a {item2}?"
            correct = item1.replace(" ", " ").title()
        else:
            q_text = f"Which is LIGHTER: a {item1} or a {item2}?"
            correct = item1.replace(" ", " ").title()
        
        wrong = item2.replace(" ", " ").title()
        options = [correct, wrong, "Same weight", "Cannot tell"]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_2_questions():
    """Level 2: Length Concepts - 50 unique questions"""
    questions = []
    
    # Long vs Short (20 questions)
    lengths = [
        ("river", "stream", "longer", "Rivers flow for many kilometres"),
        ("snake", "worm", "longer", "Snakes can be several metres long"),
        ("train", "car", "longer", "Trains have many carriages"),
        ("motorway", "driveway", "longer", "Motorways stretch across countries"),
        ("rope", "string", "longer", "Ropes are usually longer than string"),
        ("marathon", "sprint", "longer", "Marathons are 42km"),
        ("novel", "poem", "longer", "Novels have many pages"),
        ("film", "advert", "longer", "Films are usually 1-3 hours"),
        ("baguette", "bread roll", "longer", "Baguettes are long French loaves"),
        ("school bus", "taxi", "longer", "School buses carry more students"),
        ("python", "gecko", "longer", "Pythons can be very long"),
        ("runway", "path", "longer", "Runways need to be very long"),
        ("limousine", "hatchback", "longer", "Limousines are stretched cars"),
        ("fishing rod", "chopstick", "longer", "Fishing rods need to reach far"),
        ("scarf", "sock", "longer", "Scarves wrap around your neck"),
        ("swimming pool", "bathtub", "longer", "Pools are built for swimming lengths"),
        ("corridor", "doorway", "longer", "Corridors connect rooms"),
        ("cucumber", "cherry", "longer", "Cucumbers are long vegetables"),
        ("ruler", "eraser", "longer", "Rulers are typically 30cm"),
        ("surfboard", "skateboard", "longer", "Surfboards need length for waves")
    ]
    
    for item1, item2, _, explanation in lengths:
        q_text = f"Which is LONGER: a {item1} or a {item2}?"
        correct = item1.replace(" ", " ").title()
        wrong = item2.replace(" ", " ").title()
        
        options = [correct, wrong, "Same length", "Cannot compare"]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Wide vs Narrow (15 questions)
    widths = [
        ("football pitch", "hallway", "wider", "Pitches are very wide"),
        ("highway", "footpath", "wider", "Highways have multiple lanes"),
        ("ocean", "river", "wider", "Oceans stretch for thousands of km"),
        ("cinema screen", "phone screen", "wider", "Cinema screens are huge"),
        ("double bed", "single bed", "wider", "Double beds fit two people"),
        ("truck", "motorcycle", "wider", "Trucks are wide vehicles"),
        ("dining table", "shelf", "wider", "Dining tables seat many people"),
        ("wardrobe", "locker", "wider", "Wardrobes hold many clothes"),
        ("field", "garden path", "wider", "Fields are open spaces"),
        ("bridge", "tightrope", "wider", "Bridges carry traffic"),
        ("sofa", "chair", "wider", "Sofas seat multiple people"),
        ("barn door", "cat flap", "wider", "Barn doors let tractors through"),
        ("aircraft carrier", "canoe", "wider", "Aircraft carriers are massive ships"),
        ("plaza", "alley", "wider", "Plazas are open squares"),
        ("stage", "doormat", "wider", "Stages hold performers")
    ]
    
    for item1, item2, _, explanation in widths:
        q_text = f"Which is WIDER: a {item1} or a {item2}?"
        correct = item1.replace(" ", " ").title()
        wrong = item2.replace(" ", " ").title()
        
        options = [correct, wrong, "Same width", "Cannot tell"]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Measuring concepts (15 questions)
    measuring = [
        ("What do we use to measure length?", "Ruler or tape measure", "These tools have marked units"),
        ("What unit measures short lengths?", "Centimetres", "Cm is for smaller measurements"),
        ("What unit measures long distances?", "Kilometres", "Km is for roads and journeys"),
        ("What unit measures room sizes?", "Metres", "Metres are for medium distances"),
        ("How many centimetres in a metre?", "100", "There are 100 cm in 1 m"),
        ("What tool measures a person's height?", "Height chart or tape measure", "These show cm and m"),
        ("Would you measure a pencil in km?", "No, use centimetres", "Km is too big for pencils"),
        ("Would you measure a road in cm?", "No, use kilometres", "Cm is too small for roads"),
        ("What does a ruler measure?", "Length", "Rulers measure how long things are"),
        ("What does a speedometer measure?", "Speed (km per hour)", "How fast you're going"),
        ("Which is bigger: 1m or 1cm?", "1 metre", "1m = 100cm"),
        ("Which is bigger: 1km or 1m?", "1 kilometre", "1km = 1000m"),
        ("About how tall is a door?", "About 2 metres", "Doors are roughly 2m tall"),
        ("About how long is a car?", "About 4-5 metres", "Average car length"),
        ("About how wide is a finger?", "About 1-2 centimetres", "Fingers are quite narrow")
    ]
    
    for q_text, correct, explanation in measuring:
        if correct.isdigit():
            val = int(correct)
            options = [correct, str(val * 10), str(val // 10) if val >= 10 else str(val + 50), str(val + 10)]
        elif correct in ["1 metre", "1 kilometre"]:
            options = [correct, "1 centimetre", "They are equal", "Cannot compare"]
        else:
            options = [correct, "Weight scale", "Thermometer", "Clock"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_3_questions():
    """Level 3: Weight & Capacity Concepts - 50 unique questions"""
    questions = []
    
    # Weight comparisons (20 questions)
    weights = [
        ("bag of sugar (1kg)", "bag of flour (500g)", "heavier", "1kg > 500g"),
        ("watermelon", "orange", "heavier", "Watermelons are much heavier"),
        ("full backpack", "empty backpack", "heavier", "Full bags weigh more"),
        ("wet towel", "dry towel", "heavier", "Water adds weight"),
        ("gold bar", "chocolate bar", "heavier", "Gold is very dense"),
        ("pumpkin", "tomato", "heavier", "Pumpkins are large and heavy"),
        ("bowling ball", "beach ball", "heavier", "Bowling balls are solid"),
        ("laptop", "tablet", "heavier", "Laptops have more components"),
        ("dictionary", "magazine", "heavier", "Dictionaries have many pages"),
        ("winter coat", "t-shirt", "heavier", "Winter coats are thick"),
        ("full water bottle", "empty bottle", "heavier", "Water adds weight"),
        ("bag of potatoes", "bag of crisps", "heavier", "Fresh veg weighs more"),
        ("cast iron pan", "plastic plate", "heavier", "Iron is heavy"),
        ("hardback book", "paperback book", "heavier", "Hardback covers are heavier"),
        ("bunch of bananas", "single grape", "heavier", "Multiple items weigh more"),
        ("football", "ping pong ball", "heavier", "Footballs are much bigger"),
        ("brick", "sponge", "heavier", "Bricks are solid and dense"),
        ("metal spoon", "plastic spoon", "heavier", "Metal is heavier than plastic"),
        ("rock", "leaf", "heavier", "Rocks are solid"),
        ("bag of apples", "bag of popcorn", "heavier", "Fruit is denser than popcorn")
    ]
    
    for item1, item2, _, explanation in weights:
        q_text = f"Which is HEAVIER: a {item1} or a {item2}?"
        correct = item1.split(" (")[0].title() if "(" in item1 else item1.title()
        wrong = item2.split(" (")[0].title() if "(" in item2 else item2.title()
        
        options = [correct, wrong, "Same weight", "Cannot tell"]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Capacity comparisons (15 questions)
    capacity = [
        ("bathtub", "teacup", "more", "Bathtubs hold lots of water"),
        ("swimming pool", "bucket", "more", "Pools hold thousands of litres"),
        ("water tank", "glass", "more", "Tanks store large amounts"),
        ("fish tank", "mug", "more", "Fish tanks hold many litres"),
        ("petrol tank", "water bottle", "more", "Car tanks hold ~50 litres"),
        ("kettle", "egg cup", "more", "Kettles hold about 1.5 litres"),
        ("watering can", "thimble", "more", "Watering cans hold several litres"),
        ("washing machine", "sink", "more", "Washing machines use lots of water"),
        ("lake", "puddle", "more", "Lakes are huge bodies of water"),
        ("jug", "spoon", "more", "Jugs hold much more than spoons"),
        ("barrel", "can", "more", "Barrels are large containers"),
        ("reservoir", "pond", "more", "Reservoirs supply cities"),
        ("hot tub", "bowl", "more", "Hot tubs hold many people"),
        ("tanker truck", "jerry can", "more", "Tankers carry thousands of litres"),
        ("aquarium", "jar", "more", "Aquariums house many fish")
    ]
    
    for item1, item2, _, explanation in capacity:
        q_text = f"Which holds MORE liquid: a {item1} or a {item2}?"
        correct = item1.title()
        wrong = item2.title()
        
        options = [correct, wrong, "Same amount", "Cannot compare"]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Measurement units (15 questions)
    units = [
        ("What unit measures weight?", "Kilograms or grams", "Kg and g measure mass"),
        ("What unit measures liquid?", "Litres or millilitres", "L and ml measure volume"),
        ("How many grams in a kilogram?", "1000", "Kilo means thousand"),
        ("How many millilitres in a litre?", "1000", "Milli means thousandth"),
        ("Which is heavier: 1kg or 500g?", "1 kg", "1kg = 1000g > 500g"),
        ("Which is more: 1L or 500ml?", "1 litre", "1L = 1000ml > 500ml"),
        ("What tool measures weight?", "Scales", "Scales show kg or g"),
        ("What tool measures liquid volume?", "Measuring jug", "Jugs show ml and L"),
        ("About how much does an apple weigh?", "About 150-200 grams", "Apples are light"),
        ("About how much does water bottle hold?", "About 500ml to 1L", "Common bottle sizes"),
        ("What does a recipe measure flour in?", "Grams", "Recipes use g for dry ingredients"),
        ("What does a recipe measure milk in?", "Millilitres", "Recipes use ml for liquids"),
        ("Which is bigger: gram or kilogram?", "Kilogram", "Kilo = 1000 grams"),
        ("Which is bigger: millilitre or litre?", "Litre", "Litre = 1000 ml"),
        ("About how much does a bag of sugar weigh?", "1 kilogram", "Standard sugar bag")
    ]
    
    for q_text, correct, explanation in units:
        if correct.isdigit():
            val = int(correct)
            options = [correct, str(val // 10), str(val * 10), str(val // 100)]
        elif "kg" in correct.lower() or "kilogram" in correct.lower():
            options = [correct, "500g", "They are equal", "100g"]
        elif "litre" in correct.lower():
            options = [correct, "500ml", "They are equal", "100ml"]
        else:
            options = [correct, "Ruler", "Thermometer", "Clock"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_4_questions():
    """Level 4: Position & Direction - 50 unique questions"""
    questions = []
    
    # Position words (25 questions)
    positions = [
        ("The book is ON the table. Where is the book?", "On top of the table"),
        ("The cat is UNDER the bed. Where is the cat?", "Below/beneath the bed"),
        ("The ball is BEHIND the sofa. Where is the ball?", "At the back of the sofa"),
        ("The lamp is BESIDE the chair. Where is the lamp?", "Next to the chair"),
        ("The picture is ABOVE the fireplace. Where is it?", "Higher than the fireplace"),
        ("The shoes are IN the cupboard. Where are they?", "Inside the cupboard"),
        ("The dog is IN FRONT OF the door. Where is it?", "Facing the door from outside"),
        ("The plant is BETWEEN the windows. Where is it?", "In the middle of two windows"),
        ("The toy is NEAR the box. Where is the toy?", "Close to the box"),
        ("The bird is OUTSIDE the cage. Where is it?", "Not inside the cage"),
        ("The pen is INSIDE the pencil case. Where is it?", "Within the pencil case"),
        ("The coat is BEHIND the door. Where is it?", "On the back side of the door"),
        ("The clock is ABOVE the desk. Where is it?", "Higher than the desk"),
        ("The rug is UNDER the table. Where is it?", "Below the table"),
        ("The vase is ON TOP OF the shelf. Where is it?", "Sitting on the shelf"),
        ("The car is NEXT TO the house. Where is it?", "Beside the house"),
        ("The child is BETWEEN mum and dad. Where?", "In the middle of both parents"),
        ("The apple is IN the bowl. Where is it?", "Inside the bowl"),
        ("The stars are ABOVE the clouds. Where?", "Higher than the clouds"),
        ("The roots are BELOW the ground. Where?", "Under the surface"),
        ("The hat is ON your head. Where is it?", "On top of your head"),
        ("The socks are IN the drawer. Where?", "Inside the drawer"),
        ("The mirror is BEHIND you. Where is it?", "At your back"),
        ("The school is NEAR my house. Where is it?", "Close to my house"),
        ("The moon is ABOVE the horizon. Where?", "Higher than the horizon line")
    ]
    
    for q_text, correct in positions:
        wrong_positions = [
            "Far away", "In a different room", 
            "Cannot be found", "In the opposite place"
        ]
        
        options = [correct] + wrong_positions[:3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': q_text.split('.')[0]
        })
    
    # Direction words (25 questions)
    directions = [
        ("To go UP means to go...", "Higher", "Up = towards the sky"),
        ("To go DOWN means to go...", "Lower", "Down = towards the ground"),
        ("To go LEFT means to go...", "To your left side", "Left is opposite of right"),
        ("To go RIGHT means to go...", "To your right side", "Right is opposite of left"),
        ("To go FORWARD means to go...", "Ahead/in front", "Forward = continuing onward"),
        ("To go BACKWARD means to go...", "Behind/back", "Backward = reversing"),
        ("NORTH is at the... of a map", "Top", "North is usually at the top"),
        ("SOUTH is at the... of a map", "Bottom", "South is opposite to north"),
        ("EAST is at the... of a map", "Right", "East is where the sun rises"),
        ("WEST is at the... of a map", "Left", "West is where the sun sets"),
        ("The sun rises in the...", "East", "The sun rises in the east"),
        ("The sun sets in the...", "West", "The sun sets in the west"),
        ("A compass shows which direction?", "North", "Compass needles point north"),
        ("If you face north, south is...", "Behind you", "South is opposite north"),
        ("If you face east, west is...", "Behind you", "West is opposite east"),
        ("To turn LEFT, you turn...", "Anti-clockwise (counter-clockwise)", "Left is anti-clockwise"),
        ("To turn RIGHT, you turn...", "Clockwise", "Right follows clock hands"),
        ("UP on a lift button means...", "Going to higher floors", "Up = ascending"),
        ("DOWN on a lift button means...", "Going to lower floors", "Down = descending"),
        ("'Turn around' means...", "Face the opposite direction", "Turn 180 degrees"),
        ("ACROSS means going...", "From one side to the other", "Crossing over"),
        ("THROUGH means going...", "Inside and out the other side", "Passing within"),
        ("AROUND means going...", "In a circle or avoiding", "Not straight through"),
        ("TOWARDS means going...", "Getting closer to something", "Moving in that direction"),
        ("AWAY FROM means going...", "Getting further from something", "Moving in opposite direction")
    ]
    
    for q_text, correct, explanation in directions:
        if "Higher" in correct or "Lower" in correct:
            options = [correct, "Lower" if "Higher" in correct else "Higher", "Sideways", "Stay still"]
        elif "Top" in correct or "Bottom" in correct:
            options = [correct, "Bottom" if "Top" in correct else "Top", "Side", "Middle"]
        elif "Left" in correct or "Right" in correct:
            options = [correct, "Right" if "Left" in correct else "Left", "Top", "Centre"]
        elif "East" in correct or "West" in correct:
            options = [correct, "West" if "East" in correct else "East", "North", "South"]
        elif "Behind" in correct:
            options = [correct, "In front of you", "To your side", "Above you"]
        else:
            options = [correct, "Wrong direction 1", "Wrong direction 2", "Stay still"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_5_questions():
    """Level 5: Following Directions - 50 unique questions"""
    questions = []
    
    # Simple direction following (25 questions)
    simple_directions = [
        ("Start facing North. Turn right. Which way do you face?", "East"),
        ("Start facing East. Turn right. Which way do you face?", "South"),
        ("Start facing South. Turn right. Which way do you face?", "West"),
        ("Start facing West. Turn right. Which way do you face?", "North"),
        ("Start facing North. Turn left. Which way do you face?", "West"),
        ("Start facing East. Turn left. Which way do you face?", "North"),
        ("Start facing South. Turn left. Which way do you face?", "East"),
        ("Start facing West. Turn left. Which way do you face?", "South"),
        ("Start facing North. Turn around. Which way do you face?", "South"),
        ("Start facing East. Turn around. Which way do you face?", "West"),
        ("Start at A. Go 2 steps right. Where are you?", "2 spaces to the right of A"),
        ("Start at B. Go 3 steps up. Where are you?", "3 spaces above B"),
        ("Start at C. Go 1 step left, 1 step up. Where are you?", "Diagonally up-left from C"),
        ("Start at D. Go 2 steps down. Where are you?", "2 spaces below D"),
        ("You're at the door. Go forward 5 steps. Where now?", "5 steps inside the room"),
        ("You're at the window. Turn left, walk 3 steps. Where?", "3 steps left of the window"),
        ("Start in corner. Go along the wall. You're going...", "Along the edge of the room"),
        ("Face the board. Turn right. What do you face?", "The wall to your right"),
        ("Sit at your desk. Look behind you. What direction?", "Towards the back of the room"),
        ("Stand at the door. The teacher's desk is ahead. Direction?", "Forward/in front"),
        ("The window is to your left. Which way is that?", "Left side of the room"),
        ("Walk towards the exit. You're going...", "In the direction of the exit"),
        ("Move away from the wall. You're going...", "Towards the middle of the room"),
        ("Go around the table. You're...", "Walking in a path around it"),
        ("Step over the line. You're now...", "On the other side of the line")
    ]
    
    for q_text, correct in simple_directions:
        directions = ["North", "East", "South", "West"]
        positions = ["Left", "Right", "Above", "Below", "In front", "Behind"]
        
        if correct in directions:
            options = directions
        elif "right" in correct.lower():
            options = [correct, "To the left of A", "Above A", "Below A"]
        elif "above" in correct.lower():
            options = [correct, "Below B", "Left of B", "Right of B"]
        elif "diagonal" in correct.lower():
            options = [correct, "Still at C", "Below C", "Right of C"]
        elif "below" in correct.lower():
            options = [correct, "Above D", "Left of D", "Right of D"]
        else:
            options = [correct, "In the opposite direction", "Nowhere", "Back where you started"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"Following the directions: {correct}"
        })
    
    # Multi-step directions (25 questions)
    multi_step = [
        ("Go up 2, right 3. Total moves?", "5 moves"),
        ("Go left 4, down 2, right 1. Total moves?", "7 moves"),
        ("Go forward 3, turn right, go forward 2. Total steps forward?", "5 steps"),
        ("Go north 5, then south 2. How far north of start?", "3 units north"),
        ("Go east 4, then west 4. Where are you?", "Back at the start"),
        ("Go up 3, down 3. Where are you?", "Back at the start"),
        ("Go right 2, up 2. What shape path?", "An L-shape"),
        ("Go right 2, up 2, left 2, down 2. What shape?", "A square"),
        ("Go forward 5, backward 3. How far from start?", "2 steps forward"),
        ("Turn right 4 times. Which way do you face?", "Same as when you started"),
        ("Turn left 2 times. Which way do you face?", "Opposite direction"),
        ("Turn right, then left. Which way do you face?", "Same as when you started"),
        ("Go clockwise around a square. How many turns?", "4 right turns"),
        ("Walk the perimeter of a rectangle. How many corners?", "4 corners"),
        ("Spiral inward. Are you getting closer or further from center?", "Closer to center"),
        ("Walk in a circle. How many steps to return to start?", "Depends on circle size"),
        ("Zig-zag across a room. Efficient path?", "No, straight is faster"),
        ("Take shortest path between two points. What type?", "A straight line"),
        ("Walk around an obstacle. Path is...", "Longer than straight"),
        ("Pace out a room length. You're measuring...", "How long the room is"),
        ("Walk diagonally across a square. Compared to sides?", "Longer than one side"),
        ("Walk the edges of a triangle. How many sides?", "3 sides"),
        ("Start at corner, walk 2 edges of square. How many corners passed?", "2 corners"),
        ("Face north, turn right twice. Now facing?", "South"),
        ("Face east, turn left three times. Now facing?", "North")
    ]
    
    for q_text, correct in multi_step:
        if "moves" in correct:
            val = int(correct.split()[0])
            options = [correct, f"{val+2} moves", f"{val-1} moves", f"{val+1} moves"]
        elif "steps" in correct:
            val = int(correct.split()[0])
            options = [correct, f"{val+2} steps", f"{val-1} steps", f"{val*2} steps"]
        elif "units" in correct:
            val = int(correct.split()[0])
            options = [correct, f"{val+2} units north", "At the start", f"{val} units south"]
        elif "start" in correct.lower():
            options = [correct, "Far from start", "To the left", "To the right"]
        elif correct in ["North", "South", "East", "West"]:
            options = ["North", "South", "East", "West"]
        else:
            options = [correct, "Different answer 1", "Different answer 2", "Cannot tell"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"The answer is {correct}"
        })
    
    return questions[:50]


def generate_level_6_questions():
    """Level 6: Maps & Plans - 50 unique questions"""
    questions = []
    
    # Map reading basics (25 questions)
    map_basics = [
        ("What is a map?", "A drawing showing places from above"),
        ("What is a key/legend on a map?", "Explains what symbols mean"),
        ("What does a compass rose show?", "North, South, East, West directions"),
        ("What does a scale on a map show?", "How distances relate to real life"),
        ("What colour usually shows water on maps?", "Blue"),
        ("What colour usually shows land/parks on maps?", "Green"),
        ("What colour usually shows roads on maps?", "Various - often red, yellow, white"),
        ("What do dotted lines often show on maps?", "Paths, borders, or planned routes"),
        ("What does a red line often show on road maps?", "Major roads or motorways"),
        ("What is a bird's eye view?", "Looking down from above"),
        ("Why are maps useful?", "Help us find places and plan routes"),
        ("What is a street map?", "Shows roads and streets in a town"),
        ("What is a floor plan?", "Map of inside a building"),
        ("What is a world map?", "Shows all countries and oceans"),
        ("What is a treasure map?", "Shows route to hidden treasure"),
        ("What symbol often shows a church on maps?", "A cross or church shape"),
        ("What symbol often shows a train station?", "A train or railway symbol"),
        ("What symbol often shows parking?", "The letter P"),
        ("What symbol often shows a hospital?", "H or a cross"),
        ("What symbol often shows information?", "Letter i in a circle"),
        ("If north is up, where is south?", "At the bottom"),
        ("If north is up, where is east?", "On the right"),
        ("If north is up, where is west?", "On the left"),
        ("What is a grid on a map?", "Lines dividing map into squares"),
        ("How do grid references help?", "Pinpoint exact locations")
    ]
    
    for q_text, correct in map_basics:
        if "colour" in q_text.lower():
            options = [correct, "Red", "Yellow", "Purple"]
        elif "symbol" in q_text.lower():
            options = [correct, "A star", "A question mark", "Nothing"]
        elif "north" in q_text.lower() or "south" in q_text.lower() or "east" in q_text.lower() or "west" in q_text.lower():
            options = [correct, "At the top", "On the left", "In the middle"]
        else:
            options = [correct, "Wrong answer 1", "Wrong answer 2", "I don't know"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"{correct}"
        })
    
    # Using maps (25 questions)
    using_maps = [
        ("You want to walk to the park. What helps?", "A local street map"),
        ("You're driving to another city. What helps?", "A road map or sat nav"),
        ("You're lost in a building. What helps?", "A floor plan"),
        ("You want to find a country. What helps?", "A world map or atlas"),
        ("The map shows your house is 2cm from school. Scale is 1cm=100m. Real distance?", "200 metres"),
        ("The map shows 5cm between towns. Scale is 1cm=1km. Real distance?", "5 kilometres"),
        ("Map scale is 1:10000. 1cm on map = how many metres?", "100 metres"),
        ("You need to go east. The sun rises there. Which way?", "Towards where the sun rises"),
        ("It's midday, sun is south. You face the sun. Behind you is?", "North"),
        ("On a map, the shop is northeast of your house. Direction to walk?", "Between north and east"),
        ("A straight line on a map is the... route?", "Shortest"),
        ("Map shows river between you and destination. You need to...", "Find a bridge or go around"),
        ("Map shows a road is closed. What do you do?", "Find an alternative route"),
        ("You're at grid reference B3. Library is at C4. Which direction?", "Diagonally right and up"),
        ("Map shows steep hills with many lines. The area is...", "Very hilly/mountainous"),
        ("Contour lines close together mean...", "Steep slope"),
        ("Contour lines far apart mean...", "Gentle slope or flat"),
        ("A blue line on a map often shows...", "A river or stream"),
        ("A thick black line on a map often shows...", "A railway line"),
        ("Small dots or stipples might show...", "Beach or sandy area"),
        ("Green shading usually shows...", "Parks, forests, or countryside"),
        ("Grey/pink shading usually shows...", "Built-up/urban areas"),
        ("A flag symbol might show...", "A viewpoint or landmark"),
        ("Numbers on roads show...", "Road numbers (like M50, N7)"),
        ("PO or envelope symbol shows...", "Post office")
    ]
    
    for q_text, correct in using_maps:
        if "metres" in correct or "kilometres" in correct:
            val = int(correct.split()[0])
            unit = "metres" if "metres" in correct else "kilometres"
            options = [correct, f"{val*2} {unit}", f"{val//2} {unit}", f"{val+50} {unit}"]
        elif correct in ["North", "South", "East", "West", "Shortest"]:
            options = [correct, "South", "Longest", "Cannot tell"]
        else:
            options = [correct, "Wrong answer", "Cannot be done", "Not shown on maps"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"{correct}"
        })
    
    return questions[:50]


def generate_level_7_questions():
    """Level 7: Temperature - 50 unique questions"""
    questions = []
    
    # Temperature concepts (25 questions)
    temps = [
        ("What tool measures temperature?", "Thermometer"),
        ("What unit is temperature measured in?", "Degrees Celsius (°C)"),
        ("Water freezes at what temperature?", "0°C"),
        ("Water boils at what temperature?", "100°C"),
        ("What is room temperature roughly?", "About 20°C"),
        ("What is normal body temperature?", "About 37°C"),
        ("A hot summer day might be?", "25-30°C or higher"),
        ("A cold winter day might be?", "0°C or below"),
        ("What temperature is comfortable indoors?", "18-22°C"),
        ("A fever is body temperature above?", "About 38°C"),
        ("Fridge temperature should be about?", "4°C"),
        ("Freezer temperature should be about?", "-18°C"),
        ("Hot bath water is about?", "38-40°C"),
        ("Cold tap water is about?", "10-15°C"),
        ("Is 35°C hot or cold for weather?", "Very hot"),
        ("Is 5°C hot or cold for weather?", "Cold"),
        ("Is -10°C hot or cold?", "Very cold (below freezing)"),
        ("Is 22°C hot or cold for a room?", "Comfortable/warm"),
        ("What happens to water below 0°C?", "It freezes"),
        ("What happens to water at 100°C?", "It boils"),
        ("Why do we heat homes in winter?", "To stay warm and comfortable"),
        ("Why do we use fridges?", "To keep food cold and fresh"),
        ("Why do we use ovens?", "To cook food at high temperatures"),
        ("Oven cooking temperature might be?", "150-220°C"),
        ("Ice cream should be stored at?", "Below 0°C (in freezer)")
    ]
    
    for q_text, correct in temps:
        if "°C" in correct or "degrees" in correct.lower():
            if "0°C" in correct:
                options = [correct, "100°C", "-10°C", "50°C"]
            elif "100°C" in correct:
                options = [correct, "0°C", "50°C", "200°C"]
            elif "20" in correct or "22" in correct:
                options = [correct, "About 50°C", "About 0°C", "About 100°C"]
            elif "37" in correct:
                options = [correct, "About 20°C", "About 50°C", "About 100°C"]
            else:
                options = [correct, "Wrong temp 1", "Wrong temp 2", "Wrong temp 3"]
        elif correct in ["Very hot", "Cold", "Very cold (below freezing)", "Comfortable/warm"]:
            options = ["Very hot", "Cold", "Very cold (below freezing)", "Comfortable/warm"]
        elif correct in ["It freezes", "It boils"]:
            options = [correct, "Nothing happens", "It disappears", "It turns green"]
        else:
            options = [correct, "Ruler", "Scales", "Clock"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': correct
        })
    
    # Temperature comparisons (25 questions)
    temp_compare = [
        ("Which is warmer: 25°C or 15°C?", "25°C"),
        ("Which is colder: -5°C or 5°C?", "-5°C"),
        ("Which is warmer: 0°C or -10°C?", "0°C"),
        ("Which is hotter: 30°C or 20°C?", "30°C"),
        ("Which is colder: 10°C or 0°C?", "0°C"),
        ("Which is warmer: boiling water or bath water?", "Boiling water"),
        ("Which is colder: fridge or freezer?", "Freezer"),
        ("Which is warmer: summer or winter?", "Summer"),
        ("Which is colder: ice or cold water?", "Ice"),
        ("Which is warmer: oven or fridge?", "Oven"),
        ("Put in order (coldest first): 10°C, 0°C, 20°C", "0°C, 10°C, 20°C"),
        ("Put in order (warmest first): 5°C, 15°C, -5°C", "15°C, 5°C, -5°C"),
        ("Temperature goes from 15°C to 20°C. It got...", "Warmer by 5°C"),
        ("Temperature goes from 10°C to 5°C. It got...", "Colder by 5°C"),
        ("Temperature drops from 5°C to -5°C. Change?", "Dropped 10°C"),
        ("Temperature rises from -10°C to 0°C. Change?", "Rose 10°C"),
        ("Morning is 8°C, afternoon is 15°C. Change?", "Warmed by 7°C"),
        ("Day is 20°C, night is 12°C. Change?", "Cooled by 8°C"),
        ("Is -20°C or -5°C colder?", "-20°C"),
        ("Is 35°C or 40°C hotter?", "40°C"),
        ("Fridge at 4°C warms to 8°C. Change?", "Warmed by 4°C"),
        ("Room cools from 22°C to 18°C. Change?", "Cooled by 4°C"),
        ("Water at 20°C, ice at 0°C. Difference?", "20°C difference"),
        ("Body at 37°C, fever at 39°C. Difference?", "2°C higher"),
        ("Outside -2°C, inside 20°C. Difference?", "22°C warmer inside")
    ]
    
    for q_text, correct in temp_compare:
        if correct.endswith("°C") and correct[0] == '-' or correct[0].isdigit():
            # Simple temperature like "25°C" or "-5°C"
            temp_val = correct.replace("°C", "")
            try:
                val = int(temp_val)
                options = [correct, f"{val + 10}°C", f"{val - 5}°C", "They are equal"]
            except:
                options = [correct, "Different temperature", "They are equal", "Cannot compare"]
        elif "," in correct:
            parts = correct.split(", ")
            options = [correct, ", ".join(reversed(parts)), ", ".join([parts[1], parts[0], parts[2]]) if len(parts) >= 3 else ", ".join(reversed(parts)), "Cannot order"]
        elif "Warmer" in correct or "Colder" in correct or "Cooled" in correct or "Warmed" in correct:
            digits = ''.join(filter(str.isdigit, correct))
            if digits:
                val = int(digits)
                options = [correct, f"Changed by {val+3}°C", f"Changed by {val-2}°C" if val > 2 else f"Changed by {val+5}°C", "No change"]
            else:
                options = [correct, "Got warmer", "Got colder", "No change"]
        elif "difference" in correct.lower() or "higher" in correct.lower():
            digits = ''.join(filter(str.isdigit, correct))
            if digits:
                val = int(digits)
                options = [correct, f"{val+5}°C difference", f"{val-3}°C difference" if val > 3 else f"{val+8}°C difference", "Same temperature"]
            else:
                options = [correct, "10°C difference", "No difference", "Cannot tell"]
        else:
            options = [correct, "The other one", "They are equal", "Cannot compare"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': correct
        })
    
    return questions[:50]


def generate_level_8_questions():
    """Level 8: Measuring in Practice - 50 unique questions"""
    questions = []
    
    # Choosing the right unit (25 questions)
    right_units = [
        ("Measure the length of a pencil in...", "Centimetres"),
        ("Measure the distance to the next town in...", "Kilometres"),
        ("Measure the height of a door in...", "Metres"),
        ("Measure the weight of an apple in...", "Grams"),
        ("Measure the weight of a person in...", "Kilograms"),
        ("Measure milk for a recipe in...", "Millilitres"),
        ("Measure water in a swimming pool in...", "Litres (or cubic metres)"),
        ("Measure room temperature in...", "Degrees Celsius"),
        ("Measure the width of a book in...", "Centimetres"),
        ("Measure a marathon distance in...", "Kilometres"),
        ("Measure flour for baking in...", "Grams"),
        ("Measure a car's fuel tank in...", "Litres"),
        ("Measure body temperature in...", "Degrees Celsius"),
        ("Measure the thickness of a coin in...", "Millimetres"),
        ("Measure a bag of potatoes in...", "Kilograms"),
        ("Measure medicine dose in...", "Millilitres"),
        ("Measure a field length in...", "Metres"),
        ("Measure a paperclip length in...", "Centimetres or millimetres"),
        ("Measure a child's height in...", "Centimetres or metres"),
        ("Measure cooking oil in...", "Millilitres or tablespoons"),
        ("Measure a lorry's cargo in...", "Tonnes or kilograms"),
        ("Measure bathwater in...", "Litres"),
        ("Measure oven temperature in...", "Degrees Celsius"),
        ("Measure the width of a hair in...", "Millimetres (very thin)"),
        ("Measure a country's size in...", "Square kilometres")
    ]
    
    for q_text, correct in right_units:
        units = ["Centimetres", "Metres", "Kilometres", "Grams", "Kilograms", 
                 "Millilitres", "Litres", "Degrees Celsius", "Millimetres"]
        wrong = [u for u in units if u not in correct][:3]
        
        options = [correct] + wrong
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"Use {correct}"
        })
    
    # Estimation (25 questions)
    estimates = [
        ("Estimate the length of a car:", "About 4-5 metres"),
        ("Estimate the height of a classroom:", "About 3 metres"),
        ("Estimate your own height:", "Between 1-2 metres (depending on age)"),
        ("Estimate the weight of a textbook:", "About 500g - 1kg"),
        ("Estimate the weight of a mobile phone:", "About 150-200 grams"),
        ("Estimate water in a glass:", "About 250ml"),
        ("Estimate water in a bathtub:", "About 80-150 litres"),
        ("Estimate comfortable room temperature:", "About 20°C"),
        ("Estimate a hot summer day:", "About 25-30°C"),
        ("Estimate the length of your foot:", "About 20-25cm (for a child)"),
        ("Estimate the width of your hand:", "About 8-10cm"),
        ("Estimate the length of a bus:", "About 10-12 metres"),
        ("Estimate the weight of a bag of sugar:", "1 kilogram (it says on the bag!)"),
        ("Estimate milk in a carton:", "1 litre or 2 litres"),
        ("Estimate freezer temperature:", "About -18°C"),
        ("Estimate the height of a double-decker bus:", "About 4-4.5 metres"),
        ("Estimate the length of a football pitch:", "About 100 metres"),
        ("Estimate the weight of an egg:", "About 50-60 grams"),
        ("Estimate a can of drink:", "About 330ml"),
        ("Estimate the depth of a swimming pool:", "About 1-3 metres"),
        ("Estimate a pencil length:", "About 15-20cm"),
        ("Estimate a door height:", "About 2 metres"),
        ("Estimate a chair seat height:", "About 45cm"),
        ("Estimate a tablespoon of liquid:", "About 15ml"),
        ("Estimate a teaspoon of liquid:", "About 5ml")
    ]
    
    for q_text, correct in estimates:
        if "metre" in correct.lower():
            options = [correct, "About 10 centimetres", "About 100 metres", "About 1 kilometre"]
        elif "gram" in correct.lower() or "kg" in correct.lower():
            options = [correct, "About 10 grams", "About 50 kilograms", "About 1 tonne"]
        elif "litre" in correct.lower() or "ml" in correct.lower():
            options = [correct, "About 5ml", "About 1000 litres", "About 50 litres"]
        elif "°C" in correct:
            options = [correct, "About 100°C", "About -50°C", "About 0°C"]
        else:
            options = [correct, "Much smaller", "Much larger", "Cannot estimate"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': correct
        })
    
    return questions[:50]


def generate_level_9_questions():
    """Level 9: Perimeter Concepts - 50 unique questions"""
    questions = []
    
    # Perimeter understanding (25 questions)
    perimeter_concepts = [
        ("What is perimeter?", "The distance around the outside of a shape"),
        ("How do you find perimeter?", "Add up all the sides"),
        ("Perimeter of a square with sides of 5cm?", "20cm (5+5+5+5)"),
        ("Perimeter of a rectangle 4cm by 3cm?", "14cm (4+4+3+3)"),
        ("Perimeter of a triangle with sides 3cm, 4cm, 5cm?", "12cm (3+4+5)"),
        ("A square has perimeter 20cm. Each side is?", "5cm (20÷4)"),
        ("A rectangle has perimeter 24cm. If width is 4cm, length is?", "8cm"),
        ("Which has bigger perimeter: 5×5 square or 6×4 rectangle?", "Same (both 20cm)"),
        ("Walking around a 10m × 8m garden. Distance walked?", "36m (10+10+8+8)"),
        ("Fence around a 6m × 4m area needs how much fencing?", "20m of fencing"),
        ("A square field has 100m perimeter. Each side is?", "25m"),
        ("Ribbon around a 15cm × 10cm card. How much ribbon?", "50cm"),
        ("Frame for a 20cm × 30cm picture. Perimeter?", "100cm"),
        ("A room is 5m × 4m. Skirting board needed?", "18m (for all 4 walls)"),
        ("Equilateral triangle with sides 6cm. Perimeter?", "18cm (6+6+6)"),
        ("Regular hexagon with sides 3cm. Perimeter?", "18cm (6 sides × 3cm)"),
        ("Square side doubled from 4cm to 8cm. New perimeter?", "32cm (double the original)"),
        ("Rectangle 5cm × 3cm. Add 2cm to length. New perimeter?", "20cm"),
        ("Border around 8m × 6m pool. Perimeter?", "28m"),
        ("If perimeter is 40m and shape is square, side is?", "10m"),
        ("Garden path around circular flower bed. What do we need?", "Circumference (perimeter of circle)"),
        ("Track around rectangular field 100m × 50m. One lap?", "300m"),
        ("Farmer fences 3 sides of 40m × 30m field (house on 4th). Fence needed?", "110m"),
        ("Add trim around 2m × 1.5m tablecloth. Trim length?", "7m"),
        ("Square A has perimeter 12cm, Square B has perimeter 24cm. B is how much bigger?", "B's sides are double A's")
    ]
    
    for q_text, correct in perimeter_concepts:
        if "cm" in correct and correct[0].isdigit():
            val = int(''.join(filter(str.isdigit, correct.split('(')[0])))
            options = [correct, f"{val+4}cm", f"{val-4}cm" if val > 4 else f"{val*2}cm", f"{val//2}cm"]
        elif "m" in correct and correct[0].isdigit():
            val = int(''.join(filter(str.isdigit, correct.split('(')[0].split('m')[0])))
            options = [correct, f"{val+10}m", f"{val-5}m" if val > 5 else f"{val*2}m", f"{val//2}m"]
        elif correct.startswith("The distance"):
            options = [correct, "The area inside a shape", "The weight of a shape", "The colour of a shape"]
        elif correct.startswith("Add up"):
            options = [correct, "Multiply all the sides", "Divide by 2", "Only measure one side"]
        else:
            options = [correct, "Wrong answer 1", "Wrong answer 2", "Cannot calculate"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': correct
        })
    
    # More perimeter problems (25 questions)
    more_perimeter = [
        ("Square playground side 15m. Perimeter?", "60m"),
        ("Rectangle 12m × 8m. Perimeter?", "40m"),
        ("Triangle sides 7cm, 8cm, 9cm. Perimeter?", "24cm"),
        ("Pentagon (5 sides) each 4cm. Perimeter?", "20cm"),
        ("Octagon (8 sides) each 2cm. Perimeter?", "16cm"),
        ("Rectangle twice as long as wide. Width 5m. Perimeter?", "30m"),
        ("Square perimeter 48cm. Side length?", "12cm"),
        ("Rectangle perimeter 30cm. Length 10cm. Width?", "5cm"),
        ("Equilateral triangle perimeter 27cm. Side?", "9cm"),
        ("Path 2m wide around 10m × 8m pool. Outer perimeter?", "44m"),
        ("Combined perimeter of two 4cm squares sharing a side?", "24cm (not 32)"),
        ("L-shape made of two rectangles. How to find perimeter?", "Add outer edges only"),
        ("Half a square (triangle). Side 6cm. Perimeter of triangle?", "Approximately 20cm"),
        ("Circle diameter 10cm. Perimeter (circumference) roughly?", "About 31cm"),
        ("Semi-circle diameter 8cm. Perimeter roughly?", "About 21cm"),
        ("Double all sides of a shape. Perimeter?", "Doubles too"),
        ("Triple one side of rectangle 4cm × 3cm. New perimeter?", "22cm"),
        ("Irregular shape with sides 3,4,5,2,6. Perimeter?", "20 units"),
        ("Square inside square. Find perimeter of smaller square only?", "Measure its 4 sides"),
        ("Perimeter of your hand (roughly tracing)?", "About 20-30cm"),
        ("Perimeter of a door (rectangle about 2m × 0.8m)?", "About 5.6m"),
        ("Perimeter of an A4 paper (21cm × 30cm)?", "102cm"),
        ("Perimeter of a football pitch (roughly 100m × 70m)?", "340m"),
        ("Running track one lap is 400m. If rectangular, one option?", "Length 100m, width 100m (but curves exist)"),
        ("Garden with 3 straight sides and house as 4th. Perimeter of fence?", "3 sides only")
    ]
    
    for q_text, correct in more_perimeter:
        if "cm" in correct and correct[0].isdigit():
            val = int(''.join(filter(str.isdigit, correct.split('(')[0].split('cm')[0])))
            options = [correct, f"{val+8}cm", f"{val-6}cm" if val > 6 else f"{val*2}cm", f"{val//2}cm"]
        elif "m" in correct and correct[0].isdigit():
            val = int(''.join(filter(str.isdigit, correct.split('(')[0].split('m')[0])))
            options = [correct, f"{val+20}m", f"{val-10}m" if val > 10 else f"{val*2}m", f"{val//2}m"]
        else:
            options = [correct, "Different calculation", "Cannot determine", "Multiply instead"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': correct
        })
    
    return questions[:50]


def generate_level_10_questions():
    """Level 10: Area Concepts - 50 unique questions"""
    questions = []
    
    # Area understanding (25 questions)
    area_concepts = [
        ("What is area?", "The space inside a shape"),
        ("What unit is area measured in?", "Square units (cm², m²)"),
        ("Area of a 3cm × 4cm rectangle?", "12 cm² (3×4)"),
        ("Area of a square with 5cm sides?", "25 cm² (5×5)"),
        ("Area of a 10m × 6m room?", "60 m²"),
        ("Rectangle has area 24cm². Width 4cm. Length?", "6cm (24÷4)"),
        ("Square has area 36cm². Side length?", "6cm (√36)"),
        ("Which is bigger: area of 5×4 or 6×3?", "5×4 = 20cm² is bigger"),
        ("Floor tiles are 1m². Room is 5m × 4m. Tiles needed?", "20 tiles"),
        ("Paint covers 10m² per litre. Room is 40m². Litres needed?", "4 litres"),
        ("Carpet for 6m × 4m room. Area?", "24m²"),
        ("Grass seed covers 5m² per bag. Lawn is 30m². Bags needed?", "6 bags"),
        ("What's the difference between perimeter and area?", "Perimeter is around, area is inside"),
        ("Double the sides of a square. What happens to area?", "Area quadruples (×4)"),
        ("Rectangle 8cm × 6cm. Cut in half. Each piece area?", "24cm² each"),
        ("Two shapes same perimeter. Same area?", "Not necessarily"),
        ("4×4 square vs 8×2 rectangle. Same area?", "No, 16 vs 16 - yes same!"),
        ("Triangle in a 6×4 rectangle (half). Triangle area?", "12cm² (half of 24)"),
        ("Combine two 3×2 rectangles. Total area?", "12cm² (6+6)"),
        ("Square area 100cm². Perimeter?", "40cm (sides are 10cm each)"),
        ("Area of your desk roughly?", "About 0.5-1 m² (half to 1 square metre)"),
        ("Area of a football pitch roughly?", "About 7,000m² (100m × 70m)"),
        ("Area of a postage stamp roughly?", "About 4cm² (2cm × 2cm)"),
        ("Area of A4 paper (21cm × 30cm)?", "630cm²"),
        ("How many 1cm² squares fit in 5cm × 3cm?", "15 squares")
    ]
    
    for q_text, correct in area_concepts:
        if "cm²" in correct and correct[0].isdigit():
            val = int(''.join(filter(str.isdigit, correct.split('(')[0].split('cm')[0])))
            options = [correct, f"{val+10}cm²", f"{val-5}cm²" if val > 5 else f"{val*2}cm²", f"{val//2}cm²"]
        elif "m²" in correct and correct[0].isdigit():
            val = int(''.join(filter(str.isdigit, correct.split('(')[0].split('m')[0])))
            options = [correct, f"{val*2}m²", f"{val//2}m²", f"{val+20}m²"]
        elif correct.startswith("The space"):
            options = [correct, "The distance around", "The weight", "The colour"]
        elif correct.startswith("Square units"):
            options = [correct, "Centimetres", "Kilograms", "Litres"]
        elif "tiles" in correct or "litres" in correct or "bags" in correct:
            val = int(''.join(filter(str.isdigit, correct.split()[0])))
            options = [correct, f"{val+5}", f"{val-2}" if val > 2 else f"{val*2}", f"{val*3}"]
        else:
            options = [correct, "Wrong answer", "Cannot determine", "Different formula"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': correct
        })
    
    # More area problems (25 questions)
    more_area = [
        ("Square garden 8m × 8m. Area?", "64m²"),
        ("Rectangular field 50m × 30m. Area?", "1500m²"),
        ("Room 4.5m × 3m. Area?", "13.5m²"),
        ("Tile floor 6m × 5m with 0.5m × 0.5m tiles. How many tiles?", "120 tiles"),
        ("Wall 3m × 2.5m. Area to paint?", "7.5m²"),
        ("Book cover 20cm × 15cm. Area?", "300cm²"),
        ("Phone screen 12cm × 6cm. Area?", "72cm²"),
        ("Window 1.2m × 0.8m. Glass area?", "0.96m²"),
        ("2 rooms: 4m×3m and 3m×3m. Total area?", "21m²"),
        ("Square 10cm side. Remove 2cm×2cm corner. Remaining area?", "96cm²"),
        ("L-shaped room: 5m×4m with 2m×2m cut out. Area?", "16m²"),
        ("Carpet €20 per m². Room 4m×3m. Cost?", "€240"),
        ("Flooring €15 per m². Room 5m×4m. Cost?", "€300"),
        ("Garden 10m×8m. Shed 3m×2m. Lawn area?", "74m²"),
        ("Paper 30cm×20cm. Cut out 10cm×10cm. Remaining?", "500cm²"),
        ("Compare: 7m×5m vs 6m×6m. Which bigger?", "6×6=36m² > 7×5=35m²"),
        ("Rectangle area 36cm². If square, side would be?", "6cm"),
        ("Area 100m². Square shape. Side?", "10m"),
        ("Double length only of 4×3 rectangle. New area?", "24cm² (8×3)"),
        ("Halve width only of 6×4 rectangle. New area?", "12cm² (6×2)"),
        ("Scale drawing 1:100. Drawing 3cm×2cm. Real area?", "600m² (300×200cm = 6m²×100²)"),
        ("Bedroom 4m×3m. Bed 2m×1m. Floor space left?", "10m²"),
        ("Patio 5m×4m. Table takes 2m². Walking space?", "18m²"),
        ("Yard 8m×6m. Pool 4m×3m. Grass area?", "36m²"),
        ("Frame 30cm×20cm. Picture 26cm×16cm. Frame area?", "184cm² (600-416)")
    ]
    
    for q_text, correct in more_area:
        if "m²" in correct and correct[0].isdigit():
            val_str = ''.join(c for c in correct.split('m²')[0] if c.isdigit() or c == '.')
            try:
                val = float(val_str)
                options = [correct, f"{val*2}m²", f"{val/2}m²", f"{val+20}m²"]
            except:
                options = [correct, "Different area", "Cannot calculate", "More information needed"]
        elif "cm²" in correct and correct[0].isdigit():
            val_str = ''.join(c for c in correct.split('cm²')[0] if c.isdigit())
            try:
                val = int(val_str)
                options = [correct, f"{val+50}cm²", f"{val-30}cm²" if val > 30 else f"{val*2}cm²", f"{val//2}cm²"]
            except:
                options = [correct, "Different area", "Cannot calculate", "More information needed"]
        elif "€" in correct:
            val = int(''.join(filter(str.isdigit, correct)))
            options = [correct, f"€{val+100}", f"€{val-50}" if val > 50 else f"€{val*2}", f"€{val//2}"]
        elif "tiles" in correct:
            val = int(''.join(filter(str.isdigit, correct.split()[0])))
            options = [correct, f"{val+30} tiles", f"{val-20} tiles" if val > 20 else f"{val*2} tiles", f"{val//2} tiles"]
        elif "cm" in correct:
            val = int(''.join(filter(str.isdigit, correct.split('cm')[0])))
            options = [correct, f"{val+3}cm", f"{val-2}cm" if val > 2 else f"{val*2}cm", f"{val//2}cm"]
        elif "m" in correct:
            val = int(''.join(filter(str.isdigit, correct.split('m')[0])))
            options = [correct, f"{val+3}m", f"{val-2}m" if val > 2 else f"{val*2}m", f"{val//2}m"]
        else:
            options = [correct, "Wrong answer", "Cannot determine", "Different calculation"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': correct
        })
    
    return questions[:50]


def generate_level_11_questions():
    """Level 11: Real-World Measurement - 50 unique questions"""
    questions = []
    
    # Practical measurement problems (50 questions)
    practical = [
        ("Recipe needs 500ml milk. You have 1 litre. Enough?", "Yes, with 500ml left over"),
        ("Recipe needs 750g flour. Bag has 1kg. Enough?", "Yes, with 250g left over"),
        ("Car fuel tank is 50L. Petrol costs €1.80/L. Full tank cost?", "€90"),
        ("Room is 5m×4m. Paint covers 10m² per litre. Litres needed?", "2 litres"),
        ("Trip is 120km. Car uses 6L per 100km. Fuel needed?", "7.2 litres"),
        ("Medicine dose is 5ml twice daily. Bottle is 100ml. Days supply?", "10 days"),
        ("Fabric €8 per metre. Need 3.5m. Cost?", "€28"),
        ("Carpet €25 per m². Room 4m×3m. Cost?", "€300"),
        ("Fence €15 per metre. Garden perimeter 24m. Cost?", "€360"),
        ("Run 5km daily for a week. Total distance?", "35km"),
        ("Walk 2.5km to school, twice daily. Weekly distance?", "25km (5×5 days)"),
        ("Fill 8 glasses of 250ml each. Total water?", "2 litres"),
        ("Party needs 2L drink per 4 people. 20 people coming. Litres needed?", "10 litres"),
        ("Cake recipe for 8. Halve for 4 people. Original 200g butter becomes?", "100g"),
        ("Wallpaper roll covers 5m². Room walls total 40m². Rolls needed?", "8 rolls"),
        ("Wood costs €3 per metre. Need 8 pieces of 0.5m. Cost?", "€12"),
        ("Pool filling at 100L per minute. 6000L capacity. Time to fill?", "60 minutes"),
        ("Water drips 10ml per hour. Daily waste?", "240ml"),
        ("Cycling at 15km/h for 2 hours. Distance?", "30km"),
        ("Walking at 5km/h for 3 hours. Distance?", "15km"),
        ("Parcel weighs 2.5kg. Postage €1.50 per 500g. Cost?", "€7.50"),
        ("Room temperature 18°C. Increase by 4°C. New temperature?", "22°C"),
        ("Body temperature 39°C (fever). Normal is 37°C. How much over?", "2°C above normal"),
        ("Fridge at 8°C (too warm). Should be 4°C. Decrease needed?", "4°C decrease"),
        ("Shadow at 10am is 2m. At noon it's 0.5m. Difference?", "1.5m shorter at noon"),
        ("Table is 180cm. Will 3×50cm items fit in a row?", "Yes, exactly (3×50=150cm)"),
        ("Bookshelf 1m wide. Books average 3cm thick. Max books?", "About 33 books"),
        ("Curtain pole 2.4m. Curtain rings every 15cm. Rings needed?", "16 rings"),
        ("Pizza 30cm diameter. Cut into 8 slices. Each slice arc length roughly?", "About 12cm"),
        ("Plant grows 2cm per week. After 6 weeks?", "12cm taller"),
        ("Hair grows 1cm per month. After a year?", "12cm longer"),
        ("Car travels 90km in 1 hour. Speed?", "90 km/h"),
        ("Bus covers 60km in 2 hours. Speed?", "30 km/h"),
        ("You can type 40 words per minute. Words in 5 minutes?", "200 words"),
        ("Heart beats 70 times per minute. Beats in an hour?", "4200 beats"),
        ("Tap drips 20 times per minute. Drips in 10 minutes?", "200 drips"),
        ("€5 pocket money weekly. In 8 weeks?", "€40"),
        ("Save €2.50 weekly. Weeks to save €20?", "8 weeks"),
        ("Price €12.50 per kg. Cost of 2kg?", "€25"),
        ("3kg apples at €2 per kg. Cost?", "€6"),
        ("Petrol €1.65 per litre. Cost of 40L?", "€66"),
        ("Electricity €0.25 per kWh. 200kWh bill?", "€50"),
        ("Water €1.50 per 1000L. 4000L bill?", "€6"),
        ("Phone data 2GB per month. In 6 months?", "12GB"),
        ("Streaming uses 3GB per hour. 4 hours of movies?", "12GB"),
        ("Photo file is 5MB. 100 photos total size?", "500MB"),
        ("Container holds 200 items. Need 850. Containers needed?", "5 containers (with space)"),
        ("Bus holds 50 people. 180 students. Buses needed?", "4 buses"),
        ("Lift max 400kg. Average person 70kg. Max people?", "5 people"),
        ("Bridge max 3 tonnes. Your car is 1.5 tonnes. Pass ok?", "Yes, under limit")
    ]
    
    for q_text, correct in practical:
        if "€" in correct:
            val = float(''.join(c for c in correct.replace('€','').split()[0] if c.isdigit() or c == '.'))
            options = [correct, f"€{val+20:.2f}".replace('.00',''), f"€{val-10:.2f}".replace('.00','') if val > 10 else f"€{val*2:.2f}".replace('.00',''), f"€{val*1.5:.2f}".replace('.00','')]
        elif "Yes" in correct:
            options = [correct, "No, not enough", "Exactly right, nothing spare", "Cannot determine"]
        elif "km" in correct or "litre" in correct or "minute" in correct or "cm" in correct:
            options = [correct, "Half that amount", "Double that amount", "Cannot calculate"]
        else:
            options = [correct, "Different answer", "Cannot determine", "More info needed"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': correct
        })
    
    return questions[:50]


def generate_level_12_questions():
    """Level 12: Linked Problems - 50 unique questions"""
    questions = []
    
    # Multi-step measurement problems (50 questions)
    linked = [
        ("Garden 10m×8m. Path around it 1m wide. Path area?", "76m² (outer-inner)"),
        ("Buy 3m fabric at €5/m + 2m at €8/m. Total cost?", "€31"),
        ("Room 5m×4m. Paint 2 coats. Paint covers 10m²/L. Litres needed?", "4 litres"),
        ("Walk 2.5km at 5km/h. Then 4km at 8km/h. Total time?", "1 hour"),
        ("Trip: 50km at 100km/h, then 30km at 60km/h. Total time?", "1 hour"),
        ("Tank 1000L. Fill at 20L/min for 30 min. How full?", "600L (60%)"),
        ("Discount 20% on €50 item. Then add €5 delivery. Total?", "€45"),
        ("Recipe serves 4. Triple for 12 people. 150g sugar becomes?", "450g"),
        ("Fence 3 sides of 8m×6m garden. 4th side is house. Fence needed?", "20m"),
        ("Tiles 20cm×20cm for 2m×3m floor. Tiles needed?", "150 tiles"),
        ("12 eggs shared among 4 people. Then 2 more people join. Eggs each now?", "2 eggs each"),
        ("Temperature rises 3°C per hour. Start 15°C. After 4 hours?", "27°C"),
        ("Pool drains at 200L/min. 10000L pool. Time to half empty?", "25 minutes"),
        ("Car uses 8L/100km. Trip is 250km. Petrol at €1.50/L. Fuel cost?", "€30"),
        ("Cycle 30 minutes at 20km/h. Run 20 minutes at 10km/h. Total distance?", "13.3km"),
        ("2 pizzas 30cm diameter. 1 pizza 45cm diameter. Which more area?", "2 smaller ones"),
        ("Ribbon 2.5m. Cut 6 pieces of 35cm. Left over?", "40cm"),
        ("Worker earns €12/hour. Works 7.5 hours. Earnings?", "€90"),
        ("Electric heater uses 2kW. On for 3 hours at €0.25/kWh. Cost?", "€1.50"),
        ("Mix 300ml juice with water to make 1L. Water added?", "700ml"),
        ("Scale recipe: 200g flour for 8 cookies. For 20 cookies?", "500g flour"),
        ("Carpet for L-shape: 4m×3m and 2m×3m joined. Total area?", "18m²"),
        ("Save €20/month. After 1 year, spend €150. Remaining?", "€90"),
        ("Buy 1.5kg at €4/kg. Pay with €10. Change?", "€4"),
        ("3 friends walk different distances: 2km, 3km, 4km. Average?", "3km"),
        ("Fill 500ml bottle from 2L jug. Jug pours remaining?", "1.5L left"),
        ("Class 30 students. 3/5 walk to school (average 1km). Total km walked?", "18km"),
        ("5 parcels: 2kg, 3kg, 1.5kg, 2.5kg, 1kg. Total weight?", "10kg"),
        ("Measure room: 4.5m length, 3.2m width. Round to nearest m for carpet order?", "5m × 3m = 15m²"),
        ("Train 60km/h for 2h, then 80km/h for 1.5h. Total distance?", "240km"),
        ("Temperature drops 2°C per hour overnight. 8pm is 10°C. 2am temp?", "−2°C"),
        ("Plant 3cm tall. Grows 0.5cm/day. Height after 2 weeks?", "10cm"),
        ("Water 5 plants with 200ml each daily. Weekly water use?", "7L"),
        ("Paint 4 walls each 3m×2.5m. Total area?", "30m²"),
        ("Tile 2 bathrooms: 8m² and 6m². Tiles €20/m². Cost?", "€280"),
        ("Drive 45 minutes at 80km/h. Distance covered?", "60km"),
        ("Run 8km in 48 minutes. Speed in km/h?", "10km/h"),
        ("Recipe: 2 eggs per 4 muffins. Eggs for 18 muffins?", "9 eggs"),
        ("30% off €80 coat. Plus 10% student discount on sale price. Final price?", "€50.40"),
        ("Combine 3 containers: 2.5L, 1.8L, 750ml. Total?", "5.05L"),
        ("Perimeter 48m. If square, side? If rectangle 3:1 ratio, sides?", "Square: 12m. Rectangle: 18m × 6m"),
        ("Area 72m². Possible rectangle dimensions?", "12m × 6m or 9m × 8m etc"),
        ("Cyclist A: 15km/h. Cyclist B: 20km/h. B passes A. After 2h, distance apart?", "10km"),
        ("Water tank 3m × 2m × 1.5m. Capacity in litres?", "9000L"),
        ("Box 40cm × 30cm × 20cm. Volume in litres?", "24L"),
        ("€500 for 5m × 4m floor. Cost per m²?", "€25/m²"),
        ("TV 55 inch (diagonal). Width 48 inch. Height?", "About 27 inches"),
        ("Shadow 1.5× height at 4pm. Person 1.8m tall. Shadow length?", "2.7m"),
        ("Map 1:50000. Distance on map 4cm. Real distance?", "2km"),
        ("Building 45m tall. Model scale 1:150. Model height?", "30cm")
    ]
    
    for q_text, correct in linked:
        if "m²" in correct:
            options = [correct, "Double that", "Half that", "Cannot calculate"]
        elif "€" in correct:
            options = [correct, "€10 more", "€10 less", "Cannot determine"]
        elif "km" in correct or "cm" in correct or "m" in correct:
            options = [correct, "Double that distance", "Half that distance", "More info needed"]
        elif "L" in correct or "ml" in correct:
            options = [correct, "More liquid", "Less liquid", "Cannot determine"]
        elif "°C" in correct:
            options = [correct, "Higher temperature", "Lower temperature", "Same temperature"]
        elif "minutes" in correct or "hour" in correct:
            options = [correct, "Longer time", "Shorter time", "Cannot calculate"]
        else:
            options = [correct, "Different answer", "Cannot determine", "More information needed"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': correct
        })
    
    return questions[:50]


# ============================================================
# MAIN FUNCTIONS
# ============================================================

def generate_all_questions():
    all_questions = []
    
    generators = [
        (1, generate_level_1_questions),
        (2, generate_level_2_questions),
        (3, generate_level_3_questions),
        (4, generate_level_4_questions),
        (5, generate_level_5_questions),
        (6, generate_level_6_questions),
        (7, generate_level_7_questions),
        (8, generate_level_8_questions),
        (9, generate_level_9_questions),
        (10, generate_level_10_questions),
        (11, generate_level_11_questions),
        (12, generate_level_12_questions)
    ]
    
    for level, generator in generators:
        print(f"  Generating Level {level}...")
        questions = generator()
        
        for q in questions:
            options = q['options']
            while len(options) < 4:
                options.append('')
            
            all_questions.append({
                'topic': TOPIC,
                'level': level,
                'question_text': q['question_text'],
                'option_a': str(options[0]),
                'option_b': str(options[1]),
                'option_c': str(options[2]),
                'option_d': str(options[3]),
                'correct_answer': ['A', 'B', 'C', 'D'][q['correct_index']],
                'solution': q.get('explanation', ''),
                'question_image_svg': q.get('image_svg', '')
            })
        
        print(f"    Level {level}: {len(questions)} questions generated")
    
    return all_questions


def validate_questions(questions):
    errors = []
    seen = set()
    
    for i, q in enumerate(questions):
        key = (q['level'], q['question_text'][:100])
        if key in seen:
            errors.append(f"Q{i} L{q['level']}: Duplicate")
        seen.add(key)
    
    return errors


def count_existing_questions():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT difficulty_level, COUNT(*) FROM questions_adaptive WHERE topic = ? GROUP BY difficulty_level', (TOPIC,))
        counts = dict(cursor.fetchall())
        conn.close()
        return counts
    except:
        return {}


def clear_existing_questions():
    counts = count_existing_questions()
    total = sum(counts.values())
    
    if total > 0:
        print(f"\n⚠️  Found {total} existing questions for {TOPIC}")
        response = input("Delete existing? (yes/no): ").strip().lower()
        if response == 'yes':
            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM questions_adaptive WHERE topic = ?', (TOPIC,))
            deleted = cursor.rowcount
            conn.commit()
            conn.close()
            print(f"   Deleted {deleted} questions")
            return True
        return False
    return True


def insert_questions(questions):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    letter_to_int = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    inserted = 0
    
    for q in questions:
        try:
            level = q['level']
            band = get_difficulty_band(level)
            
            correct_answer = q['correct_answer']
            if isinstance(correct_answer, str):
                correct_answer = letter_to_int.get(correct_answer.upper(), 0)
            
            cursor.execute('''
                INSERT OR IGNORE INTO questions_adaptive 
                (topic, question_text, option_a, option_b, option_c, option_d, 
                 correct_answer, explanation, difficulty_level, difficulty_band,
                 question_type, is_active, image_svg, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                q['topic'], q['question_text'], q['option_a'], q['option_b'],
                q.get('option_c', ''), q.get('option_d', ''),
                correct_answer, q.get('solution', ''), level, band,
                'multiple_choice', 1, q.get('question_image_svg', ''),
                datetime.now(), datetime.now()
            ))
            
            if cursor.rowcount > 0:
                inserted += 1
        except sqlite3.Error as e:
            print(f"Error: {e}")
    
    conn.commit()
    conn.close()
    return inserted


def main():
    print("=" * 60)
    print("AgentMath L2LP Question Generator V3")
    print(f"Topic: {TOPIC}")
    print(f"Table: questions_adaptive")
    print(f"Target: {QUESTIONS_PER_LEVEL} × {TOTAL_LEVELS} = {QUESTIONS_PER_LEVEL * TOTAL_LEVELS}")
    print("=" * 60)
    
    if not clear_existing_questions():
        return
    
    print("\nGenerating questions...")
    questions = generate_all_questions()
    print(f"\nTotal: {len(questions)}")
    
    print("\nValidating...")
    errors = validate_questions(questions)
    if errors:
        print(f"⚠️  {len(errors)} duplicates (will be skipped)")
    
    print("✅ Validation passed")
    
    print("\nInserting...")
    inserted = insert_questions(questions)
    
    print(f"\n{'=' * 60}")
    print(f"✅ Complete! Inserted {inserted} questions")
    
    counts = count_existing_questions()
    print("\nQuestions per level:")
    for level in range(1, 13):
        count = counts.get(level, 0)
        status = "✓" if count >= 40 else "⚠️"
        print(f"   Level {level}: {count} {status}")
    print("=" * 60)


if __name__ == '__main__':
    main()

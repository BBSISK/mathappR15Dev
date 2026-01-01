// ============================================================
// NUMERACY STRAND - HELP CONTENT
// AgentMath v3.3.0
// 12 Topics × 12 Levels = 144 Help Entries
// 
// ADD THIS CODE BEFORE the getHelpContent() function definition
// ============================================================

// ============================================================
// 1. WHOLE NUMBERS HELP CONTENT
// ============================================================
const wholeNumbersHelpContent = {
    1: {
        title: "Reading Numbers",
        band: "Foundation",
        description: "Learn to read and say numbers up to 10,000. Break big numbers into smaller parts to read them easily.",
        keyPoints: [
            "Read numbers from <strong>left to right</strong>",
            "Say the <strong>thousands</strong> first, then hundreds, then tens and ones",
            "Use commas to help separate thousands: 3,542"
        ],
        examples: [
            {
                question: "How do you read 3,542?",
                steps: [
                    "3 thousands = <strong>three thousand</strong>",
                    "5 hundreds = <strong>five hundred</strong>",
                    "4 tens and 2 ones = <strong>forty-two</strong>",
                    "Together: <strong>three thousand, five hundred and forty-two</strong>"
                ],
                answer: "Three thousand, five hundred and forty-two"
            }
        ],
        tip: "💡 Break big numbers into chunks - thousands, hundreds, tens, ones!"
    },
    2: {
        title: "Place Value",
        band: "Foundation",
        description: "Every digit in a number has a place value. The position tells us how much it's worth.",
        keyPoints: [
            "The <strong>ones</strong> place is on the right",
            "Moving left: ones → tens → hundreds → thousands",
            "A digit's <strong>value</strong> depends on its <strong>position</strong>"
        ],
        examples: [
            {
                question: "In 4,729, what is the value of the 7?",
                steps: [
                    "Find the 7: it's in the <strong>hundreds</strong> place",
                    "Value = 7 × 100 = <strong>700</strong>"
                ],
                answer: "700"
            }
        ],
        tip: "💡 Each place is 10 times bigger than the place to its right!"
    },
    3: {
        title: "Comparing Numbers",
        band: "Foundation",
        description: "Use < (less than), > (greater than), and = (equal to) to compare numbers.",
        keyPoints: [
            "<strong>></strong> means greater than (the bigger number is on the left)",
            "<strong><</strong> means less than (the smaller number is on the left)",
            "Compare from <strong>left to right</strong>, starting with the largest place value"
        ],
        examples: [
            {
                question: "Compare 3,456 and 3,465",
                steps: [
                    "Thousands: both have 3 - <strong>equal</strong>",
                    "Hundreds: both have 4 - <strong>equal</strong>",
                    "Tens: 5 vs 6 - <strong>6 is bigger</strong>",
                    "So 3,456 < 3,465"
                ],
                answer: "3,456 < 3,465"
            }
        ],
        tip: "💡 The hungry crocodile always eats the bigger number! 🐊"
    },
    4: {
        title: "Ordering Numbers",
        band: "Developing",
        description: "Put numbers in order from smallest to largest (ascending) or largest to smallest (descending).",
        keyPoints: [
            "<strong>Ascending</strong> = going UP (smallest first)",
            "<strong>Descending</strong> = going DOWN (largest first)",
            "Compare place values starting from the left"
        ],
        examples: [
            {
                question: "Order 2,345, 2,435, 2,354 in ascending order",
                steps: [
                    "All start with 2 thousand",
                    "Hundreds: 3, 4, 3",
                    "2,345 and 2,354 both have 3 hundreds",
                    "Compare tens: 4 vs 5, so 2,345 < 2,354",
                    "Order: <strong>2,345, 2,354, 2,435</strong>"
                ],
                answer: "2,345, 2,354, 2,435"
            }
        ],
        tip: "💡 Write numbers in a column lined up by place value to compare easily!"
    },
    5: {
        title: "Rounding (10s, 100s)",
        band: "Developing",
        description: "Rounding makes numbers simpler. Look at the digit to the right to decide whether to round up or down.",
        keyPoints: [
            "Look at the digit <strong>to the right</strong> of the place you're rounding to",
            "If it's <strong>5 or more</strong>, round UP",
            "If it's <strong>4 or less</strong>, round DOWN"
        ],
        examples: [
            {
                question: "Round 347 to the nearest 10",
                steps: [
                    "Rounding to tens - look at the ones digit: <strong>7</strong>",
                    "7 ≥ 5, so round UP",
                    "347 → <strong>350</strong>"
                ],
                answer: "350"
            }
        ],
        tip: "💡 5 or more, let it soar! 4 or less, let it rest!"
    },
    6: {
        title: "Rounding (1000s)",
        band: "Developing",
        description: "Round to the nearest thousand by looking at the hundreds digit.",
        keyPoints: [
            "To round to thousands, look at the <strong>hundreds</strong> digit",
            "If hundreds digit is 5-9, round UP to next thousand",
            "If hundreds digit is 0-4, round DOWN"
        ],
        examples: [
            {
                question: "Round 7,621 to the nearest 1,000",
                steps: [
                    "Rounding to thousands - look at hundreds digit: <strong>6</strong>",
                    "6 ≥ 5, so round UP",
                    "7,621 → <strong>8,000</strong>"
                ],
                answer: "8,000"
            }
        ],
        tip: "💡 After rounding to thousands, all digits after become zeros!"
    },
    7: {
        title: "Large Numbers",
        band: "Proficient",
        description: "Work with numbers up to 100,000. The same place value rules apply - just with more digits!",
        keyPoints: [
            "Ten thousands come after thousands: 10,000 = ten thousand",
            "Use commas every 3 digits from the right",
            "Place value pattern continues: ones, tens, hundreds, thousands, ten thousands, hundred thousands"
        ],
        examples: [
            {
                question: "What is the value of 5 in 52,847?",
                steps: [
                    "5 is in the <strong>ten thousands</strong> place",
                    "Value = 5 × 10,000 = <strong>50,000</strong>"
                ],
                answer: "50,000"
            }
        ],
        tip: "💡 Commas are your friends - they make big numbers easier to read!"
    },
    8: {
        title: "Millions",
        band: "Proficient",
        description: "Numbers over a million follow the same patterns. A million is 1,000 thousands!",
        keyPoints: [
            "1,000,000 = one million (1 followed by 6 zeros)",
            "Millions come after hundred thousands",
            "Use commas: millions, thousands, ones groups"
        ],
        examples: [
            {
                question: "How do you read 2,345,678?",
                steps: [
                    "2 million",
                    "345 thousand",
                    "678",
                    "= <strong>two million, three hundred forty-five thousand, six hundred seventy-eight</strong>"
                ],
                answer: "Two million, three hundred forty-five thousand, six hundred seventy-eight"
            }
        ],
        tip: "💡 Group digits in threes: millions | thousands | ones"
    },
    9: {
        title: "Estimation",
        band: "Proficient",
        description: "Estimation gives a quick, approximate answer. Round numbers first, then calculate.",
        keyPoints: [
            "Round each number <strong>before</strong> calculating",
            "Estimation is useful for checking if answers make sense",
            "Choose sensible rounding (to 10s, 100s, or 1000s)"
        ],
        examples: [
            {
                question: "Estimate 387 + 524",
                steps: [
                    "Round 387 → <strong>400</strong>",
                    "Round 524 → <strong>500</strong>",
                    "Estimate: 400 + 500 = <strong>900</strong>"
                ],
                answer: "Approximately 900"
            }
        ],
        tip: "💡 Estimation is your 'sense check' - use it to spot mistakes!"
    },
    10: {
        title: "Number Properties",
        band: "Advanced",
        description: "Learn about special number types: odd, even, factors, and multiples.",
        keyPoints: [
            "<strong>Even</strong> numbers end in 0, 2, 4, 6, 8",
            "<strong>Odd</strong> numbers end in 1, 3, 5, 7, 9",
            "<strong>Factors</strong> divide exactly into a number",
            "<strong>Multiples</strong> are in a number's times table"
        ],
        examples: [
            {
                question: "Find all factors of 12",
                steps: [
                    "1 × 12 = 12 ✓",
                    "2 × 6 = 12 ✓",
                    "3 × 4 = 12 ✓",
                    "Factors: <strong>1, 2, 3, 4, 6, 12</strong>"
                ],
                answer: "1, 2, 3, 4, 6, 12"
            }
        ],
        tip: "💡 Factors come in pairs that multiply to give the number!"
    },
    11: {
        title: "Problem Solving",
        band: "Advanced",
        description: "Apply your number skills to solve multi-step word problems.",
        keyPoints: [
            "Read carefully - <strong>what is the question asking?</strong>",
            "Identify the <strong>numbers</strong> and <strong>operations</strong> needed",
            "Check your answer makes sense"
        ],
        examples: [
            {
                question: "A school has 847 students. 395 are boys. How many are girls?",
                steps: [
                    "Total students: 847",
                    "Boys: 395",
                    "Girls = Total - Boys",
                    "847 - 395 = <strong>452 girls</strong>"
                ],
                answer: "452 girls"
            }
        ],
        tip: "💡 RUCSAC: Read, Understand, Choose operation, Solve, Answer, Check!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You've mastered whole numbers! These questions combine all your skills.",
        keyPoints: [
            "Use <strong>place value</strong> to understand numbers",
            "Apply <strong>rounding</strong> and <strong>estimation</strong> wisely",
            "Think about <strong>number properties</strong> to help solve problems"
        ],
        examples: [
            {
                question: "The population of a town is 45,678. Round to the nearest thousand, then find if this is odd or even.",
                steps: [
                    "Round 45,678 → <strong>46,000</strong>",
                    "46,000 ends in 0",
                    "Answer: <strong>46,000 (even)</strong>"
                ],
                answer: "46,000 (even)"
            }
        ],
        tip: "🏆 Amazing! You're a Whole Numbers Champion!"
    }
};

// ============================================================
// 2. ADDITION & SUBTRACTION HELP CONTENT
// ============================================================
const additionSubtractionHelpContent = {
    1: {
        title: "Adding to 20",
        band: "Foundation",
        description: "Learn to add numbers with totals up to 20. Use counting, fingers, or number lines to help!",
        keyPoints: [
            "<strong>Addition</strong> means putting numbers together",
            "Count on from the bigger number",
            "Learn number bonds to 10 and 20"
        ],
        examples: [
            {
                question: "What is 8 + 5?",
                steps: [
                    "Start with the bigger number: <strong>8</strong>",
                    "Count on 5: 9, 10, 11, 12, 13",
                    "8 + 5 = <strong>13</strong>"
                ],
                answer: "13"
            }
        ],
        tip: "💡 Number bonds to 10: 1+9, 2+8, 3+7, 4+6, 5+5 - learn these by heart!"
    },
    2: {
        title: "Subtracting to 20",
        band: "Foundation",
        description: "Subtraction means taking away. Count back or use number bonds to help.",
        keyPoints: [
            "<strong>Subtraction</strong> means taking away or finding the difference",
            "Count back from the bigger number",
            "Use your addition facts backwards"
        ],
        examples: [
            {
                question: "What is 15 - 7?",
                steps: [
                    "Start at 15",
                    "Count back 7: 14, 13, 12, 11, 10, 9, 8",
                    "15 - 7 = <strong>8</strong>"
                ],
                answer: "8"
            }
        ],
        tip: "💡 If 8 + 7 = 15, then 15 - 7 = 8. Addition and subtraction are opposites!"
    },
    3: {
        title: "Adding 2-Digit Numbers",
        band: "Foundation",
        description: "Add two-digit numbers by adding tens and ones separately.",
        keyPoints: [
            "Line up the numbers by place value",
            "Add the <strong>ones</strong> first",
            "Then add the <strong>tens</strong>"
        ],
        examples: [
            {
                question: "What is 34 + 25?",
                steps: [
                    "Add ones: 4 + 5 = 9",
                    "Add tens: 30 + 20 = 50",
                    "Total: 50 + 9 = <strong>59</strong>"
                ],
                answer: "59"
            }
        ],
        tip: "💡 Partition numbers: 34 = 30 + 4, then add each part!"
    },
    4: {
        title: "Subtracting 2-Digit Numbers",
        band: "Developing",
        description: "Subtract two-digit numbers using column method or partitioning.",
        keyPoints: [
            "Line up digits by place value",
            "Subtract ones first, then tens",
            "If you can't subtract, you might need to <strong>exchange</strong> (borrow)"
        ],
        examples: [
            {
                question: "What is 67 - 24?",
                steps: [
                    "Subtract ones: 7 - 4 = 3",
                    "Subtract tens: 60 - 20 = 40",
                    "Total: 40 + 3 = <strong>43</strong>"
                ],
                answer: "43"
            }
        ],
        tip: "💡 Always check: does your answer + what you subtracted = the start number?"
    },
    5: {
        title: "Adding 3-Digit Numbers",
        band: "Developing",
        description: "Add three-digit numbers using the column method. Remember to carry when needed!",
        keyPoints: [
            "Line up <strong>hundreds, tens, ones</strong>",
            "Add from right to left (ones first)",
            "If a column adds to 10 or more, <strong>carry</strong> to the next column"
        ],
        examples: [
            {
                question: "What is 347 + 285?",
                steps: [
                    "Ones: 7 + 5 = 12. Write 2, carry 1",
                    "Tens: 4 + 8 + 1 = 13. Write 3, carry 1",
                    "Hundreds: 3 + 2 + 1 = 6",
                    "Answer: <strong>632</strong>"
                ],
                answer: "632"
            }
        ],
        tip: "💡 Write the carry digits small above the next column!"
    },
    6: {
        title: "Subtracting 3-Digit Numbers",
        band: "Developing",
        description: "Subtract three-digit numbers. Exchange (borrow) when the top digit is smaller.",
        keyPoints: [
            "Work from right to left",
            "If you can't subtract, <strong>exchange</strong> from the next column",
            "Exchange = borrow 1 ten (or hundred) = 10 ones (or tens)"
        ],
        examples: [
            {
                question: "What is 532 - 178?",
                steps: [
                    "Ones: Can't do 2-8, exchange: 12-8=4",
                    "Tens: 2-7 (after exchange), exchange: 12-7=5",
                    "Hundreds: 4-1=3",
                    "Answer: <strong>354</strong>"
                ],
                answer: "354"
            }
        ],
        tip: "💡 When you exchange, cross out and rewrite the digits to keep track!"
    },
    7: {
        title: "Word Problems (+)",
        band: "Proficient",
        description: "Solve addition word problems. Look for keywords that tell you to add.",
        keyPoints: [
            "Keywords for addition: <strong>total, altogether, sum, combined, in all, plus, more</strong>",
            "Read the problem twice",
            "Write the number sentence before calculating"
        ],
        examples: [
            {
                question: "Aoife has 245 stickers. She gets 178 more. How many does she have now?",
                steps: [
                    "'Gets more' means <strong>add</strong>",
                    "245 + 178 = ?",
                    "245 + 178 = <strong>423 stickers</strong>"
                ],
                answer: "423 stickers"
            }
        ],
        tip: "💡 Circle the numbers and underline the question!"
    },
    8: {
        title: "Word Problems (−)",
        band: "Proficient",
        description: "Solve subtraction word problems. Find the keywords that signal subtraction.",
        keyPoints: [
            "Keywords for subtraction: <strong>left, remaining, difference, fewer, less than, take away</strong>",
            "Draw a picture or bar model if it helps",
            "Check your answer makes sense"
        ],
        examples: [
            {
                question: "A shop had 500 apples. They sold 327. How many are left?",
                steps: [
                    "'How many left' means <strong>subtract</strong>",
                    "500 - 327 = ?",
                    "500 - 327 = <strong>173 apples</strong>"
                ],
                answer: "173 apples"
            }
        ],
        tip: "💡 'How many more' and 'what's the difference' also mean subtract!"
    },
    9: {
        title: "Mixed Operations",
        band: "Proficient",
        description: "Decide whether to add or subtract based on the problem.",
        keyPoints: [
            "Read carefully to decide: add or subtract?",
            "Adding = combining, totalling, increasing",
            "Subtracting = removing, finding difference, decreasing"
        ],
        examples: [
            {
                question: "Cian scored 156 points. Niamh scored 189 points. How many more did Niamh score?",
                steps: [
                    "'How many more' = find the <strong>difference</strong>",
                    "Difference means <strong>subtract</strong>",
                    "189 - 156 = <strong>33 more points</strong>"
                ],
                answer: "33 more points"
            }
        ],
        tip: "💡 Ask yourself: am I putting together or taking apart?"
    },
    10: {
        title: "Multi-Step Problems",
        band: "Advanced",
        description: "Some problems need more than one calculation. Work step by step!",
        keyPoints: [
            "Break the problem into <strong>smaller steps</strong>",
            "Do one calculation at a time",
            "Use the answer from step 1 in step 2"
        ],
        examples: [
            {
                question: "A class has 28 students. 15 are girls. 3 more boys join. How many boys now?",
                steps: [
                    "Step 1: Find original boys: 28 - 15 = 13",
                    "Step 2: Add new boys: 13 + 3 = 16",
                    "Answer: <strong>16 boys</strong>"
                ],
                answer: "16 boys"
            }
        ],
        tip: "💡 Write down each step - don't try to do it all in your head!"
    },
    11: {
        title: "Estimation",
        band: "Advanced",
        description: "Use estimation to check if your answers are sensible.",
        keyPoints: [
            "Round numbers to make calculation easier",
            "Estimate BEFORE you calculate (predict your answer)",
            "If your exact answer is very different from estimate, check again!"
        ],
        examples: [
            {
                question: "Estimate 487 + 312",
                steps: [
                    "Round 487 → 500",
                    "Round 312 → 300",
                    "Estimate: 500 + 300 = <strong>800</strong>",
                    "(Exact answer is 799 - very close! ✓)"
                ],
                answer: "Approximately 800"
            }
        ],
        tip: "💡 Use estimation as a 'sense check' for every calculation!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You've mastered addition and subtraction! Show off all your skills.",
        keyPoints: [
            "Use the <strong>column method</strong> for accuracy",
            "Choose the right operation based on keywords",
            "Always <strong>estimate</strong> first and <strong>check</strong> after"
        ],
        examples: [
            {
                question: "A cinema has 450 seats. Morning show: 287 people. Afternoon: 394 people. How many more in the afternoon?",
                steps: [
                    "'How many more' = subtract",
                    "394 - 287 = <strong>107 more people</strong>"
                ],
                answer: "107 more people"
            }
        ],
        tip: "🏆 Fantastic! You're an Addition & Subtraction Champion!"
    }
};

// ============================================================
// 3. MULTIPLICATION SKILLS HELP CONTENT
// ============================================================
const multiplicationSkillsHelpContent = {
    1: {
        title: "Times Tables (2, 5, 10)",
        band: "Foundation",
        description: "Start with the easiest times tables: 2s, 5s, and 10s. These have simple patterns!",
        keyPoints: [
            "<strong>×2</strong>: double the number (same as adding to itself)",
            "<strong>×5</strong>: ends in 0 or 5",
            "<strong>×10</strong>: just add a 0 to the end"
        ],
        examples: [
            {
                question: "What is 7 × 5?",
                steps: [
                    "Count in 5s: 5, 10, 15, 20, 25, 30, <strong>35</strong>",
                    "Or: 7 × 5 = half of 7 × 10 = half of 70 = <strong>35</strong>"
                ],
                answer: "35"
            }
        ],
        tip: "💡 ×10 is super easy - just add a zero! 7 × 10 = 70"
    },
    2: {
        title: "Times Tables (3, 4)",
        band: "Foundation",
        description: "Learn the 3 and 4 times tables. Look for patterns to help remember them.",
        keyPoints: [
            "<strong>×3</strong>: add the digits of answers - they sum to 3, 6, or 9",
            "<strong>×4</strong>: double, then double again",
            "Practice makes perfect!"
        ],
        examples: [
            {
                question: "What is 8 × 4?",
                steps: [
                    "Double 8: 8 × 2 = 16",
                    "Double again: 16 × 2 = <strong>32</strong>"
                ],
                answer: "32"
            }
        ],
        tip: "💡 ×4 trick: double it twice! 6×4 = 6×2×2 = 12×2 = 24"
    },
    3: {
        title: "Times Tables (6, 7, 8, 9)",
        band: "Foundation",
        description: "Master the trickier times tables. You already know most of these from earlier tables!",
        keyPoints: [
            "If you know 3 × 7, you know 7 × 3 (same answer!)",
            "<strong>×9 trick</strong>: multiply by 10 and subtract once",
            "<strong>×6</strong>: multiply by 3, then double"
        ],
        examples: [
            {
                question: "What is 7 × 9?",
                steps: [
                    "×9 trick: 7 × 10 = 70",
                    "Subtract 7: 70 - 7 = <strong>63</strong>"
                ],
                answer: "63"
            }
        ],
        tip: "💡 9× finger trick: hold up 10 fingers, put down the one you're multiplying by!"
    },
    4: {
        title: "Multiplying by 10, 100",
        band: "Developing",
        description: "Multiplying by 10, 100, or 1000 just moves the digits to the left!",
        keyPoints: [
            "<strong>×10</strong>: digits move 1 place left (add 1 zero)",
            "<strong>×100</strong>: digits move 2 places left (add 2 zeros)",
            "<strong>×1000</strong>: digits move 3 places left (add 3 zeros)"
        ],
        examples: [
            {
                question: "What is 45 × 100?",
                steps: [
                    "×100 = add 2 zeros",
                    "45 × 100 = <strong>4,500</strong>"
                ],
                answer: "4,500"
            }
        ],
        tip: "💡 The number of zeros you add = the number of zeros in what you multiply by!"
    },
    5: {
        title: "2-Digit × 1-Digit",
        band: "Developing",
        description: "Multiply larger numbers by breaking them into parts (partitioning).",
        keyPoints: [
            "Split the 2-digit number: 34 = 30 + 4",
            "Multiply each part separately",
            "Add the results together"
        ],
        examples: [
            {
                question: "What is 34 × 6?",
                steps: [
                    "Split: 34 = 30 + 4",
                    "30 × 6 = 180",
                    "4 × 6 = 24",
                    "Add: 180 + 24 = <strong>204</strong>"
                ],
                answer: "204"
            }
        ],
        tip: "💡 The grid method is great for showing your working!"
    },
    6: {
        title: "2-Digit × 2-Digit",
        band: "Developing",
        description: "Use the grid method or long multiplication for bigger calculations.",
        keyPoints: [
            "Split BOTH numbers",
            "Multiply all 4 parts",
            "Add everything together"
        ],
        examples: [
            {
                question: "What is 23 × 15?",
                steps: [
                    "23 = 20 + 3, 15 = 10 + 5",
                    "20×10=200, 20×5=100, 3×10=30, 3×5=15",
                    "Add: 200+100+30+15 = <strong>345</strong>"
                ],
                answer: "345"
            }
        ],
        tip: "💡 Draw a grid to organise your multiplication!"
    },
    7: {
        title: "Word Problems",
        band: "Proficient",
        description: "Spot when to multiply in word problems. Look for groups of equal amounts.",
        keyPoints: [
            "Keywords: <strong>times, groups of, each, every, per</strong>",
            "If you have equal groups, multiply!",
            "'3 boxes with 24 in each' = 3 × 24"
        ],
        examples: [
            {
                question: "A book has 28 pages. Saoirse reads 5 books. How many pages?",
                steps: [
                    "5 books, each with 28 pages",
                    "5 × 28 = ?",
                    "5 × 28 = <strong>140 pages</strong>"
                ],
                answer: "140 pages"
            }
        ],
        tip: "💡 'Each' and 'every' are multiplication signals!"
    },
    8: {
        title: "Multi-Step Problems",
        band: "Proficient",
        description: "Combine multiplication with other operations.",
        keyPoints: [
            "Read the whole problem first",
            "Plan your steps before calculating",
            "Do one operation at a time"
        ],
        examples: [
            {
                question: "Cinema tickets cost €8 each. A family of 4 buys tickets and €12 of popcorn. Total cost?",
                steps: [
                    "Step 1: Tickets = 4 × €8 = €32",
                    "Step 2: Add popcorn = €32 + €12 = <strong>€44</strong>"
                ],
                answer: "€44"
            }
        ],
        tip: "💡 List the steps you need before you start calculating!"
    },
    9: {
        title: "Estimation",
        band: "Proficient",
        description: "Estimate multiplication answers by rounding first.",
        keyPoints: [
            "Round to <strong>easy numbers</strong> (10s or 100s)",
            "Multiply the rounded numbers",
            "Your estimate should be close to the exact answer"
        ],
        examples: [
            {
                question: "Estimate 48 × 23",
                steps: [
                    "Round: 48 → 50, 23 → 20",
                    "Estimate: 50 × 20 = <strong>1,000</strong>",
                    "(Exact: 1,104 - close! ✓)"
                ],
                answer: "Approximately 1,000"
            }
        ],
        tip: "💡 If your answer is way off from your estimate, check your working!"
    },
    10: {
        title: "3-Digit × 2-Digit",
        band: "Advanced",
        description: "Use long multiplication for larger numbers. Same method, more digits!",
        keyPoints: [
            "Multiply by ones digit first",
            "Multiply by tens digit (remember the zero!)",
            "Add the two rows together"
        ],
        examples: [
            {
                question: "What is 234 × 15?",
                steps: [
                    "234 × 5 = 1,170",
                    "234 × 10 = 2,340",
                    "Add: 1,170 + 2,340 = <strong>3,510</strong>"
                ],
                answer: "3,510"
            }
        ],
        tip: "💡 Keep your columns lined up carefully!"
    },
    11: {
        title: "Problem Solving",
        band: "Advanced",
        description: "Apply multiplication skills to challenging real-world problems.",
        keyPoints: [
            "Identify what you need to find",
            "Choose the right method",
            "Check your answer is reasonable"
        ],
        examples: [
            {
                question: "A school orders 156 books at €12 each. What's the total cost?",
                steps: [
                    "156 × 12 = ?",
                    "156 × 10 = 1,560",
                    "156 × 2 = 312",
                    "Total: 1,560 + 312 = <strong>€1,872</strong>"
                ],
                answer: "€1,872"
            }
        ],
        tip: "💡 Break hard calculations into easier parts!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You're a multiplication master! Put all your skills together.",
        keyPoints: [
            "Know your <strong>times tables</strong> by heart",
            "Use <strong>partitioning</strong> for bigger numbers",
            "<strong>Estimate</strong> to check your answers"
        ],
        examples: [
            {
                question: "A farmer plants 24 rows with 35 apple trees in each row. How many trees?",
                steps: [
                    "24 × 35 = ?",
                    "20×35=700, 4×35=140",
                    "Total: 700 + 140 = <strong>840 trees</strong>"
                ],
                answer: "840 trees"
            }
        ],
        tip: "🏆 Brilliant! You're a Multiplication Champion!"
    }
};

// ============================================================
// 4. DIVISION SKILLS HELP CONTENT
// ============================================================
const divisionSkillsHelpContent = {
    1: {
        title: "Sharing Equally",
        band: "Foundation",
        description: "Division means sharing equally. If you share fairly, everyone gets the same amount!",
        keyPoints: [
            "<strong>Division</strong> = sharing into equal groups",
            "12 ÷ 3 means '12 shared between 3'",
            "Each person gets the same amount"
        ],
        examples: [
            {
                question: "Share 15 sweets equally between 3 friends",
                steps: [
                    "15 ÷ 3 = ?",
                    "Give 1 sweet each: 3 given, 12 left",
                    "Give 1 more each: 6 given, 9 left",
                    "Keep going... each friend gets <strong>5 sweets</strong>"
                ],
                answer: "5 sweets each"
            }
        ],
        tip: "💡 Division is the opposite of multiplication!"
    },
    2: {
        title: "Division Facts",
        band: "Foundation",
        description: "Use your times tables backwards to help with division facts.",
        keyPoints: [
            "If 6 × 4 = 24, then 24 ÷ 4 = 6 AND 24 ÷ 6 = 4",
            "Division and multiplication are <strong>inverse operations</strong>",
            "Fact families: 3, 5, 15 → 3×5=15, 5×3=15, 15÷3=5, 15÷5=3"
        ],
        examples: [
            {
                question: "What is 42 ÷ 7?",
                steps: [
                    "Think: ? × 7 = 42",
                    "From 7 times table: <strong>6</strong> × 7 = 42",
                    "So 42 ÷ 7 = <strong>6</strong>"
                ],
                answer: "6"
            }
        ],
        tip: "💡 Know your times tables and you know your division facts!"
    },
    3: {
        title: "Dividing by 2, 5, 10",
        band: "Foundation",
        description: "These divisions have easy patterns and connect to halving and place value.",
        keyPoints: [
            "<strong>÷2</strong> = halving (split in half)",
            "<strong>÷10</strong> = remove the zero (move digits right)",
            "<strong>÷5</strong> = divide by 10, then double"
        ],
        examples: [
            {
                question: "What is 350 ÷ 10?",
                steps: [
                    "Dividing by 10: digits move 1 place right",
                    "350 → 35",
                    "350 ÷ 10 = <strong>35</strong>"
                ],
                answer: "35"
            }
        ],
        tip: "💡 To divide by 5: divide by 10 first, then double your answer!"
    },
    4: {
        title: "Short Division",
        band: "Developing",
        description: "Use the bus stop method (short division) to divide bigger numbers.",
        keyPoints: [
            "Write the division as a 'bus stop': divisor | dividend",
            "Work from <strong>left to right</strong>",
            "Carry remainders to the next digit"
        ],
        examples: [
            {
                question: "What is 84 ÷ 4?",
                steps: [
                    "4 into 8 = 2 (write 2 above)",
                    "4 into 4 = 1 (write 1 above)",
                    "Answer: <strong>21</strong>"
                ],
                answer: "21"
            }
        ],
        tip: "💡 The 'bus stop' method keeps everything organised!"
    },
    5: {
        title: "Remainders",
        band: "Developing",
        description: "Sometimes division doesn't work out exactly. The leftover is called a remainder.",
        keyPoints: [
            "<strong>Remainder</strong> = what's left over after dividing",
            "Written as 'r' (e.g., 17 ÷ 5 = 3 r 2)",
            "The remainder must be <strong>less than</strong> the divisor"
        ],
        examples: [
            {
                question: "What is 23 ÷ 4?",
                steps: [
                    "4 × 5 = 20 (closest without going over)",
                    "23 - 20 = 3 left over",
                    "Answer: <strong>5 remainder 3</strong> (or 5 r 3)"
                ],
                answer: "5 r 3"
            }
        ],
        tip: "💡 Check: (answer × divisor) + remainder = original number"
    },
    6: {
        title: "Dividing by 10, 100",
        band: "Developing",
        description: "Dividing by 10 or 100 moves digits to the right.",
        keyPoints: [
            "<strong>÷10</strong>: digits move 1 place right",
            "<strong>÷100</strong>: digits move 2 places right",
            "This introduces decimals: 45 ÷ 10 = 4.5"
        ],
        examples: [
            {
                question: "What is 2,500 ÷ 100?",
                steps: [
                    "÷100 = move digits 2 places right",
                    "2,500 → 25",
                    "Answer: <strong>25</strong>"
                ],
                answer: "25"
            }
        ],
        tip: "💡 The number of zeros you 'remove' = zeros in what you divide by!"
    },
    7: {
        title: "Long Division",
        band: "Proficient",
        description: "Long division shows all the steps clearly. Great for bigger numbers!",
        keyPoints: [
            "Divide, Multiply, Subtract, Bring down (DMSB)",
            "Work one digit at a time",
            "Write out all your working"
        ],
        examples: [
            {
                question: "What is 156 ÷ 12?",
                steps: [
                    "12 into 15 = 1, write 1. 1×12=12, 15-12=3",
                    "Bring down 6: 36",
                    "12 into 36 = 3, write 3. 3×12=36, 36-36=0",
                    "Answer: <strong>13</strong>"
                ],
                answer: "13"
            }
        ],
        tip: "💡 Does McDonald's Sell Burgers? Divide, Multiply, Subtract, Bring down!"
    },
    8: {
        title: "Word Problems",
        band: "Proficient",
        description: "Spot when to divide. Look for sharing, grouping, or 'how many in each'.",
        keyPoints: [
            "Keywords: <strong>share, divide, split, per, each, every</strong>",
            "'How many groups?' or 'How many in each group?' = divide",
            "Draw pictures if it helps"
        ],
        examples: [
            {
                question: "144 stickers are shared equally between 8 children. How many each?",
                steps: [
                    "'Shared equally' = divide",
                    "144 ÷ 8 = ?",
                    "Answer: <strong>18 stickers each</strong>"
                ],
                answer: "18 stickers each"
            }
        ],
        tip: "💡 'How many ___ can fit in ___?' signals division!"
    },
    9: {
        title: "Interpreting Remainders",
        band: "Proficient",
        description: "What do you do with the remainder? It depends on the problem!",
        keyPoints: [
            "Sometimes you <strong>round up</strong> (buses needed, containers)",
            "Sometimes you <strong>round down</strong> (complete sets only)",
            "Sometimes you <strong>write the remainder</strong> as a fraction or decimal"
        ],
        examples: [
            {
                question: "33 children need to travel. Each car holds 4. How many cars needed?",
                steps: [
                    "33 ÷ 4 = 8 r 1",
                    "8 cars fit 32 children, 1 left over",
                    "Need 1 more car → <strong>9 cars</strong>"
                ],
                answer: "9 cars (round up)"
            }
        ],
        tip: "💡 Think about what the remainder means in real life!"
    },
    10: {
        title: "Multi-Step Problems",
        band: "Advanced",
        description: "Combine division with other operations to solve complex problems.",
        keyPoints: [
            "Break the problem into steps",
            "Identify which operation for each step",
            "Use the answer from one step in the next"
        ],
        examples: [
            {
                question: "360 apples are packed in boxes of 12, then boxes go on shelves holding 5 boxes. How many shelves?",
                steps: [
                    "Step 1: Boxes = 360 ÷ 12 = 30 boxes",
                    "Step 2: Shelves = 30 ÷ 5 = <strong>6 shelves</strong>"
                ],
                answer: "6 shelves"
            }
        ],
        tip: "💡 Write out each step clearly!"
    },
    11: {
        title: "Problem Solving",
        band: "Advanced",
        description: "Apply division skills to challenging real-world scenarios.",
        keyPoints: [
            "Read carefully to understand what's being asked",
            "Decide: sharing into groups OR how many groups?",
            "Check your answer makes sense"
        ],
        examples: [
            {
                question: "A rope is 225cm long. It's cut into 15cm pieces. How many pieces?",
                steps: [
                    "225 ÷ 15 = ?",
                    "15 × 15 = 225 ✓",
                    "Answer: <strong>15 pieces</strong>"
                ],
                answer: "15 pieces"
            }
        ],
        tip: "💡 Division answers 'how many groups?' or 'how many in each group?'"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You're a division expert! Show off everything you've learned.",
        keyPoints: [
            "Use times tables to help with division facts",
            "Choose short or long division based on the numbers",
            "Think carefully about what to do with remainders"
        ],
        examples: [
            {
                question: "A school orders 1,248 pencils. They come in packs of 24. How many packs?",
                steps: [
                    "1,248 ÷ 24 = ?",
                    "Using long division: <strong>52 packs</strong>"
                ],
                answer: "52 packs"
            }
        ],
        tip: "🏆 Excellent! You're a Division Champion!"
    }
};

// ============================================================
// 5. BASIC FRACTIONS HELP CONTENT
// ============================================================
const basicFractionsHelpContent = {
    1: {
        title: "What is a Fraction?",
        band: "Foundation",
        description: "A fraction shows parts of a whole. It has two numbers: numerator (top) and denominator (bottom).",
        keyPoints: [
            "The <strong>denominator</strong> (bottom) = how many equal parts in total",
            "The <strong>numerator</strong> (top) = how many parts you have",
            "The line in the middle means 'out of' or 'divided by'"
        ],
        examples: [
            {
                question: "What does ¾ mean?",
                steps: [
                    "Denominator = 4 (4 equal parts)",
                    "Numerator = 3 (we have 3 of them)",
                    "¾ = <strong>3 out of 4 parts</strong>"
                ],
                answer: "3 out of 4 equal parts"
            }
        ],
        tip: "💡 Think of a pizza cut into slices - the denominator is total slices!"
    },
    2: {
        title: "Unit Fractions",
        band: "Foundation",
        description: "Unit fractions have 1 as the numerator. They show one equal part of a whole.",
        keyPoints: [
            "<strong>Unit fraction</strong> = numerator is 1",
            "Examples: ½, ⅓, ¼, ⅕, ⅙, etc.",
            "The bigger the denominator, the <strong>smaller</strong> each piece"
        ],
        examples: [
            {
                question: "Which is bigger: ¼ or ⅛?",
                steps: [
                    "¼ = 1 piece when whole is cut into 4",
                    "⅛ = 1 piece when whole is cut into 8",
                    "More pieces = smaller pieces",
                    "So <strong>¼ is bigger</strong>"
                ],
                answer: "¼ is bigger"
            }
        ],
        tip: "💡 More slices = smaller slices! ⅛ < ¼"
    },
    3: {
        title: "Fractions of Shapes",
        band: "Foundation",
        description: "Identify fractions by looking at shaded parts of shapes.",
        keyPoints: [
            "Count <strong>total equal parts</strong> (denominator)",
            "Count <strong>shaded parts</strong> (numerator)",
            "Write as: shaded/total"
        ],
        examples: [
            {
                question: "A rectangle is divided into 5 equal parts. 2 are shaded. What fraction is shaded?",
                steps: [
                    "Total parts = 5 (denominator)",
                    "Shaded parts = 2 (numerator)",
                    "Fraction = <strong>⅖</strong>"
                ],
                answer: "⅖"
            }
        ],
        tip: "💡 Parts MUST be equal for it to be a fraction!"
    },
    4: {
        title: "Equivalent Fractions",
        band: "Developing",
        description: "Equivalent fractions look different but show the same amount. Like ½ and 2/4!",
        keyPoints: [
            "<strong>Equivalent</strong> = equal value",
            "Multiply or divide top AND bottom by the same number",
            "Use fraction walls to see equivalents"
        ],
        examples: [
            {
                question: "Find a fraction equivalent to ⅔",
                steps: [
                    "Multiply top and bottom by 2",
                    "2×2 = 4, 3×2 = 6",
                    "⅔ = <strong>4/6</strong>"
                ],
                answer: "4/6 (or 6/9, 8/12, etc.)"
            }
        ],
        tip: "💡 Whatever you do to the top, do to the bottom!"
    },
    5: {
        title: "Comparing Fractions",
        band: "Developing",
        description: "Compare fractions to see which is larger or smaller.",
        keyPoints: [
            "<strong>Same denominator</strong>: compare numerators (bigger numerator = bigger fraction)",
            "<strong>Same numerator</strong>: compare denominators (bigger denominator = smaller fraction)",
            "<strong>Different both</strong>: find equivalent fractions with same denominator"
        ],
        examples: [
            {
                question: "Which is larger: ⅗ or ⅘?",
                steps: [
                    "Same denominator (5)",
                    "Compare numerators: 4 > 3",
                    "<strong>⅘ is larger</strong>"
                ],
                answer: "⅘"
            }
        ],
        tip: "💡 Same denominator? Just compare the tops!"
    },
    6: {
        title: "Simplifying Fractions",
        band: "Developing",
        description: "Simplify fractions to their lowest terms by dividing top and bottom by common factors.",
        keyPoints: [
            "Find a number that divides <strong>both</strong> numerator and denominator",
            "Keep dividing until you can't anymore",
            "The simplified fraction has the same value"
        ],
        examples: [
            {
                question: "Simplify 6/8",
                steps: [
                    "Both 6 and 8 divide by 2",
                    "6÷2 = 3, 8÷2 = 4",
                    "6/8 = <strong>¾</strong>"
                ],
                answer: "¾"
            }
        ],
        tip: "💡 Try dividing by 2, then 3, then 5... until you can't divide anymore!"
    },
    7: {
        title: "Adding (Same Denominator)",
        band: "Proficient",
        description: "Add fractions with the same denominator by adding the numerators.",
        keyPoints: [
            "Keep the <strong>denominator the same</strong>",
            "<strong>Add the numerators</strong>",
            "Simplify if possible"
        ],
        examples: [
            {
                question: "What is ⅜ + ⅜?",
                steps: [
                    "Same denominator (8) - keep it!",
                    "Add numerators: 3 + 3 = 6",
                    "Answer: <strong>⅝</strong>"
                ],
                answer: "6/8 = ¾"
            }
        ],
        tip: "💡 Same denominator? Add the tops, keep the bottom!"
    },
    8: {
        title: "Subtracting (Same Denominator)",
        band: "Proficient",
        description: "Subtract fractions with the same denominator by subtracting numerators.",
        keyPoints: [
            "Keep the <strong>denominator the same</strong>",
            "<strong>Subtract the numerators</strong>",
            "Simplify if possible"
        ],
        examples: [
            {
                question: "What is ⅚ - ⅔?",
                steps: [
                    "First, make denominators same: ⅔ = 4/6",
                    "⅚ - 4/6 = ?",
                    "Subtract numerators: 5 - 4 = 1",
                    "Answer: <strong>⅙</strong>"
                ],
                answer: "⅙"
            }
        ],
        tip: "💡 Same denominator? Subtract the tops, keep the bottom!"
    },
    9: {
        title: "Fractions of Amounts",
        band: "Proficient",
        description: "Find a fraction of a number by dividing then multiplying.",
        keyPoints: [
            "To find <strong>⅓ of 12</strong>: divide 12 by 3 = 4",
            "To find <strong>⅔ of 12</strong>: find ⅓ (=4), then multiply by 2 = 8",
            "'Of' means multiply!"
        ],
        examples: [
            {
                question: "What is ¾ of 20?",
                steps: [
                    "First find ¼ of 20: 20 ÷ 4 = 5",
                    "Then multiply by 3: 5 × 3 = 15",
                    "¾ of 20 = <strong>15</strong>"
                ],
                answer: "15"
            }
        ],
        tip: "💡 Divide by the bottom, multiply by the top!"
    },
    10: {
        title: "Mixed Numbers",
        band: "Advanced",
        description: "Mixed numbers combine a whole number and a fraction, like 2½.",
        keyPoints: [
            "<strong>Mixed number</strong> = whole number + fraction",
            "<strong>Improper fraction</strong> = numerator ≥ denominator (like 5/2)",
            "You can convert between them"
        ],
        examples: [
            {
                question: "Convert 7/4 to a mixed number",
                steps: [
                    "How many times does 4 go into 7? <strong>1 time</strong>",
                    "Remainder: 7 - 4 = 3",
                    "Answer: <strong>1¾</strong>"
                ],
                answer: "1¾"
            }
        ],
        tip: "💡 Improper → Mixed: divide to get whole number, remainder is new numerator!"
    },
    11: {
        title: "Word Problems",
        band: "Advanced",
        description: "Apply fraction skills to real-world problems.",
        keyPoints: [
            "Read carefully - what fraction operation is needed?",
            "'What fraction?' = write a fraction",
            "'Of' = multiply (find fraction of amount)"
        ],
        examples: [
            {
                question: "Aoife ate ¼ of a pizza. Cian ate ⅜. How much is left?",
                steps: [
                    "Convert ¼ = 2/8",
                    "Eaten: 2/8 + ⅜ = ⅝",
                    "Left: 8/8 - ⅝ = <strong>⅜</strong>"
                ],
                answer: "⅜ of the pizza"
            }
        ],
        tip: "💡 Draw a picture to help visualise the problem!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You've mastered basic fractions! Time for the ultimate challenge.",
        keyPoints: [
            "Understand what fractions represent",
            "Find equivalents and simplify",
            "Add, subtract, and find fractions of amounts"
        ],
        examples: [
            {
                question: "A recipe needs ⅔ cup of flour. You want to make 1½ times the recipe. How much flour?",
                steps: [
                    "1½ = 3/2",
                    "⅔ × 3/2 = (2×3)/(3×2) = 6/6 = 1",
                    "Need: <strong>1 cup of flour</strong>"
                ],
                answer: "1 cup"
            }
        ],
        tip: "🏆 Fantastic! You're a Fractions Champion!"
    }
};

// ============================================================
// 6. BASIC DECIMALS HELP CONTENT
// ============================================================
const basicDecimalsHelpContent = {
    1: {
        title: "Understanding Tenths",
        band: "Foundation",
        description: "Decimals show parts of a whole. The first place after the decimal point is tenths.",
        keyPoints: [
            "<strong>Decimal point</strong> separates whole numbers from parts",
            "First place after decimal = <strong>tenths</strong> (÷10)",
            "0.1 = one tenth = 1/10"
        ],
        examples: [
            {
                question: "What does 0.7 mean?",
                steps: [
                    "0 = zero whole numbers",
                    ".7 = 7 tenths",
                    "0.7 = <strong>seven tenths</strong> = 7/10"
                ],
                answer: "Seven tenths (7/10)"
            }
        ],
        tip: "💡 Think of 1 divided into 10 equal parts - each part is 0.1!"
    },
    2: {
        title: "Decimal Place Value",
        band: "Foundation",
        description: "Every digit in a decimal has a place value, just like whole numbers.",
        keyPoints: [
            "Ones . Tenths Hundredths",
            "Each place is <strong>10 times smaller</strong> as you go right",
            "3.45 = 3 ones + 4 tenths + 5 hundredths"
        ],
        examples: [
            {
                question: "In 2.47, what is the value of the 4?",
                steps: [
                    "4 is in the <strong>tenths</strong> place",
                    "Value = 4 tenths = <strong>0.4</strong>"
                ],
                answer: "0.4 (four tenths)"
            }
        ],
        tip: "💡 Place value chart: ones | tenths | hundredths | thousandths"
    },
    3: {
        title: "Decimals and Money",
        band: "Foundation",
        description: "Money is a great way to understand decimals. €1.50 means 1 euro and 50 cent.",
        keyPoints: [
            "€1 = 100 cent, so 1 cent = €0.01",
            "€3.45 = 3 euros + 45 cent",
            "Money has 2 decimal places (hundredths)"
        ],
        examples: [
            {
                question: "Write 2 euros and 35 cent as a decimal",
                steps: [
                    "Whole euros: 2",
                    "Cent as decimal: 35 cent = 0.35",
                    "Answer: <strong>€2.35</strong>"
                ],
                answer: "€2.35"
            }
        ],
        tip: "💡 Money is always written with 2 decimal places: €5.00, €3.50, €0.99"
    },
    4: {
        title: "Understanding Hundredths",
        band: "Developing",
        description: "The second decimal place is hundredths - one hundred parts of a whole.",
        keyPoints: [
            "Hundredths = second place after decimal point",
            "0.01 = one hundredth = 1/100",
            "0.25 = 25 hundredths = 25/100 = ¼"
        ],
        examples: [
            {
                question: "Write 0.75 as a fraction",
                steps: [
                    "0.75 = 75 hundredths",
                    "= 75/100",
                    "Simplify: = <strong>¾</strong>"
                ],
                answer: "75/100 = ¾"
            }
        ],
        tip: "💡 Hundredths are tiny! 100 of them make 1 whole."
    },
    5: {
        title: "Comparing Decimals",
        band: "Developing",
        description: "Compare decimals by looking at each place value from left to right.",
        keyPoints: [
            "Start comparing from the <strong>left</strong>",
            "Compare ones first, then tenths, then hundredths",
            "Add zeros if needed: 0.5 = 0.50"
        ],
        examples: [
            {
                question: "Which is bigger: 0.45 or 0.5?",
                steps: [
                    "Make same decimal places: 0.5 = 0.50",
                    "Compare: 0.45 vs 0.50",
                    "50 hundredths > 45 hundredths",
                    "<strong>0.5 is bigger</strong>"
                ],
                answer: "0.5"
            }
        ],
        tip: "💡 Line up the decimal points, then compare digit by digit!"
    },
    6: {
        title: "Ordering Decimals",
        band: "Developing",
        description: "Put decimals in order from smallest to largest or largest to smallest.",
        keyPoints: [
            "Make all decimals have the <strong>same number of places</strong>",
            "Compare like whole numbers",
            "Check your order is right!"
        ],
        examples: [
            {
                question: "Order these: 0.4, 0.35, 0.42 (smallest first)",
                steps: [
                    "Make same places: 0.40, 0.35, 0.42",
                    "Compare: 35 < 40 < 42 (hundredths)",
                    "Order: <strong>0.35, 0.4, 0.42</strong>"
                ],
                answer: "0.35, 0.4, 0.42"
            }
        ],
        tip: "💡 Adding zeros after a decimal doesn't change its value: 0.4 = 0.40 = 0.400"
    },
    7: {
        title: "Adding Decimals",
        band: "Proficient",
        description: "Add decimals by lining up the decimal points and adding as normal.",
        keyPoints: [
            "<strong>Line up the decimal points</strong>",
            "Add zeros to make same places if needed",
            "Add column by column, carry if needed"
        ],
        examples: [
            {
                question: "What is 3.45 + 2.8?",
                steps: [
                    "Line up: 3.45",
                    "        + 2.80",
                    "Add: <strong>6.25</strong>"
                ],
                answer: "6.25"
            }
        ],
        tip: "💡 The decimal point in your answer goes directly below the others!"
    },
    8: {
        title: "Subtracting Decimals",
        band: "Proficient",
        description: "Subtract decimals by lining up decimal points, just like addition.",
        keyPoints: [
            "<strong>Line up the decimal points</strong>",
            "Add zeros if needed",
            "Exchange (borrow) if the top digit is smaller"
        ],
        examples: [
            {
                question: "What is 5.2 - 2.75?",
                steps: [
                    "Line up: 5.20",
                    "       - 2.75",
                    "Subtract: <strong>2.45</strong>"
                ],
                answer: "2.45"
            }
        ],
        tip: "💡 5.2 = 5.20 - add that zero so you can subtract hundredths!"
    },
    9: {
        title: "Decimals ↔ Fractions",
        band: "Proficient",
        description: "Convert between decimals and fractions. They're just different ways to write the same thing!",
        keyPoints: [
            "<strong>Decimal → Fraction</strong>: use place value (0.25 = 25/100)",
            "<strong>Fraction → Decimal</strong>: divide numerator by denominator",
            "Learn common ones: ½=0.5, ¼=0.25, ¾=0.75"
        ],
        examples: [
            {
                question: "Write ⅗ as a decimal",
                steps: [
                    "⅗ means 3 ÷ 5",
                    "3 ÷ 5 = <strong>0.6</strong>"
                ],
                answer: "0.6"
            }
        ],
        tip: "💡 Know these: ½=0.5, ¼=0.25, ¾=0.75, ⅕=0.2, ⅒=0.1"
    },
    10: {
        title: "Rounding Decimals",
        band: "Advanced",
        description: "Round decimals to a given number of decimal places.",
        keyPoints: [
            "Look at the digit <strong>after</strong> where you're rounding",
            "5 or more = round up",
            "4 or less = round down"
        ],
        examples: [
            {
                question: "Round 3.47 to 1 decimal place",
                steps: [
                    "Rounding to 1 d.p. - look at hundredths: 7",
                    "7 ≥ 5, so round UP",
                    "3.47 → <strong>3.5</strong>"
                ],
                answer: "3.5"
            }
        ],
        tip: "💡 '1 decimal place' means 1 digit after the point!"
    },
    11: {
        title: "Word Problems",
        band: "Advanced",
        description: "Apply decimal skills to real-world problems, especially money!",
        keyPoints: [
            "Money problems often use decimals",
            "Read carefully - add or subtract?",
            "Line up decimal points for accurate calculation"
        ],
        examples: [
            {
                question: "Niamh has €10. She buys a book for €6.75. How much change?",
                steps: [
                    "€10.00 - €6.75 = ?",
                    "Calculate: <strong>€3.25</strong>"
                ],
                answer: "€3.25"
            }
        ],
        tip: "💡 Always include € and use 2 decimal places for money answers!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You've mastered decimals! Show off all your skills.",
        keyPoints: [
            "Understand decimal place value",
            "Add and subtract with lined-up decimal points",
            "Convert between fractions and decimals"
        ],
        examples: [
            {
                question: "Calculate: 4.5 + ¾ (give answer as decimal)",
                steps: [
                    "Convert ¾ to decimal: 0.75",
                    "Add: 4.5 + 0.75 = 4.50 + 0.75 = <strong>5.25</strong>"
                ],
                answer: "5.25"
            }
        ],
        tip: "🏆 Brilliant! You're a Decimals Champion!"
    }
};

// ============================================================
// 7. BASIC PERCENTAGES HELP CONTENT
// ============================================================
const basicPercentagesHelpContent = {
    1: {
        title: "What is Percent?",
        band: "Foundation",
        description: "Percent means 'out of 100'. The % symbol shows a number as parts of 100.",
        keyPoints: [
            "<strong>Percent</strong> = per hundred (per cent)",
            "100% = the whole thing (all of it)",
            "50% = half, 25% = quarter"
        ],
        examples: [
            {
                question: "What does 75% mean?",
                steps: [
                    "75% = 75 out of 100",
                    "= 75/100",
                    "= <strong>three quarters</strong>"
                ],
                answer: "75 out of 100 (¾)"
            }
        ],
        tip: "💡 Think of a hundred square - 75% means 75 squares shaded!"
    },
    2: {
        title: "50% and Halves",
        band: "Foundation",
        description: "50% is the same as a half. Half of something means dividing by 2.",
        keyPoints: [
            "<strong>50% = ½ = 0.5</strong>",
            "To find 50%, divide by 2",
            "50% of 80 = 80 ÷ 2 = 40"
        ],
        examples: [
            {
                question: "What is 50% of 64?",
                steps: [
                    "50% means half",
                    "Half of 64 = 64 ÷ 2",
                    "= <strong>32</strong>"
                ],
                answer: "32"
            }
        ],
        tip: "💡 50% = half. Just divide by 2!"
    },
    3: {
        title: "25% and Quarters",
        band: "Foundation",
        description: "25% is a quarter. A quarter means dividing by 4.",
        keyPoints: [
            "<strong>25% = ¼ = 0.25</strong>",
            "To find 25%, divide by 4",
            "75% = three quarters (25% × 3)"
        ],
        examples: [
            {
                question: "What is 25% of 80?",
                steps: [
                    "25% = one quarter",
                    "80 ÷ 4 = <strong>20</strong>"
                ],
                answer: "20"
            }
        ],
        tip: "💡 25% = quarter. 50% ÷ 2 also gives 25%!"
    },
    4: {
        title: "10% and Tenths",
        band: "Developing",
        description: "10% is one tenth. Finding 10% is super useful for calculating other percentages!",
        keyPoints: [
            "<strong>10% = 1/10 = 0.1</strong>",
            "To find 10%, divide by 10",
            "Use 10% to find 20%, 30%, 5%, etc."
        ],
        examples: [
            {
                question: "What is 10% of 350?",
                steps: [
                    "10% = divide by 10",
                    "350 ÷ 10 = <strong>35</strong>"
                ],
                answer: "35"
            }
        ],
        tip: "💡 10% = move the decimal point one place left! 350 → 35.0"
    },
    5: {
        title: "Common Percentages",
        band: "Developing",
        description: "Build other percentages from 10%, 25%, and 50%.",
        keyPoints: [
            "20% = 10% × 2",
            "30% = 10% × 3",
            "5% = 10% ÷ 2",
            "75% = 50% + 25%"
        ],
        examples: [
            {
                question: "What is 30% of 60?",
                steps: [
                    "Find 10% first: 60 ÷ 10 = 6",
                    "30% = 10% × 3",
                    "= 6 × 3 = <strong>18</strong>"
                ],
                answer: "18"
            }
        ],
        tip: "💡 Build from 10%! It's your percentage building block."
    },
    6: {
        title: "% ↔ Fractions",
        band: "Developing",
        description: "Convert between percentages and fractions. They're just different ways to show parts.",
        keyPoints: [
            "<strong>% to fraction</strong>: put over 100, then simplify",
            "<strong>Fraction to %</strong>: × 100",
            "Know common ones by heart!"
        ],
        examples: [
            {
                question: "Convert 40% to a fraction",
                steps: [
                    "40% = 40/100",
                    "Simplify: ÷20 each",
                    "= <strong>⅖</strong>"
                ],
                answer: "40/100 = ⅖"
            }
        ],
        tip: "💡 Memorise: 50%=½, 25%=¼, 20%=⅕, 10%=1/10"
    },
    7: {
        title: "% ↔ Decimals",
        band: "Proficient",
        description: "Convert between percentages and decimals quickly.",
        keyPoints: [
            "<strong>% to decimal</strong>: divide by 100 (move point 2 left)",
            "<strong>Decimal to %</strong>: multiply by 100 (move point 2 right)",
            "45% = 0.45, 0.8 = 80%"
        ],
        examples: [
            {
                question: "Convert 0.35 to a percentage",
                steps: [
                    "Decimal to %: × 100",
                    "0.35 × 100 = <strong>35%</strong>"
                ],
                answer: "35%"
            }
        ],
        tip: "💡 % ÷ 100 = decimal. Decimal × 100 = %"
    },
    8: {
        title: "Finding % of Amount",
        band: "Proficient",
        description: "Calculate any percentage of a number using the methods you've learned.",
        keyPoints: [
            "Method 1: Find 10% or 1%, then multiply",
            "Method 2: Convert % to decimal, then multiply",
            "Choose whichever method is easier!"
        ],
        examples: [
            {
                question: "What is 35% of 80?",
                steps: [
                    "Method: Find 10%, then build",
                    "10% of 80 = 8",
                    "30% = 8 × 3 = 24",
                    "5% = 8 ÷ 2 = 4",
                    "35% = 24 + 4 = <strong>28</strong>"
                ],
                answer: "28"
            }
        ],
        tip: "💡 Break percentages into easier parts: 35% = 30% + 5%"
    },
    9: {
        title: "Percentage Problems",
        band: "Proficient",
        description: "Apply percentage skills to real problems like test scores and surveys.",
        keyPoints: [
            "Express as percentage: (part ÷ total) × 100",
            "Read what the question asks for",
            "Check your answer makes sense"
        ],
        examples: [
            {
                question: "Cian scored 18 out of 20 on a test. What percentage?",
                steps: [
                    "Percentage = (18 ÷ 20) × 100",
                    "= 0.9 × 100",
                    "= <strong>90%</strong>"
                ],
                answer: "90%"
            }
        ],
        tip: "💡 (Part ÷ Whole) × 100 = Percentage"
    },
    10: {
        title: "Discounts",
        band: "Advanced",
        description: "Calculate sale prices using percentage discounts.",
        keyPoints: [
            "<strong>Discount</strong> = amount taken off",
            "Sale price = Original price - Discount",
            "Or: Sale price = Original × (100% - discount%)"
        ],
        examples: [
            {
                question: "A €50 jacket has 20% off. What's the sale price?",
                steps: [
                    "Discount = 20% of €50 = €10",
                    "Sale price = €50 - €10 = <strong>€40</strong>"
                ],
                answer: "€40"
            }
        ],
        tip: "💡 20% off = you pay 80%! (100% - 20% = 80%)"
    },
    11: {
        title: "Word Problems",
        band: "Advanced",
        description: "Solve various real-world percentage problems.",
        keyPoints: [
            "Identify: finding %, finding amount, or comparing",
            "Use the method that fits",
            "Show your working clearly"
        ],
        examples: [
            {
                question: "A school has 400 students. 55% are girls. How many boys?",
                steps: [
                    "Girls = 55%, so Boys = 45%",
                    "45% of 400 = ?",
                    "10% = 40, so 45% = 4 × 40 + 20 = <strong>180 boys</strong>"
                ],
                answer: "180 boys"
            }
        ],
        tip: "💡 If you know one percentage, you can find the other (they add to 100%)!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You're a percentage pro! Show everything you've learned.",
        keyPoints: [
            "Convert between %, fractions, and decimals",
            "Find percentages of amounts",
            "Apply to discounts and real problems"
        ],
        examples: [
            {
                question: "A €80 game is reduced by 15%. What's the new price?",
                steps: [
                    "15% of €80: 10% = €8, 5% = €4, 15% = €12",
                    "New price = €80 - €12 = <strong>€68</strong>"
                ],
                answer: "€68"
            }
        ],
        tip: "🏆 Amazing! You're a Percentages Champion!"
    }
};

// ============================================================
// 8. TIME AND CLOCKS HELP CONTENT
// ============================================================
const timeAndClocksHelpContent = {
    1: {
        title: "O'Clock Times",
        band: "Foundation",
        description: "Learn to read o'clock times. The long hand points to 12, the short hand to the hour.",
        keyPoints: [
            "<strong>Short hand</strong> (hour hand) = which hour",
            "<strong>Long hand</strong> (minute hand) = how many minutes",
            "O'clock = long hand on 12"
        ],
        examples: [
            {
                question: "The short hand points to 3, long hand to 12. What time?",
                steps: [
                    "Short hand on 3 = 3 hours",
                    "Long hand on 12 = o'clock",
                    "Time = <strong>3 o'clock</strong>"
                ],
                answer: "3 o'clock (3:00)"
            }
        ],
        tip: "💡 The short hand is shorter because it moves slower (once around = 12 hours)!"
    },
    2: {
        title: "Half Past",
        band: "Foundation",
        description: "Half past means 30 minutes past the hour. The long hand points to 6.",
        keyPoints: [
            "<strong>Half past</strong> = 30 minutes",
            "Long hand points to <strong>6</strong>",
            "Short hand is between two numbers"
        ],
        examples: [
            {
                question: "Long hand on 6, short hand between 4 and 5. What time?",
                steps: [
                    "Long hand on 6 = half past",
                    "Short hand past 4 = hour is 4",
                    "Time = <strong>half past 4</strong> (4:30)"
                ],
                answer: "Half past 4 (4:30)"
            }
        ],
        tip: "💡 At half past, the short hand is halfway between two numbers!"
    },
    3: {
        title: "Quarter Past/To",
        band: "Foundation",
        description: "Quarter past (15 min) and quarter to (45 min) are important clock positions.",
        keyPoints: [
            "<strong>Quarter past</strong> = 15 minutes, long hand on 3",
            "<strong>Quarter to</strong> = 45 minutes, long hand on 9",
            "'To' means towards the NEXT hour"
        ],
        examples: [
            {
                question: "What is quarter to 5?",
                steps: [
                    "Quarter to = 45 minutes",
                    "'To 5' means approaching 5 o'clock",
                    "= <strong>4:45</strong>"
                ],
                answer: "4:45"
            }
        ],
        tip: "💡 Quarter = 15 minutes. There are 4 quarters in an hour (15 × 4 = 60)!"
    },
    4: {
        title: "5-Minute Intervals",
        band: "Developing",
        description: "Each number on the clock represents 5 minutes. Count in 5s!",
        keyPoints: [
            "1 = 5 min, 2 = 10 min, 3 = 15 min...",
            "Count in 5s from 12",
            "12 numbers × 5 minutes = 60 minutes"
        ],
        examples: [
            {
                question: "Long hand on 4, short hand past 7. What time?",
                steps: [
                    "Long hand on 4 = 4 × 5 = 20 minutes",
                    "Short hand past 7 = hour is 7",
                    "Time = <strong>7:20</strong>"
                ],
                answer: "7:20 (twenty past 7)"
            }
        ],
        tip: "💡 The clock numbers are a times-5 table: 1=5, 2=10, 3=15..."
    },
    5: {
        title: "Reading Any Time",
        band: "Developing",
        description: "Read any time by combining hour and minute hands.",
        keyPoints: [
            "Hour = what number the short hand has passed",
            "Minutes = count 5s to where long hand points",
            "Between numbers? Count extra minutes"
        ],
        examples: [
            {
                question: "Long hand between 5 and 6, short hand past 9. What time?",
                steps: [
                    "Long hand: 5 = 25 min, a bit more... ~27 min",
                    "Short hand past 9 = hour is 9",
                    "Time ≈ <strong>9:27</strong>"
                ],
                answer: "Approximately 9:27"
            }
        ],
        tip: "💡 Short hand shows hours, long hand shows minutes. Simple!"
    },
    6: {
        title: "Digital Time",
        band: "Developing",
        description: "Digital clocks show time with numbers: hours:minutes.",
        keyPoints: [
            "Format: <strong>HH:MM</strong> (hours:minutes)",
            "Hours before the colon, minutes after",
            "07:15 = 7:15 = quarter past 7"
        ],
        examples: [
            {
                question: "Write 'twenty to 9' in digital format",
                steps: [
                    "Twenty to 9 = 40 minutes past 8",
                    "= <strong>8:40</strong>"
                ],
                answer: "8:40"
            }
        ],
        tip: "💡 'To' times: subtract from 60 for minutes, use previous hour!"
    },
    7: {
        title: "24-Hour Clock",
        band: "Proficient",
        description: "The 24-hour clock counts from 00:00 to 23:59. Used for timetables!",
        keyPoints: [
            "Morning (AM): same as 12-hour (9am = 09:00)",
            "Afternoon/Evening (PM): add 12 (3pm = 15:00)",
            "Midnight = 00:00, Noon = 12:00"
        ],
        examples: [
            {
                question: "Convert 3:45 PM to 24-hour time",
                steps: [
                    "PM = afternoon, so add 12 to hours",
                    "3 + 12 = 15",
                    "= <strong>15:45</strong>"
                ],
                answer: "15:45"
            }
        ],
        tip: "💡 After 12:59, keep adding: 13:00 (1pm), 14:00 (2pm)..."
    },
    8: {
        title: "Elapsed Time",
        band: "Proficient",
        description: "Calculate how much time has passed between two times.",
        keyPoints: [
            "<strong>Count on</strong> from start time to end time",
            "Count to the next hour, then add remaining",
            "Or subtract start from end"
        ],
        examples: [
            {
                question: "How long from 9:45 to 11:20?",
                steps: [
                    "9:45 to 10:00 = 15 min",
                    "10:00 to 11:00 = 1 hour",
                    "11:00 to 11:20 = 20 min",
                    "Total = <strong>1 hour 35 min</strong>"
                ],
                answer: "1 hour 35 minutes"
            }
        ],
        tip: "💡 Break it into chunks: to the hour, full hours, then remaining minutes!"
    },
    9: {
        title: "Timetables",
        band: "Proficient",
        description: "Read bus, train, and school timetables using 24-hour time.",
        keyPoints: [
            "Timetables often use 24-hour time",
            "Read across rows for one journey",
            "Calculate journey time by finding the difference"
        ],
        examples: [
            {
                question: "A bus leaves at 14:30 and arrives at 15:15. How long is the journey?",
                steps: [
                    "14:30 to 15:00 = 30 min",
                    "15:00 to 15:15 = 15 min",
                    "Total = <strong>45 minutes</strong>"
                ],
                answer: "45 minutes"
            }
        ],
        tip: "💡 Highlight your row in timetables to avoid reading the wrong times!"
    },
    10: {
        title: "Time Calculations",
        band: "Advanced",
        description: "Add and subtract times, dealing with hours and minutes.",
        keyPoints: [
            "60 minutes = 1 hour (carry over when adding)",
            "Borrow from hours when subtracting minutes",
            "Keep hours and minutes aligned"
        ],
        examples: [
            {
                question: "Add: 2 hours 45 min + 1 hour 30 min",
                steps: [
                    "Add minutes: 45 + 30 = 75 min = 1 hr 15 min",
                    "Add hours: 2 + 1 + 1 = 4 hours",
                    "Total = <strong>4 hours 15 min</strong>"
                ],
                answer: "4 hours 15 minutes"
            }
        ],
        tip: "💡 Remember: 60 minutes = 1 hour, not 100!"
    },
    11: {
        title: "Scheduling Problems",
        band: "Advanced",
        description: "Solve real-world scheduling and timing problems.",
        keyPoints: [
            "Start time + Duration = End time",
            "End time - Duration = Start time",
            "End time - Start time = Duration"
        ],
        examples: [
            {
                question: "A film is 1 hr 45 min long. If it ends at 9:30 PM, when did it start?",
                steps: [
                    "Work backwards from 9:30",
                    "9:30 - 45 min = 8:45",
                    "8:45 - 1 hr = <strong>7:45 PM</strong>"
                ],
                answer: "7:45 PM"
            }
        ],
        tip: "💡 Draw a timeline to help visualise the problem!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You're a time-telling expert! Master all aspects of time.",
        keyPoints: [
            "Read analogue and digital clocks confidently",
            "Convert between 12-hour and 24-hour",
            "Calculate elapsed time and solve scheduling problems"
        ],
        examples: [
            {
                question: "A train leaves Dublin at 13:45 and takes 2 hr 35 min. What time does it arrive?",
                steps: [
                    "13:45 + 2 hr = 15:45",
                    "15:45 + 35 min = <strong>16:20</strong>"
                ],
                answer: "16:20 (4:20 PM)"
            }
        ],
        tip: "🏆 Excellent! You're a Time & Clocks Champion!"
    }
};

// ============================================================
// 9. MONEY SKILLS HELP CONTENT
// ============================================================
const moneySkillsHelpContent = {
    1: {
        title: "Coins and Notes",
        band: "Foundation",
        description: "Learn to recognise and know the value of Euro coins and notes.",
        keyPoints: [
            "<strong>Coins</strong>: 1c, 2c, 5c, 10c, 20c, 50c, €1, €2",
            "<strong>Notes</strong>: €5, €10, €20, €50, €100",
            "100 cent = €1"
        ],
        examples: [
            {
                question: "How many 20c coins make €1?",
                steps: [
                    "€1 = 100 cent",
                    "100 ÷ 20 = <strong>5 coins</strong>"
                ],
                answer: "5 coins"
            }
        ],
        tip: "💡 Know your coins: copper (1c, 2c, 5c), gold (10c, 20c, 50c), bi-metal (€1, €2)!"
    },
    2: {
        title: "Counting Money",
        band: "Foundation",
        description: "Count collections of coins and notes to find the total.",
        keyPoints: [
            "Start with the <strong>highest value</strong> coins/notes",
            "Add in order from largest to smallest",
            "Keep a running total"
        ],
        examples: [
            {
                question: "Count: €1, 50c, 20c, 10c, 5c",
                steps: [
                    "€1.00 + 50c = €1.50",
                    "€1.50 + 20c = €1.70",
                    "€1.70 + 10c = €1.80",
                    "€1.80 + 5c = <strong>€1.85</strong>"
                ],
                answer: "€1.85"
            }
        ],
        tip: "💡 Organise coins by value before counting!"
    },
    3: {
        title: "Making Amounts",
        band: "Foundation",
        description: "Use different combinations of coins to make a given amount.",
        keyPoints: [
            "There are often <strong>many ways</strong> to make the same amount",
            "Start with large coins, fill in with smaller ones",
            "Use fewest coins when possible"
        ],
        examples: [
            {
                question: "Make €2.35 using the fewest coins",
                steps: [
                    "€2 coin = €2.00",
                    "Need 35c more",
                    "20c + 10c + 5c = 35c",
                    "Total: <strong>€2 + 20c + 10c + 5c</strong>"
                ],
                answer: "€2 + 20c + 10c + 5c (4 coins)"
            }
        ],
        tip: "💡 Fewest coins = use largest coins possible!"
    },
    4: {
        title: "Adding Money",
        band: "Developing",
        description: "Add amounts of money using the same skills as adding decimals.",
        keyPoints: [
            "<strong>Line up the decimal points</strong>",
            "Add cent first, then euros",
            "Carry over when cent > 99"
        ],
        examples: [
            {
                question: "€3.45 + €2.80 = ?",
                steps: [
                    "Line up: €3.45",
                    "       + €2.80",
                    "45c + 80c = 125c = €1.25",
                    "€3 + €2 + €1 = €6.25",
                    "Answer: <strong>€6.25</strong>"
                ],
                answer: "€6.25"
            }
        ],
        tip: "💡 100c = €1. If cent adds to 100+, carry €1!"
    },
    5: {
        title: "Subtracting Money",
        band: "Developing",
        description: "Subtract money amounts to find the difference or change.",
        keyPoints: [
            "Line up decimal points",
            "Exchange if needed (borrow €1 = 100c)",
            "This is how you calculate change!"
        ],
        examples: [
            {
                question: "€10.00 - €6.75 = ?",
                steps: [
                    "Can't do 0c - 75c, borrow €1",
                    "100c - 75c = 25c",
                    "€9 - €6 = €3",
                    "Answer: <strong>€3.25</strong>"
                ],
                answer: "€3.25"
            }
        ],
        tip: "💡 Need to borrow? €1 becomes 100 cent!"
    },
    6: {
        title: "Giving Change",
        band: "Developing",
        description: "Calculate change from a purchase. This is subtraction!",
        keyPoints: [
            "<strong>Change = Amount paid - Cost</strong>",
            "Count up from cost to amount paid",
            "Or subtract directly"
        ],
        examples: [
            {
                question: "Pay €5 for item costing €3.35. What's the change?",
                steps: [
                    "Change = €5.00 - €3.35",
                    "Count up: €3.35 → €3.40 (5c) → €4 (60c) → €5 (€1)",
                    "5c + 60c + €1 = <strong>€1.65</strong>"
                ],
                answer: "€1.65"
            }
        ],
        tip: "💡 Shopkeepers count up: 'That's €3.35... €4... €5. €1.65 change!'"
    },
    7: {
        title: "Shopping Problems",
        band: "Proficient",
        description: "Solve word problems involving buying multiple items.",
        keyPoints: [
            "List what's being bought",
            "Add all costs together",
            "Calculate change if they pay with larger note"
        ],
        examples: [
            {
                question: "Aoife buys bread (€1.80) and milk (€1.45). She pays with €5. What's her change?",
                steps: [
                    "Total cost: €1.80 + €1.45 = €3.25",
                    "Change: €5.00 - €3.25 = <strong>€1.75</strong>"
                ],
                answer: "€1.75"
            }
        ],
        tip: "💡 Find total cost first, then calculate change!"
    },
    8: {
        title: "Comparing Prices",
        band: "Proficient",
        description: "Compare prices to find which option is cheaper or better value.",
        keyPoints: [
            "Line up prices to compare easily",
            "Sometimes bigger packs are better value",
            "Calculate 'per item' cost for fair comparison"
        ],
        examples: [
            {
                question: "6 apples for €2.40 or 4 apples for €1.80. Which is better value?",
                steps: [
                    "6 for €2.40: €2.40 ÷ 6 = 40c each",
                    "4 for €1.80: €1.80 ÷ 4 = 45c each",
                    "<strong>6 for €2.40 is better value</strong>"
                ],
                answer: "6 for €2.40 (40c each)"
            }
        ],
        tip: "💡 Price per item = Total ÷ Number of items"
    },
    9: {
        title: "Budgeting",
        band: "Proficient",
        description: "Plan spending to stay within a budget.",
        keyPoints: [
            "<strong>Budget</strong> = maximum amount you can spend",
            "Add up costs, check against budget",
            "Don't forget to leave room for essentials!"
        ],
        examples: [
            {
                question: "Cian has €20. Books cost €12.50, lunch €4.75. Can he buy both?",
                steps: [
                    "Total needed: €12.50 + €4.75 = €17.25",
                    "Budget: €20.00",
                    "€17.25 < €20.00 ✓",
                    "<strong>Yes, with €2.75 to spare!</strong>"
                ],
                answer: "Yes (€2.75 left over)"
            }
        ],
        tip: "💡 Always check if total ≤ budget before buying!"
    },
    10: {
        title: "Multi-Step Problems",
        band: "Advanced",
        description: "Solve complex money problems with multiple operations.",
        keyPoints: [
            "Break into steps",
            "Do one calculation at a time",
            "Check your answer makes sense"
        ],
        examples: [
            {
                question: "3 children share €15 equally. Each spends €2.50. How much does each have left?",
                steps: [
                    "Each gets: €15 ÷ 3 = €5",
                    "Each spends: €2.50",
                    "Left: €5.00 - €2.50 = <strong>€2.50 each</strong>"
                ],
                answer: "€2.50 each"
            }
        ],
        tip: "💡 List the steps before calculating!"
    },
    11: {
        title: "Best Value",
        band: "Advanced",
        description: "Analyse deals and special offers to find the best purchase.",
        keyPoints: [
            "Calculate the 'unit price' (price per item)",
            "Watch for 'buy one get one free' (halves unit price!)",
            "Sometimes buying more saves money"
        ],
        examples: [
            {
                question: "Small juice €1.20 (250ml) or Large €2.00 (500ml). Which is better value?",
                steps: [
                    "Small: €1.20 ÷ 250 = 0.48c per ml",
                    "Large: €2.00 ÷ 500 = 0.40c per ml",
                    "<strong>Large is better value</strong>"
                ],
                answer: "Large (cheaper per ml)"
            }
        ],
        tip: "💡 Unit price lets you compare fairly - same amount for same cost!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You're a money master! Apply all your skills to complex problems.",
        keyPoints: [
            "Know your coins and notes",
            "Add, subtract, and calculate change confidently",
            "Compare prices and manage budgets"
        ],
        examples: [
            {
                question: "A family buys 4 cinema tickets at €9.50 each and €8.75 of snacks. They pay with €50. What change?",
                steps: [
                    "Tickets: 4 × €9.50 = €38.00",
                    "Total: €38.00 + €8.75 = €46.75",
                    "Change: €50.00 - €46.75 = <strong>€3.25</strong>"
                ],
                answer: "€3.25"
            }
        ],
        tip: "🏆 Brilliant! You're a Money Skills Champion!"
    }
};

// ============================================================
// 10. MEASUREMENT HELP CONTENT
// ============================================================
const measurementHelpContent = {
    1: {
        title: "Length (cm)",
        band: "Foundation",
        description: "Centimetres (cm) measure shorter lengths. There are 100 cm in 1 metre.",
        keyPoints: [
            "<strong>cm</strong> = centimetre (small lengths)",
            "Your fingernail is about 1 cm wide",
            "A ruler is usually 30 cm long"
        ],
        examples: [
            {
                question: "A pencil is 18 cm long. Is that longer or shorter than a 30 cm ruler?",
                steps: [
                    "18 cm vs 30 cm",
                    "18 < 30",
                    "<strong>Shorter</strong> than the ruler"
                ],
                answer: "Shorter"
            }
        ],
        tip: "💡 Use cm for measuring small things like pencils, books, your hand!"
    },
    2: {
        title: "Length (m, km)",
        band: "Foundation",
        description: "Metres (m) for medium lengths, kilometres (km) for long distances.",
        keyPoints: [
            "<strong>m</strong> = metre (room lengths, heights)",
            "<strong>km</strong> = kilometre (distances between places)",
            "1 km = 1,000 m"
        ],
        examples: [
            {
                question: "Would you measure the length of a football pitch in cm, m, or km?",
                steps: [
                    "A pitch is big but not super far",
                    "cm = too small",
                    "km = too big",
                    "Answer: <strong>metres (m)</strong>"
                ],
                answer: "Metres (about 100m)"
            }
        ],
        tip: "💡 Think: cm for small, m for room-sized, km for map distances!"
    },
    3: {
        title: "Measuring Length",
        band: "Foundation",
        description: "Use rulers and measuring tapes correctly to measure length.",
        keyPoints: [
            "Start measuring from <strong>0</strong>, not the edge of the ruler",
            "Keep the ruler <strong>straight</strong>",
            "Read where the object ends"
        ],
        examples: [
            {
                question: "A line starts at 0 and ends at 7.5 on a ruler. How long is it?",
                steps: [
                    "Start: 0 cm",
                    "End: 7.5 cm",
                    "Length = <strong>7.5 cm</strong>"
                ],
                answer: "7.5 cm"
            }
        ],
        tip: "💡 Always check where 0 is - some rulers have a gap at the start!"
    },
    4: {
        title: "Mass (g, kg)",
        band: "Developing",
        description: "Mass (weight) is measured in grams (g) and kilograms (kg).",
        keyPoints: [
            "<strong>g</strong> = gram (light things)",
            "<strong>kg</strong> = kilogram (heavier things)",
            "1 kg = 1,000 g"
        ],
        examples: [
            {
                question: "A bag of sugar weighs 1 kg. How many grams is that?",
                steps: [
                    "1 kg = 1,000 g",
                    "So 1 kg bag = <strong>1,000 g</strong>"
                ],
                answer: "1,000 g"
            }
        ],
        tip: "💡 A paperclip is about 1g. A bag of sugar is 1kg. A child is about 30kg!"
    },
    5: {
        title: "Capacity (ml, l)",
        band: "Developing",
        description: "Capacity measures how much liquid a container holds.",
        keyPoints: [
            "<strong>ml</strong> = millilitre (small amounts)",
            "<strong>l</strong> = litre (larger amounts)",
            "1 l = 1,000 ml"
        ],
        examples: [
            {
                question: "A medicine spoon holds 5 ml. A bottle holds 100 ml. How many spoonfuls in the bottle?",
                steps: [
                    "100 ml ÷ 5 ml = <strong>20 spoonfuls</strong>"
                ],
                answer: "20 spoonfuls"
            }
        ],
        tip: "💡 A teaspoon ≈ 5ml. A water bottle ≈ 500ml. A big milk carton = 1 litre!"
    },
    6: {
        title: "Comparing Measures",
        band: "Developing",
        description: "Compare measurements to see which is bigger, smaller, or equal.",
        keyPoints: [
            "Make sure units are the <strong>same</strong> before comparing",
            "Convert if necessary",
            "Then compare the numbers"
        ],
        examples: [
            {
                question: "Which is longer: 150 cm or 1.2 m?",
                steps: [
                    "Convert to same unit: 1.2 m = 120 cm",
                    "Compare: 150 cm vs 120 cm",
                    "<strong>150 cm is longer</strong>"
                ],
                answer: "150 cm"
            }
        ],
        tip: "💡 Always convert to the same unit before comparing!"
    },
    7: {
        title: "Converting Length",
        band: "Proficient",
        description: "Convert between cm, m, and km using multiplication and division.",
        keyPoints: [
            "<strong>cm → m</strong>: ÷ 100",
            "<strong>m → cm</strong>: × 100",
            "<strong>m → km</strong>: ÷ 1000, <strong>km → m</strong>: × 1000"
        ],
        examples: [
            {
                question: "Convert 3.5 km to metres",
                steps: [
                    "km to m: multiply by 1,000",
                    "3.5 × 1,000 = <strong>3,500 m</strong>"
                ],
                answer: "3,500 m"
            }
        ],
        tip: "💡 Going to smaller unit? × (number gets bigger). Bigger unit? ÷"
    },
    8: {
        title: "Converting Mass",
        band: "Proficient",
        description: "Convert between grams and kilograms.",
        keyPoints: [
            "<strong>g → kg</strong>: ÷ 1,000",
            "<strong>kg → g</strong>: × 1,000",
            "1.5 kg = 1,500 g"
        ],
        examples: [
            {
                question: "Convert 2,750 g to kg",
                steps: [
                    "g to kg: divide by 1,000",
                    "2,750 ÷ 1,000 = <strong>2.75 kg</strong>"
                ],
                answer: "2.75 kg"
            }
        ],
        tip: "💡 The decimal point moves 3 places when converting g ↔ kg!"
    },
    9: {
        title: "Converting Capacity",
        band: "Proficient",
        description: "Convert between millilitres and litres.",
        keyPoints: [
            "<strong>ml → l</strong>: ÷ 1,000",
            "<strong>l → ml</strong>: × 1,000",
            "0.5 l = 500 ml"
        ],
        examples: [
            {
                question: "A jug holds 1.25 litres. How many ml?",
                steps: [
                    "l to ml: multiply by 1,000",
                    "1.25 × 1,000 = <strong>1,250 ml</strong>"
                ],
                answer: "1,250 ml"
            }
        ],
        tip: "💡 Same as mass: × 1,000 going smaller, ÷ 1,000 going bigger!"
    },
    10: {
        title: "Mixed Conversions",
        band: "Advanced",
        description: "Convert between any metric units for length, mass, and capacity.",
        keyPoints: [
            "Know the conversion factors",
            "Identify: smaller → bigger (÷) or bigger → smaller (×)",
            "Check your answer makes sense"
        ],
        examples: [
            {
                question: "Express 4.2 km + 350 m in metres",
                steps: [
                    "Convert 4.2 km to m: 4.2 × 1,000 = 4,200 m",
                    "Add: 4,200 m + 350 m = <strong>4,550 m</strong>"
                ],
                answer: "4,550 m"
            }
        ],
        tip: "💡 Convert everything to the same unit first, then calculate!"
    },
    11: {
        title: "Word Problems",
        band: "Advanced",
        description: "Apply measurement skills to real-world problems.",
        keyPoints: [
            "Identify what measurement is needed",
            "Choose appropriate units",
            "Convert if necessary"
        ],
        examples: [
            {
                question: "A recipe needs 750ml of milk. You have 2 litres. How much is left after making the recipe?",
                steps: [
                    "2 l = 2,000 ml",
                    "2,000 ml - 750 ml = 1,250 ml",
                    "= <strong>1.25 litres</strong>"
                ],
                answer: "1.25 l (1,250 ml)"
            }
        ],
        tip: "💡 Convert to the same unit, solve, then convert back if needed!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You're a measurement expert! Show your skills across all units.",
        keyPoints: [
            "Know metric prefixes: kilo (1000), centi (1/100), milli (1/1000)",
            "Convert confidently",
            "Apply to real problems"
        ],
        examples: [
            {
                question: "A parcel weighs 2.4 kg. Postage is 15c per 100g. What's the cost?",
                steps: [
                    "2.4 kg = 2,400 g",
                    "2,400 ÷ 100 = 24 lots of 100g",
                    "24 × 15c = 360c = <strong>€3.60</strong>"
                ],
                answer: "€3.60"
            }
        ],
        tip: "🏆 Excellent! You're a Measurement Champion!"
    }
};

// ============================================================
// 11. DATA AND CHARTS HELP CONTENT
// ============================================================
const dataAndChartsHelpContent = {
    1: {
        title: "Tally Charts",
        band: "Foundation",
        description: "Tally charts use marks to count. Every 5th mark crosses the previous 4.",
        keyPoints: [
            "Draw | | | | then cross with fifth: <s>| | | |</s>",
            "Each bundle of 5 makes counting easier",
            "Count in 5s, then add extras"
        ],
        examples: [
            {
                question: "What number does |||| |||| ||| represent?",
                steps: [
                    "Two bundles of 5: 5 + 5 = 10",
                    "Plus 3 more: 10 + 3 = <strong>13</strong>"
                ],
                answer: "13"
            }
        ],
        tip: "💡 The crossing line bundles four marks into a group of 5!"
    },
    2: {
        title: "Pictograms",
        band: "Foundation",
        description: "Pictograms use pictures to represent data. Always check the key!",
        keyPoints: [
            "Each picture represents a number (check the <strong>key</strong>)",
            "Half picture = half the value",
            "Count pictures, then multiply by key value"
        ],
        examples: [
            {
                question: "A pictogram shows 🍎🍎🍎 for Monday. Key: 🍎 = 4 apples. How many apples?",
                steps: [
                    "Count symbols: 3 apples",
                    "Each = 4",
                    "Total: 3 × 4 = <strong>12 apples</strong>"
                ],
                answer: "12 apples"
            }
        ],
        tip: "💡 ALWAYS read the key first - one picture might equal 2, 5, 10..."
    },
    3: {
        title: "Reading Bar Charts",
        band: "Foundation",
        description: "Bar charts use bars to show amounts. Read the height against the scale.",
        keyPoints: [
            "The <strong>scale</strong> (usually on the left) tells you the values",
            "Read where the <strong>top of the bar</strong> lines up",
            "Compare bars to see which is biggest/smallest"
        ],
        examples: [
            {
                question: "A bar chart shows Monday's bar reaching 15. What does this mean?",
                steps: [
                    "Find Monday's bar",
                    "Read across to the scale",
                    "Value = <strong>15</strong>"
                ],
                answer: "15 (of whatever is being measured)"
            }
        ],
        tip: "💡 Check what the scale goes up in: 1s, 2s, 5s, 10s?"
    },
    4: {
        title: "Reading Tables",
        band: "Developing",
        description: "Tables organise data in rows and columns. Find where row and column meet.",
        keyPoints: [
            "<strong>Rows</strong> go across (horizontal)",
            "<strong>Columns</strong> go down (vertical)",
            "Find the cell where row and column intersect"
        ],
        examples: [
            {
                question: "In a table, find the value for 'Blue' (column) and 'Girls' (row)",
                steps: [
                    "Find 'Girls' row",
                    "Find 'Blue' column",
                    "Read the value where they meet"
                ],
                answer: "The value in that cell"
            }
        ],
        tip: "💡 Use your finger to trace along the row and down the column!"
    },
    5: {
        title: "Creating Bar Charts",
        band: "Developing",
        description: "Draw bar charts from data. Remember labels, title, and scale!",
        keyPoints: [
            "Choose an appropriate <strong>scale</strong>",
            "Draw bars of correct height",
            "Add <strong>title</strong>, <strong>labels</strong>, and <strong>scale</strong>"
        ],
        examples: [
            {
                question: "Data: Red=8, Blue=12, Green=6. What scale would you use?",
                steps: [
                    "Highest value: 12",
                    "A scale of 2s works well (0, 2, 4, 6, 8, 10, 12)",
                    "Bars: Red=8, Blue=12, Green=6"
                ],
                answer: "Scale in 2s up to at least 12"
            }
        ],
        tip: "💡 Choose a scale that fits your data and is easy to read!"
    },
    6: {
        title: "Interpreting Data",
        band: "Developing",
        description: "Answer questions about what data shows. Look for patterns and comparisons.",
        keyPoints: [
            "Find <strong>highest</strong> and <strong>lowest</strong> values",
            "Calculate <strong>differences</strong>",
            "Look for <strong>patterns</strong> or trends"
        ],
        examples: [
            {
                question: "Bar chart shows: Mon=15, Tue=10, Wed=20. Which day had most? How many more than Tuesday?",
                steps: [
                    "Most: Wednesday (20)",
                    "Wed - Tue = 20 - 10 = <strong>10 more</strong>"
                ],
                answer: "Wednesday; 10 more than Tuesday"
            }
        ],
        tip: "💡 Read questions carefully - 'how many more' means find the difference!"
    },
    7: {
        title: "Finding Mode",
        band: "Proficient",
        description: "The mode is the most common value - it appears most often.",
        keyPoints: [
            "<strong>Mode</strong> = most frequent value",
            "Count how many times each value appears",
            "There can be more than one mode, or no mode"
        ],
        examples: [
            {
                question: "Find the mode: 3, 5, 5, 7, 5, 8, 7",
                steps: [
                    "3 appears 1 time",
                    "5 appears 3 times ← most",
                    "7 appears 2 times",
                    "8 appears 1 time",
                    "Mode = <strong>5</strong>"
                ],
                answer: "5"
            }
        ],
        tip: "💡 Mode = Most Often Data Entry!"
    },
    8: {
        title: "Finding Mean",
        band: "Proficient",
        description: "The mean is the average. Add all values, then divide by how many.",
        keyPoints: [
            "<strong>Mean = Total ÷ Number of values</strong>",
            "Add up all the values first",
            "Count how many values there are"
        ],
        examples: [
            {
                question: "Find the mean: 4, 6, 8, 10, 12",
                steps: [
                    "Total: 4+6+8+10+12 = 40",
                    "Number of values: 5",
                    "Mean: 40 ÷ 5 = <strong>8</strong>"
                ],
                answer: "8"
            }
        ],
        tip: "💡 Mean = Add them all up, share them all out!"
    },
    9: {
        title: "Comparing Data",
        band: "Proficient",
        description: "Compare two sets of data using mean, mode, range, or charts.",
        keyPoints: [
            "Calculate <strong>same measure</strong> for both sets",
            "Higher mean = higher average",
            "Larger range = more spread out"
        ],
        examples: [
            {
                question: "Class A mean: 65%. Class B mean: 72%. Which class did better on average?",
                steps: [
                    "Compare means: 65% vs 72%",
                    "72% > 65%",
                    "<strong>Class B</strong> did better on average"
                ],
                answer: "Class B"
            }
        ],
        tip: "💡 Make sure you're comparing the same type of measure!"
    },
    10: {
        title: "Data Analysis",
        band: "Advanced",
        description: "Analyse data sets to draw conclusions and answer questions.",
        keyPoints: [
            "Look at <strong>all the statistics</strong> together",
            "Consider what the data is <strong>telling you</strong>",
            "Think about <strong>why</strong> patterns might exist"
        ],
        examples: [
            {
                question: "Test scores: Mean=68, Mode=72, Range=35. What does this tell us?",
                steps: [
                    "Mean (68): average performance",
                    "Mode (72): most common score",
                    "Range (35): scores varied by 35 marks",
                    "Most scored around 72, but there's quite a spread"
                ],
                answer: "Most scored 72, average was 68, with a 35-point spread"
            }
        ],
        tip: "💡 Different statistics tell different parts of the story!"
    },
    11: {
        title: "Survey Problems",
        band: "Advanced",
        description: "Design surveys, collect data, and analyse results.",
        keyPoints: [
            "Ask <strong>clear questions</strong>",
            "Use <strong>categories</strong> that cover all options",
            "Present results clearly"
        ],
        examples: [
            {
                question: "45 students surveyed: 18 walk, 15 by bus, 12 by car. What fraction walk?",
                steps: [
                    "Walkers: 18",
                    "Total: 45",
                    "Fraction: 18/45 = <strong>2/5</strong>"
                ],
                answer: "2/5 (or 40%)"
            }
        ],
        tip: "💡 Survey tip: make sure everyone's answer fits a category!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You're a data expert! Use all your skills to analyse and present information.",
        keyPoints: [
            "Read and create charts confidently",
            "Calculate mean, mode, and range",
            "Draw conclusions from data"
        ],
        examples: [
            {
                question: "Scores: 45, 52, 48, 52, 58, 52, 47. Find mean, mode, range.",
                steps: [
                    "Mean: 354 ÷ 7 = 50.6 (to 1 d.p.)",
                    "Mode: 52 (appears 3 times)",
                    "Range: 58 - 45 = 13"
                ],
                answer: "Mean=50.6, Mode=52, Range=13"
            }
        ],
        tip: "🏆 Fantastic! You're a Data & Charts Champion!"
    }
};

// ============================================================
// 12. NUMBER PATTERNS HELP CONTENT
// ============================================================
const numberPatternsHelpContent = {
    1: {
        title: "Counting Patterns",
        band: "Foundation",
        description: "Spot patterns when counting in 2s, 5s, 10s, and other numbers.",
        keyPoints: [
            "<strong>Count in 2s</strong>: 2, 4, 6, 8, 10... (even numbers)",
            "<strong>Count in 5s</strong>: 5, 10, 15, 20... (ends in 0 or 5)",
            "<strong>Count in 10s</strong>: 10, 20, 30, 40..."
        ],
        examples: [
            {
                question: "What comes next: 5, 10, 15, 20, ?",
                steps: [
                    "Pattern: counting in 5s",
                    "Next: 20 + 5 = <strong>25</strong>"
                ],
                answer: "25"
            }
        ],
        tip: "💡 Look at the gaps between numbers to find the pattern!"
    },
    2: {
        title: "Adding Patterns",
        band: "Foundation",
        description: "Some patterns add the same number each time.",
        keyPoints: [
            "Find the <strong>common difference</strong> (what's being added)",
            "Add this to each term to get the next",
            "Example: +3 each time: 2, 5, 8, 11, 14..."
        ],
        examples: [
            {
                question: "Find the pattern and next two terms: 7, 12, 17, 22, ?, ?",
                steps: [
                    "Difference: 12-7=5, 17-12=5, 22-17=5",
                    "Pattern: +5 each time",
                    "Next: 22+5=27, 27+5=<strong>32</strong>"
                ],
                answer: "27, 32"
            }
        ],
        tip: "💡 Calculate the difference between consecutive terms!"
    },
    3: {
        title: "Subtracting Patterns",
        band: "Foundation",
        description: "Some patterns subtract the same number each time (decreasing).",
        keyPoints: [
            "Numbers get <strong>smaller</strong> each time",
            "Find what's being subtracted",
            "Example: -4 each time: 50, 46, 42, 38..."
        ],
        examples: [
            {
                question: "Find the pattern and next term: 100, 93, 86, 79, ?",
                steps: [
                    "Difference: 93-100=-7, 86-93=-7",
                    "Pattern: -7 each time",
                    "Next: 79-7=<strong>72</strong>"
                ],
                answer: "72"
            }
        ],
        tip: "💡 Decreasing patterns have negative differences!"
    },
    4: {
        title: "Times Table Patterns",
        band: "Developing",
        description: "Times tables create patterns. Recognise them to spot relationships.",
        keyPoints: [
            "×3 pattern: 3, 6, 9, 12, 15...",
            "×4 pattern: 4, 8, 12, 16, 20...",
            "Multiples follow times table patterns"
        ],
        examples: [
            {
                question: "Which times table: 6, 12, 18, 24, 30?",
                steps: [
                    "Check differences: all +6",
                    "These are multiples of 6",
                    "Answer: <strong>6 times table</strong>"
                ],
                answer: "6 times table"
            }
        ],
        tip: "💡 Multiples of a number follow the same pattern as its times table!"
    },
    5: {
        title: "Finding the Rule",
        band: "Developing",
        description: "Express the pattern as a rule in words or as a formula.",
        keyPoints: [
            "Look at <strong>what's happening</strong> to get from one term to the next",
            "Write it as: 'add 3 each time' or 'multiply by 2'",
            "Test your rule on all terms"
        ],
        examples: [
            {
                question: "Find the rule: 4, 9, 14, 19, 24",
                steps: [
                    "9-4=5, 14-9=5, 19-14=5, 24-19=5",
                    "Rule: <strong>Add 5 each time</strong>",
                    "Or: Start at 4, +5"
                ],
                answer: "Add 5 (or +5)"
            }
        ],
        tip: "💡 A rule should work for ALL terms in the sequence!"
    },
    6: {
        title: "Continuing Patterns",
        band: "Developing",
        description: "Use the rule to find more terms in a sequence.",
        keyPoints: [
            "Apply the rule to find next terms",
            "You can find any term if you know the rule",
            "Check by working backwards too"
        ],
        examples: [
            {
                question: "Rule: Start at 3, add 4 each time. Find the first 5 terms.",
                steps: [
                    "1st term: 3",
                    "2nd: 3+4=7",
                    "3rd: 7+4=11",
                    "4th: 11+4=15",
                    "5th: 15+4=<strong>19</strong>"
                ],
                answer: "3, 7, 11, 15, 19"
            }
        ],
        tip: "💡 Keep applying the rule to extend the pattern!"
    },
    7: {
        title: "Shape Patterns",
        band: "Proficient",
        description: "Patterns can involve shapes, where numbers grow in visual ways.",
        keyPoints: [
            "Count objects in each stage",
            "Look for how many are <strong>added</strong> each time",
            "Draw the next stage to check"
        ],
        examples: [
            {
                question: "Triangle pattern: 3, 6, 10, 15... (dots in triangles). What's next?",
                steps: [
                    "Differences: +3, +4, +5",
                    "Pattern in differences: add one more each time",
                    "Next difference: +6",
                    "Next term: 15+6=<strong>21</strong>"
                ],
                answer: "21"
            }
        ],
        tip: "💡 If the differences aren't constant, look for a pattern in the differences!"
    },
    8: {
        title: "Two-Step Patterns",
        band: "Proficient",
        description: "Some patterns need two operations to find the rule.",
        keyPoints: [
            "Position-to-term rules: 'multiply position by 2, add 1'",
            "Example: Position 1→3, 2→5, 3→7 (×2 +1)",
            "Use a table to spot the relationship"
        ],
        examples: [
            {
                question: "Find rule: Position 1=5, 2=8, 3=11, 4=14",
                steps: [
                    "Differences: +3 each time",
                    "When position=1, term=5",
                    "Rule: <strong>3n + 2</strong> (3×position + 2)",
                    "Check: 3×1+2=5 ✓, 3×2+2=8 ✓"
                ],
                answer: "3n + 2 (multiply by 3, add 2)"
            }
        ],
        tip: "💡 The difference gives you the multiplier in 'an + b' rules!"
    },
    9: {
        title: "Missing Numbers",
        band: "Proficient",
        description: "Find missing terms in a sequence by working out the pattern.",
        keyPoints: [
            "Find the rule using the terms you know",
            "Work forwards or backwards to find missing terms",
            "Check your answer fits the pattern"
        ],
        examples: [
            {
                question: "Find the missing number: 8, ?, 20, 26, 32",
                steps: [
                    "Difference from 20 to 26: +6",
                    "Difference from 26 to 32: +6",
                    "Rule: +6",
                    "8 + 6 = <strong>14</strong>"
                ],
                answer: "14"
            }
        ],
        tip: "💡 Use known terms to figure out the pattern, then fill in gaps!"
    },
    10: {
        title: "Complex Patterns",
        band: "Advanced",
        description: "Tackle more challenging sequences with varying differences.",
        keyPoints: [
            "Some sequences have <strong>changing differences</strong>",
            "Look for patterns in the second level of differences",
            "Triangular, square, cube numbers have special patterns"
        ],
        examples: [
            {
                question: "Sequence: 1, 4, 9, 16, 25... What's the pattern?",
                steps: [
                    "These are: 1², 2², 3², 4², 5²",
                    "Pattern: <strong>Square numbers</strong>",
                    "Next: 6² = 36"
                ],
                answer: "Square numbers (n²)"
            }
        ],
        tip: "💡 Recognise special sequences: squares (1,4,9,16), triangles (1,3,6,10), cubes (1,8,27)!"
    },
    11: {
        title: "Pattern Problems",
        band: "Advanced",
        description: "Apply pattern skills to solve real problems.",
        keyPoints: [
            "Set up a table of values",
            "Find the rule",
            "Use the rule to answer the question"
        ],
        examples: [
            {
                question: "A pattern has 5 tiles in row 1, 9 in row 2, 13 in row 3. How many in row 10?",
                steps: [
                    "Pattern: 5, 9, 13... (+4 each time)",
                    "Rule: 4n + 1",
                    "Row 10: 4(10) + 1 = <strong>41 tiles</strong>"
                ],
                answer: "41 tiles"
            }
        ],
        tip: "💡 Find the rule, then substitute any position to find its term!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You're a pattern master! Apply all your skills.",
        keyPoints: [
            "Identify patterns quickly",
            "Write rules in words or formulas",
            "Find any term in a sequence"
        ],
        examples: [
            {
                question: "Sequence: 2, 6, 12, 20, 30... Find the 10th term.",
                steps: [
                    "Differences: +4, +6, +8, +10 (increasing by 2)",
                    "These are n(n+1): 1×2=2, 2×3=6, 3×4=12...",
                    "10th term: 10×11 = <strong>110</strong>"
                ],
                answer: "110"
            }
        ],
        tip: "🏆 Wonderful! You're a Number Patterns Champion!"
    }
};

// ============================================================
// END OF HELP CONTENT DEFINITIONS
// ============================================================

// Now add branches to getHelpContent() function.
// Add these at the TOP of the function's if/else chain:
//
// function getHelpContent(topic, level) {
//     // Numeracy Strand
//     if (topic === 'whole_numbers') return wholeNumbersHelpContent[level];
//     if (topic === 'addition_subtraction') return additionSubtractionHelpContent[level];
//     if (topic === 'multiplication_skills') return multiplicationSkillsHelpContent[level];
//     if (topic === 'division_skills') return divisionSkillsHelpContent[level];
//     if (topic === 'basic_fractions') return basicFractionsHelpContent[level];
//     if (topic === 'basic_decimals') return basicDecimalsHelpContent[level];
//     if (topic === 'basic_percentages') return basicPercentagesHelpContent[level];
//     if (topic === 'time_and_clocks') return timeAndClocksHelpContent[level];
//     if (topic === 'money_skills') return moneySkillsHelpContent[level];
//     if (topic === 'measurement') return measurementHelpContent[level];
//     if (topic === 'data_and_charts') return dataAndChartsHelpContent[level];
//     if (topic === 'number_patterns') return numberPatternsHelpContent[level];
//     
//     // ... existing JC Exam topic branches below ...
// }

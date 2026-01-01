#!/bin/bash
# Resources Category Column Migration
# Run this on PythonAnywhere in a Bash console

echo "=== Adding category column to additional_resources table ==="

# Path to your database - adjust if different
DB_PATH="/home/bbsisk/mathappR12/instance/mathquiz.db"

# Check if column already exists
echo "Checking if category column exists..."
COLUMN_EXISTS=$(sqlite3 "$DB_PATH" "PRAGMA table_info(additional_resources);" | grep -c "category")

if [ "$COLUMN_EXISTS" -gt 0 ]; then
    echo "✓ Category column already exists!"
else
    echo "Adding category column..."
    sqlite3 "$DB_PATH" "ALTER TABLE additional_resources ADD COLUMN category VARCHAR(50) DEFAULT '';"
    
    if [ $? -eq 0 ]; then
        echo "✓ Category column added successfully!"
    else
        echo "✗ Error adding column"
        exit 1
    fi
fi

# Verify the column was added
echo ""
echo "=== Current table structure ==="
sqlite3 "$DB_PATH" "PRAGMA table_info(additional_resources);"

echo ""
echo "=== Current resources ==="
sqlite3 "$DB_PATH" "SELECT id, button_text, category FROM additional_resources;"

echo ""
echo "=== Migration complete! ==="
echo ""
echo "Next steps:"
echo "1. Upload the updated app.py"
echo "2. Reload the web app"
echo "3. Use Admin → Resources to assign categories to each resource"
echo ""
echo "Category values to use:"
echo "  - maths_awareness  (🧠 Maths Awareness)"
echo "  - workbooks        (📚 Maths WorkBooks)"
echo "  - worksheets       (📝 Proficiency Building - Worksheet)"
echo "  - exam_papers      (📋 Past Exam Paper and Exam Technique)"

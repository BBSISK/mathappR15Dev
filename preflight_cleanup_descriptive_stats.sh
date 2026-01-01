#!/bin/bash
# ============================================================
# PRE-FLIGHT CLEANUP SCRIPT FOR DESCRIPTIVE STATISTICS
# Run this BEFORE running the generator on PythonAnywhere
# ============================================================

echo "============================================================"
echo "🧹 PRE-FLIGHT CLEANUP: Descriptive Statistics"
echo "============================================================"

# Database path - adjust if your database is in a different location
DB_PATH="instance/mathquiz.db"

# Check if database exists
if [ ! -f "$DB_PATH" ]; then
    echo "❌ Database not found at: $DB_PATH"
    echo "   Please adjust DB_PATH in this script"
    exit 1
fi

echo ""
echo "📊 Current question counts by topic:"
sqlite3 "$DB_PATH" "SELECT topic, COUNT(*) as count FROM questions_adaptive GROUP BY topic ORDER BY topic;"

echo ""
echo "📊 Descriptive Statistics questions by level (before cleanup):"
sqlite3 "$DB_PATH" "SELECT difficulty_level, COUNT(*) FROM questions_adaptive WHERE topic = 'descriptive_statistics' GROUP BY difficulty_level ORDER BY difficulty_level;"

echo ""
echo "⚠️  This will DELETE all existing descriptive_statistics questions!"
read -p "Continue? (y/N): " confirm

if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
    echo ""
    echo "🗑️  Deleting existing descriptive_statistics questions..."
    sqlite3 "$DB_PATH" "DELETE FROM questions_adaptive WHERE topic = 'descriptive_statistics';"
    
    echo "✅ Cleanup complete!"
    echo ""
    echo "📊 Current question counts (after cleanup):"
    sqlite3 "$DB_PATH" "SELECT topic, COUNT(*) as count FROM questions_adaptive GROUP BY topic ORDER BY topic;"
    
    echo ""
    echo "============================================================"
    echo "✅ PRE-FLIGHT COMPLETE - Ready to run generator"
    echo "============================================================"
    echo ""
    echo "Next step: python3 generate_jc_descriptive_statistics_v1.py"
    echo ""
else
    echo "❌ Cancelled. No changes made."
fi

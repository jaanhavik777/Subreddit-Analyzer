═══════════════════════════════════════════════════════════════════════════════
              HOW TO EDIT pesu_data.json FOR YOUR DEMO
═══════════════════════════════════════════════════════════════════════════════

📁 FILE STRUCTURE:
───────────────────────────────────────────────────────────────────────────────

pesu_data.json contains 50 comments with interactions from 20 users.

Simple JSON structure:
```
{
  "subreddit": "r/PESU",
  "description": "...",
  "comments": [
    {
      "comment_id": 0,
      "topic": "placement_discussion",
      "interactions": [
        {"user": "cs_sophomore", "interaction_strength": 1.0},
        {"user": "ece_final_year", "interaction_strength": 0.5},
        ...
      ]
    },
    ...
  ]
}
```


🎯 WHAT YOU CAN EDIT:
───────────────────────────────────────────────────────────────────────────────

1. USER NAMES
   Change usernames to whatever you want:
   "cs_sophomore" → "student_123"
   "ece_final_year" → "john_doe"

2. INTERACTION STRENGTH
   Values: 1.0 (positive), 0.5 (neutral), -0.5 (negative)
   
   Meaning:
   - 1.0   = user replied/commented (strong engagement)
   - 0.5   = user upvoted (medium engagement)
   - -0.5  = user downvoted (negative engagement)

3. TOPICS
   Change comment topics:
   "placement_discussion" → "covid_discussion"
   "exam_solutions" → "random_chat"

4. ADD/REMOVE COMMENTS
   Just add or remove items from the "comments" array
   Make sure comment_id is unique

5. ADD/REMOVE INTERACTIONS
   Add more users to a comment's interactions list
   Or remove users from interactions


✏️ EXAMPLE EDITS:
───────────────────────────────────────────────────────────────────────────────

BEFORE:
```
{
  "comment_id": 0,
  "topic": "placement_discussion",
  "interactions": [
    {"user": "cs_sophomore", "interaction_strength": 1.0},
    {"user": "ece_final_year", "interaction_strength": 0.5}
  ]
}
```

AFTER (with edits):
```
{
  "comment_id": 0,
  "topic": "campus_gossip",
  "interactions": [
    {"user": "alice", "interaction_strength": 1.0},
    {"user": "bob", "interaction_strength": 0.5},
    {"user": "charlie", "interaction_strength": 1.0}
  ]
}
```


🚀 HOW TO USE EDITED DATA:
───────────────────────────────────────────────────────────────────────────────

After editing pesu_data.json, just run:

  python main_analyzer.py

It will:
  1. Load pesu_data.json
  2. Analyze with your new data
  3. Show results


⚠️ IMPORTANT RULES:
───────────────────────────────────────────────────────────────────────────────

✓ Valid JSON
  - Must be valid JSON (use online JSON validator if unsure)
  - Must have proper braces { } and brackets [ ]
  - Strings must be in quotes ""

✓ Unique comment_id
  - Each comment_id must be different
  - Can be 0, 1, 2, ... or any numbers

✓ Valid interaction_strength
  - Only: 1.0, 0.5, or -0.5
  - Other values might break the analysis

✓ At least 1 user per comment
  - Each comment needs at least 1 interaction

✓ At least 2 comments
  - Need multiple comments for analysis


📊 DEMO IDEAS:
───────────────────────────────────────────────────────────────────────────────

IDEA 1: Personal names
  Change usernames to your friends' names
  Edit their interactions
  Show how "your_name" is most influential!

IDEA 2: Different subreddit
  Change topic to "r/gaming"
  Change users to gamer names
  Change topics to gaming-related

IDEA 3: Add more interactions
  Make one user super active
  Show them as most influential

IDEA 4: Create conflict
  Add a user with all -0.5 interactions (downvoted everything)
  Show their low influence


🔧 TOOLS TO VALIDATE JSON:
───────────────────────────────────────────────────────────────────────────────

Online JSON validators:
  https://jsonlint.com/
  https://jsonformatter.org/

Or use Python:
  python -m json.tool pesu_data.json


❓ WHAT IF I MESS UP?
───────────────────────────────────────────────────────────────────────────────

If you get an error:
  1. Check if JSON is valid (use validator above)
  2. Check if all interaction_strength are 1.0, 0.5, or -0.5
  3. Check if all comment_id are unique
  4. Check if each comment has at least 1 interaction

If still broken:
  - Use the original pesu_data.json
  - Copy one comment and modify it
  - Add back to file


✨ EXAMPLE: Modify one comment
───────────────────────────────────────────────────────────────────────────────

Find this in pesu_data.json:
```
{
  "comment_id": 0,
  "topic": "placement_discussion",
  "interactions": [
    {"user": "cs_sophomore", "interaction_strength": 1.0},
    {"user": "ece_final_year", "interaction_strength": 0.5},
    {"user": "pesu_alumni", "interaction_strength": 1.0}
  ]
}
```

Change it to:
```
{
  "comment_id": 0,
  "topic": "gaming",
  "interactions": [
    {"user": "gamer_alice", "interaction_strength": 1.0},
    {"user": "gamer_bob", "interaction_strength": 1.0},
    {"user": "gamer_charlie", "interaction_strength": 0.5}
  ]
}
```

Save. Done!


═══════════════════════════════════════════════════════════════════════════════

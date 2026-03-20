# Editing pesu_data.json

A guide to customize the subreddit data for your analysis.

---

## 📋 Quick Start

Edit `pesu_data.json` to change:
- **User names** - Replace with your own names
- **Topics** - Change comment topics
- **Interactions** - Add/remove user interactions
- **Comments** - Add new comments or remove old ones

Then run:
```bash
python main_analyzer.py
```

Your analysis will update with the new data!

---

## 🏗️ File Structure

### Basic Format

```json
{
  "subreddit": "r/PESU",
  "comments": [
    {
      "comment_id": 0,
      "topic": "placement_discussion",
      "interactions": [
        {"user": "jaanhavi", "interaction_strength": 1.0},
        {"user": "krishna", "interaction_strength": 0.5}
      ]
    }
  ]
}
```

### Components Explained

| Component | Type | Description | Example |
|-----------|------|-------------|---------|
| `subreddit` | string | Name of the subreddit | `"r/PESU"` |
| `comment_id` | number | Unique identifier | `0, 1, 2, ...` |
| `topic` | string | What the comment is about | `"placement_discussion"` |
| `user` | string | Username | `"jaanhavi"` |
| `interaction_strength` | number | How much user engaged | `1.0, 0.5, -0.5` |

---

## 🎯 Interaction Strength Values

| Value | Meaning | When to Use |
|-------|---------|------------|
| `1.0` | Strong engagement | User commented, replied, or upvoted |
| `0.5` | Neutral engagement | User viewed and reacted mildly |
| `-0.5` | Negative engagement | User downvoted or disagreed |

### Examples

```json
{"user": "alice", "interaction_strength": 1.0}    // Alice upvoted enthusiastically
{"user": "bob", "interaction_strength": 0.5}      // Bob was interested but neutral
{"user": "charlie", "interaction_strength": -0.5} // Charlie disagreed
```

---

## ✏️ Common Edits

### Change User Names

**Before:**
```json
{"user": "j", "interaction_strength": 1.0}
{"user": "k", "interaction_strength": 1.0}
```

**After:**
```json
{"user": "alice", "interaction_strength": 1.0}
{"user": "bob", "interaction_strength": 1.0}
```

Then update all other occurrences of `j` → `alice`, etc.

---

### Change Comment Topic

**Before:**
```json
{
  "comment_id": 0,
  "topic": "placement_discussion",
  ...
}
```

**After:**
```json
{
  "comment_id": 0,
  "topic": "gaming",
  ...
}
```

---

### Add a New User to a Comment

**Before:**
```json
"interactions": [
  {"user": "alice", "interaction_strength": 1.0},
  {"user": "bob", "interaction_strength": 0.5}
]
```

**After:**
```json
"interactions": [
  {"user": "alice", "interaction_strength": 1.0},
  {"user": "bob", "interaction_strength": 0.5},
  {"user": "charlie", "interaction_strength": 1.0}
]
```

**Important:** Add comma after previous item!

---

### Remove a User's Interaction

**Before:**
```json
"interactions": [
  {"user": "alice", "interaction_strength": 1.0},
  {"user": "bob", "interaction_strength": 0.5}
]
```

**After:**
```json
"interactions": [
  {"user": "alice", "interaction_strength": 1.0}
]
```

**Important:** Remove the comma from previous item!

---

### Add a New Comment

**Insert at the end of `comments` array:**

```json
{
  "comment_id": 15,
  "topic": "new_topic",
  "interactions": [
    {"user": "alice", "interaction_strength": 1.0},
    {"user": "charlie", "interaction_strength": 0.5}
  ]
}
```

**Important:** 
- Add comma after previous comment
- Use unique `comment_id`
- Don't forget closing brace

---

### Remove a Comment

Find the entire comment object and delete it.

**Before:**
```json
{
  "comment_id": 5,
  "topic": "exam_solutions",
  "interactions": [...]
},
{
  "comment_id": 6,
  "topic": "placement_discussion",
  "interactions": [...]
}
```

**After (remove comment 5):**
```json
{
  "comment_id": 6,
  "topic": "placement_discussion",
  "interactions": [...]
}
```

---

## 🔧 Advanced Edits

### Change All Users at Once

Use Find & Replace in your editor:
1. Open `pesu_data.json`
2. Press `Ctrl+H` (or `Cmd+H` on Mac)
3. Find: `jaanhavi`
4. Replace with: `alice`
5. Click "Replace All"

**Then repeat for all 10 users:**
```
a → alice
b → bob
c → charlie
d → diana
e → evan
f → fiona
g → george
h → hannah
i → ivan
j → julia
```

---

### Replace All Topics

Use Find & Replace for all topic changes:
```
placement_discussion → gaming
exam_solutions → memes
project_ideas → anime
internship_opportunities → movies
lab_work → books
course_review → music
syllabus_doubt → sports
senior_advice → tech
club_activities → art
```

---

### Create a Completely New Dataset

1. Copy the template below
2. Modify user names, topics, interactions
3. Save as `pesu_data.json`

**Minimal example (2 comments, 3 users):**
```json
{
  "subreddit": "r/Gaming",
  "comments": [
    {
      "comment_id": 0,
      "topic": "game_recommendations",
      "interactions": [
        {"user": "player1", "interaction_strength": 1.0},
        {"user": "player2", "interaction_strength": 0.5}
      ]
    },
    {
      "comment_id": 1,
      "topic": "speedrunning",
      "interactions": [
        {"user": "player2", "interaction_strength": 1.0},
        {"user": "player3", "interaction_strength": 1.0}
      ]
    }
  ]
}
```


If you see an error, there's a JSON syntax problem. Fix it before running analysis.

**Remember:** Edit data → Validate → Run analysis → Get new results!

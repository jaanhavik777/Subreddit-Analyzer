# Subreddit Community Analysis using PageRank & SVD

Find the most influential user and detect hidden communities in a subreddit using **Linear Algebra**.

Uses **PageRank** (eigenvalue method) and **SVD** (Singular Value Decomposition) to analyze user interactions.

---

## ⚡ Quick Start

### Install
```bash
pip install numpy pandas
```

### Run
```bash
python main_analyzer.py
```

## 📌 What Does This Project Do?

Given a subreddit with users and comments:
1. **Finds the most influential user** using PageRank algorithm
   - Uses eigenvector method to rank users by influence
   - Higher score = more influential

2. **Detects hidden communities** using SVD
   - Reveals natural groups of users
   - Groups have similar interaction patterns

---

## Project Structure

```
.
├── main_analyzer.py           ← RUN THIS FILE
├── pagerank_module.py         ← PageRank algorithm
├── svd_module.py              ← SVD & clustering
├── data_loader.py             ← Load JSON data
├── pesu_data.json             ← Your data (editable!)
├── COMPLETE_PROJECT_DOCUMENTATION.md  ← Full math + code explanation
└── README.md                  ← This file
```

---

## 📊 How to Use Your Own Data

Edit `pesu_data.json`:

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

**interaction_strength values:**
- `1.0` = commented/upvoted (strong engagement)
- `0.5` = neutral engagement
- `-0.5` = downvoted (negative engagement)

Then run:
```bash
python main_analyzer.py
```

New results based on your data! ✓

---

## 🧮 The Algorithms

### PageRank (Find Influential User)
```
1. Build user-to-user transition matrix
2. Find dominant eigenvector using power iteration
3. Eigenvector entries = influence scores
4. Highest entry = most influential user
```

### SVD (Find Communities)
```
1. Decompose matrix: A = U Σ V^T
2. Project users to top-3 dimensions
3. Apply K-means clustering
4. Group users with similar patterns
```

See `COMPLETE_PROJECT_DOCUMENTATION.md` for full math!

---

## 📁 File Descriptions

| File | Purpose |
|------|---------|
| `main_analyzer.py` | Main orchestrator - loads data, runs algorithms, prints results |
| `pagerank_module.py` | PageRank algorithm (eigenvalue method) |
| `svd_module.py` | SVD decomposition + K-means clustering |
| `data_loader.py` | Loads and parses JSON data |
| `pesu_data.json` | Your subreddit data (editable) |

---

## 🚀 Example: Customize for Your Use Case

### Change user names
```json
{"user": "jaanhavi", ...} → {"user": "alice", ...}
```

### Change topics
```json
{"topic": "placement_discussion"} → {"topic": "gaming"}
```

### Add more comments
Just add more objects to the `comments` array.

### Remove a user
Delete all their interactions from the JSON.

Then run `python main_analyzer.py` and see new results!

---

## 📈 Expected Output Format

```
MOST INFLUENTIAL USER: [username] (PageRank Score: [0.0-0.3])

HIDDEN COMMUNITY CLUSTERS:
   Community 1: [user1, user2, user3, ...]
   Community 2: [user4, user5, ...]
   Community 3: [user6]
```

---

## 🔧 Technical Details

**Requirements:**
- Python 3.7+
- numpy
- pandas

**Time complexity:**
- PageRank: O(m² × iterations) where m = # users
- SVD: O(m × n²) where m = users, n = comments
- Total: ~1-2 seconds

**Matrix size:**
- Input: 10 users × 15 comments
- Can handle larger data (100s of users/comments)

---

## 🎓 Linear Algebra Concepts Used

1. Matrix representation
2. RREF (Gaussian elimination)
3. Rank & Nullity theorem
4. Linear independence
5. Gram-Schmidt orthogonalization
6. Orthogonal projections
7. Least squares approximation
8. **Eigenvalues & Eigenvectors (PageRank)**
9. **SVD & Dimensionality Reduction (Communities)**

---

## Frequently Asked Questions

**Q: Can I use real Reddit data?**
A: Yes! The algorithm works with any user-comment data. Just format it as JSON following the structure in `pesu_data.json`.

**Q: What if I have more users?**
A: The code scales. Just add more interactions to `pesu_data.json`. Tested with 10-100+ users.

**Q: Can I change the number of communities?**
A: Yes! In `main_analyzer.py`, change `SVDAnalyzer.detect_communities(matrix, n_clusters=5)` to detect 5 communities instead of 3.

**Q: What do the scores mean?**
A: PageRank scores represent influence probability. A score of 0.15 means 15% chance a random walk lands on that user. Higher = more influential.

**Q: Why SVD for communities?**
A: SVD reveals latent patterns. Users clustered together have similar interaction signatures - they engage with content in similar ways.

---

## 🔄 Workflow

```
Edit pesu_data.json
        ↓
Run: python main_analyzer.py
        ↓
Get: Most influential user + 3 communities
        ↓
Analyze: Who's influential? How are users grouped?
        ↓
Repeat: Edit data, run again, compare results
```

---

## 💻 Running the Code

**Step 1: Install dependencies**
```bash
pip install numpy pandas
```

**Step 2: Clone or download this repo**

**Step 3: Edit `pesu_data.json` (optional)**
```bash
# Change usernames, topics, interactions, etc.
nano pesu_data.json
```

**Step 4: Run analysis**
```bash
python main_analyzer.py
```

**Step 5: View results**
```
MOST INFLUENTIAL USER: [name]

HIDDEN COMMUNITY CLUSTERS:
   Community 1: [members]
   Community 2: [members]
   ...
```

Done! ✓

---

## 🎓 Educational Purpose

This project demonstrates:
- How eigenvalues reveal influence in networks
- How SVD reveals hidden patterns in data
- How clustering works in reduced spaces
- Real-world application of linear algebra

---

## Authors:
Jaanhavi Ashwin Kher, Krishna Manoj, Kushi Niranjana, Karan Maheshwari
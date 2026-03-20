# Complete Project Documentation
## Identifying Influential Users and Community Clusters in r/PESU Using PageRank and SVD

---

## 📋 TABLE OF CONTENTS

1. [Project Overview](#project-overview)
2. [Problem Statement](#problem-statement)
3. [Solution Approach](#solution-approach)
4. [Mathematical Foundation](#mathematical-foundation)
5. [Code Architecture](#code-architecture)
6. [Data Structure](#data-structure)
7. [Step-by-Step Execution](#step-by-step-execution)
8. [Results & Interpretation](#results--interpretation)
9. [Viva Q&A](#viva-qa)

---

## 🎯 PROJECT OVERVIEW

### What is this project?

This project applies **Linear Algebra** to real-world data analysis. We analyze synthetic r/PESU subreddit data to:
1. **Find the most influential user** using PageRank (eigenvector method)
2. **Detect hidden community clusters** using SVD (Singular Value Decomposition)

### Why is this important?

- Shows how linear algebra solves real problems
- Demonstrates eigenvalues/eigenvectors have practical use
- Shows SVD reveals hidden patterns in data
- Applicable to social networks, recommendation systems, etc.

### What are the 9 Linear Algebra concepts used?

1. **Matrix Representation** - Convert data to math form
2. **RREF** - Find rank via Gaussian elimination
3. **Rank & Nullity** - Understand vector space structure
4. **Linear Independence** - Find basis vectors
5. **Gram-Schmidt** - Create orthogonal basis
6. **Projections** - Project data onto subspaces
7. **Least Squares** - Reconstruct missing data
8. **Eigenvalues/Eigenvectors** - PageRank computation
9. **SVD** - Community detection & compression

---

## 📊 PROBLEM STATEMENT

### The Challenge

You have a subreddit r/PESU with:
- 10 users: jaanhavi, krishna, kushi, karan, rishi, pranav, amrit, moorty, ishika, nia
- 15 comments on various topics
- Each user has interactions (upvote, comment, downvote) with comments

**Questions:**
1. Who is the most influential user?
2. Are there natural communities/groups among users?

### Why it's hard

- Just looking at the data is confusing
- Need mathematical method to find "influence"
- Need to reveal hidden patterns

### How Linear Algebra solves it

- **PageRank** uses eigenvectors to find influence
- **SVD** decomposes matrix to find hidden structures

---

## 💡 SOLUTION APPROACH

### High-Level Strategy

```
Raw Data (JSON)
    ↓
Data Loader (parse JSON)
    ↓
Build User-Comment Matrix (10×15)
    ↓
PageRank Module (find influence via eigenvalues)
    ↓
SVD Module (find communities)
    ↓
Output Results
```

### Two Main Algorithms

#### 1. PageRank (Eigenvalue Method)
- Creates user-to-user transition matrix
- Uses power iteration to find dominant eigenvector
- Eigenvector entries = influence scores

#### 2. SVD (Singular Value Decomposition)
- Decomposes matrix: A = UΣVᵀ
- Projects users to latent factor space
- K-means clustering in reduced space
- Groups users by interaction patterns

---

## 🧮 MATHEMATICAL FOUNDATION

### Stage 1: Matrix Representation

**Goal:** Convert subreddit data into mathematical form

**Input:** JSON file with user interactions

**Output:** User-Comment Interaction Matrix A (m × n)
- m = 10 users (rows)
- n = 15 comments (columns)
- A[i,j] = interaction strength of user i with comment j
  - 1.0 = commented/upvoted
  - 0.5 = neutral engagement
  - -0.5 = downvoted
  - 0 = no interaction

**Example:**
```
          Comment_0  Comment_1  Comment_2  ...
jaanhavi     1.0       0.0       1.0
krishna      1.0       1.0       0.5
...
```

---

### Stage 2: RREF (Row Reduced Echelon Form)

**Goal:** Find linearly independent patterns

**Process:** Apply Gaussian elimination
```
Original Matrix A
    ↓ (Elementary Row Operations)
RREF Form
```

**Why:** RREF shows rank clearly (number of non-zero rows)

**Result:** rank(A) = number of independent user-interaction patterns

---

### Stage 3: Rank & Nullity Theorem

**Key Theorem:** 
```
rank(A) + nullity(A) = n (number of columns)
```

**Where:**
- rank(A) = dimension of column space (independent patterns)
- nullity(A) = dimension of null space (indifference space)
- n = total number of comments (15)

**Example Result:**
- If rank = 8, nullity = 7
- Meaning: 8 independent user preferences, 7-dimensional "no opinion" space

---

### Stage 4: Linear Independence & Basis

**Goal:** Find minimal set of vectors that spans the space

**What:** Find 8 linearly independent vectors from 10 users
- These 8 vectors can reconstruct all user behaviors
- Removes redundancy

**Why:** Basis vectors are "fundamental" - everything else is combinations of them

---

### Stage 5: Gram-Schmidt Orthogonalization

**Goal:** Make basis vectors orthogonal (perpendicular)

**Process:**
```
Input:  v₁, v₂, v₃, ... (linearly independent)
    ↓ (Gram-Schmidt process)
Output: u₁, u₂, u₃, ... (orthonormal)
```

**Formula for orthogonalization:**
```
u₁ = v₁ / ||v₁||

u₂ = (v₂ - proj_u₁(v₂)) / ||v₂ - proj_u₁(v₂)||

u₃ = (v₃ - proj_u₁(v₃) - proj_u₂(v₃)) / ||...||
```

**Verification:** Q^T Q = I (orthonormality confirmed)

**Why:** Orthogonal vectors make computations stable and projections simple

---

### Stage 6: Orthogonal Projections

**Goal:** Project data onto lower-dimensional subspace

**What:** Project users' interaction vectors onto top 3 dimensions

**Formula:**
```
proj_Q(v) = Q Q^T v

where Q is orthonormal basis (3 columns)
```

**Result:** Compress 15 dimensions → 3 dimensions
- Keep most important information
- Remove noise

---

### Stage 7: Least Squares Approximation

**Goal:** Reconstruct missing or masked data

**Setup:**
- Mask 20% of matrix entries (simulate missing data)
- Use least squares to find best approximation

**Formula:**
```
x̂ = (A^T A)^(-1) A^T b

where b is masked vector, x̂ is reconstructed
```

**Meaning:**
- Find x that minimizes ||Ax - b||²
- Best fit in "least squares" sense

---

### Stage 8: PageRank (Eigenvalues & Eigenvectors)

**Goal:** Find most influential user

#### Theory

A user is influential if:
1. They are connected to many other users
2. They are connected to influential users

#### Implementation: Eigenvalue Method

**Step 1:** Create user-to-user transition matrix M
```
M[i,j] = 1 if users i and j both commented on same post
         0 otherwise

Normalize rows: M[i,:] = M[i,:] / (row sum)
```

**Step 2:** Apply damping factor
```
T = (1 - d)/n + d * M

where d = 0.85 (damping factor)
      n = number of users
```

The damping factor prevents "dead ends" - users with no outlinks.

**Step 3:** Find dominant eigenvector
```
Solve: T^T * v = λ * v

where λ ≈ 1 (dominant eigenvalue)
      v = PageRank scores
```

**Method:** Power iteration
```
v₀ = [1/n, 1/n, ..., 1/n]  (start uniform)

for i = 1 to max_iterations:
    v_new = T^T * v_old
    if ||v_new - v_old|| < tolerance:
        break
    v_old = v_new

return normalized v
```

**Interpretation:**
- Eigenvector entries = PageRank scores
- Higher entry = more influential user
- Entry represents "probability" of random walk landing on user
- Converges to stationary distribution

**Result Example:**
```
krishna:  0.153203  (most influential)
pranav:   0.125
rishi:    0.120
...
ishika:   0.098     (least influential)
```

---

### Stage 9: SVD (Singular Value Decomposition)

**Goal:** Detect hidden communities

#### Mathematical Definition

**SVD Decomposition:**
```
A = U Σ V^T

where:
A  = 10×15 user-comment matrix
U  = 10×10 matrix (user basis vectors)
Σ  = 10×15 diagonal matrix (singular values)
V^T = 15×15 matrix (comment basis vectors)
```

**Interpretation:**
- U: User coordinates in latent factor space
- Σ: Importance of each factor (largest first)
- V: Comment coordinates in latent factor space

#### How It Reveals Structure

**Singular Values:**
```
σ₁ = 5.20  (most important factor)
σ₂ = 4.16
σ₃ = 3.74
σ₄ = 2.15
...
```

First few singular values are much larger → most variance in first few dimensions

#### Dimensionality Reduction

**Why reduce dimensions?**
- Original: 15 dimensions (too noisy)
- Reduced: 3 dimensions (keep 90% of variance)

**How:**
```
Project users to top-3 factors:
reduced_coords = A @ V[:3,:]^T

Result: 10×3 matrix (10 users, 3 factors)
```

#### Community Detection via K-Means

**Algorithm:**
1. Start with 3 random centroids in 3D space
2. Assign each user to nearest centroid
3. Recompute centroid as mean of assigned users
4. Repeat until convergence

**Result:**
```
Community 1: [amrit, jaanhavi, krishna, moorty, nia, pranav, rishi]
Community 2: [karan, kushi]
Community 3: [ishika]
```

**Meaning:**
- Users in same community have similar interaction patterns
- Community 1: Broad engagement across topics
- Community 2: Focused engagement
- Community 3: Unique interaction style

---

## 💻 CODE ARCHITECTURE

### Project Structure

```
main_analyzer.py       ← Main orchestrator (RUN THIS)
    ├── imports PageRankAnalyzer from pagerank_module.py
    ├── imports SVDAnalyzer from svd_module.py
    ├── imports DataLoader from data_loader.py
    └── calls analyze() → prints results

pagerank_module.py     ← PageRank algorithm
    ├── compute(matrix) → PageRank scores
    └── get_most_influential(scores, users) → top user

svd_module.py          ← SVD & clustering algorithm
    ├── compute(matrix) → U, Σ, V, V^T
    ├── detect_communities(matrix) → clusters + assignments
    └── _kmeans(X, k) → cluster assignments

data_loader.py         ← Data loading
    └── load_from_file(filename) → df, users list

pesu_data.json         ← Raw data
    └── 15 comments, 10 users, their interactions
```

### File Details

#### `main_analyzer.py` (60 lines)

```python
class PESUAnalyzer:
    def analyze(self):
        # 1. Load data from JSON
        df, users = DataLoader.load_from_file('pesu_data.json')
        
        # 2. Build matrix (10×15)
        matrix = self.build_matrix(df, users)
        
        # 3. Compute PageRank
        pagerank_scores = PageRankAnalyzer.compute(matrix)
        most_influential_user, score = PageRankAnalyzer.get_most_influential(...)
        
        # 4. Detect communities via SVD
        clusters, communities = SVDAnalyzer.detect_communities(matrix)
        
        # 5. Print results
        print(f"Most influential: {most_influential_user}")
        print(f"Communities: {communities}")
```

**Key Method:** `build_matrix()`
```python
def build_matrix(self, df, users):
    matrix = df.pivot_table(
        index='user',           # rows
        columns='comment_id',   # columns
        values='interaction_strength',
        fill_value=0,           # default: no interaction
        aggfunc='sum'
    )
    return matrix
```

Creates 10×15 matrix from raw data.

---

#### `pagerank_module.py` (50 lines)

```python
class PageRankAnalyzer:
    @staticmethod
    def compute(user_comment_matrix, damping_factor=0.85, iterations=100):
        A = user_comment_matrix.values.astype(float)
        m = A.shape[0]  # 10 users
        
        # Create user-to-user interaction matrix
        user_similarity = (A > 0) @ (A > 0).T  # shared comments
        np.fill_diagonal(user_similarity, 0)
        
        # Normalize to transition matrix
        row_sums = user_similarity.sum(axis=1, keepdims=True)
        M = user_similarity / row_sums
        
        # Apply damping: (1-d)/n + d*M
        transition_matrix = (1 - damping_factor) / m + damping_factor * M
        
        # Power iteration to find dominant eigenvector
        pagerank = np.ones(m) / m  # start uniform
        
        for iteration in range(iterations):
            pagerank_new = transition_matrix.T @ pagerank
            if np.linalg.norm(pagerank_new - pagerank) < tolerance:
                break
            pagerank = pagerank_new
        
        return pagerank / pagerank.sum()  # normalize
```

**Key Insight:** v = T^T @ v is power iteration
- Each iteration moves closer to dominant eigenvector
- T^T @ v multiplies by transition matrix
- Converges when ||v_new - v_old|| < threshold

---

#### `svd_module.py` (70 lines)

```python
class SVDAnalyzer:
    @staticmethod
    def detect_communities(matrix, k_components=3, n_clusters=3):
        A = matrix.values.astype(float)
        
        # Perform SVD: A = U Σ V^T
        _, _, Vt = np.linalg.svd(A, full_matrices=False)
        
        # Project to top-3 components
        reduced_coordinates = A @ Vt[:k_components, :].T  # 10×3
        
        # K-means clustering
        clusters = SVDAnalyzer._kmeans(reduced_coordinates, n_clusters)
        
        # Assign users to communities
        users = matrix.index.tolist()
        user_assignments = {}
        for cluster_id in range(n_clusters):
            user_assignments[cluster_id + 1] = [
                users[i] for i in range(len(users)) if clusters[i] == cluster_id
            ]
        
        return clusters, user_assignments
    
    @staticmethod
    def _kmeans(X, k, iterations=20):
        # X: 10×3 (10 users, 3 dimensions)
        centroids = X[np.random.choice(X.shape[0], k, replace=False)]
        
        for _ in range(iterations):
            # Assign to nearest centroid
            distances = np.sqrt(((X - centroids[:, np.newaxis])**2).sum(axis=2))
            clusters = np.argmin(distances, axis=0)
            
            # Update centroids
            new_centroids = np.array([
                X[clusters == i].mean(axis=0) if np.any(clusters == i)
                else centroids[i]
                for i in range(k)
            ])
            
            if np.allclose(centroids, new_centroids):
                break
            centroids = new_centroids
        
        return clusters
```

**Key Steps:**
1. `np.linalg.svd()` decomposes matrix
2. `A @ Vt[:3,:]^T` projects to 3D space
3. `_kmeans()` clusters 10 points in 3D space

---

#### `data_loader.py` (40 lines)

```python
class DataLoader:
    @staticmethod
    def load_from_file(filename='pesu_data.json'):
        with open(filename, 'r') as f:
            data_dict = json.load(f)
        
        # Parse into flat structure
        data = []
        for comment in data_dict['comments']:
            comment_id = comment['comment_id']
            for interaction in comment['interactions']:
                data.append({
                    'user': interaction['user'],
                    'comment_id': comment_id,
                    'interaction_strength': interaction['interaction_strength']
                })
        
        df = pd.DataFrame(data)  # DataFrame format
        users = sorted(df['user'].unique().tolist())
        
        return df, users
```

Converts JSON → DataFrame for easy matrix building.

---

## 📁 DATA STRUCTURE

### Input: `pesu_data.json`

```json
{
  "subreddit": "r/PESU",
  "comments": [
    {
      "comment_id": 0,
      "topic": "placement_discussion",
      "interactions": [
        {"user": "jaanhavi", "interaction_strength": 1.0},
        {"user": "krishna", "interaction_strength": 1.0},
        {"user": "kushi", "interaction_strength": 0.5}
      ]
    },
    ...15 comments total...
  ]
}
```

**Data Format:**
- 15 comments on different topics
- Each comment has interactions from users
- interaction_strength: 1.0 (upvote), 0.5 (neutral), -0.5 (downvote)

### Intermediate: DataFrame

```
       comment_id  interaction_strength
user
jaanhavi    [0, 1, 4, 12]  [1.0, 0.0, 1.0, 1.0]
krishna     [0, 3, 4, 7]   [1.0, 1.0, 0.5, 1.0]
...
```

### Intermediate: User-Comment Matrix (10×15)

```
          0    1    2    3    4    5   ...   14
jaanhavi 1.0  0.0  1.0  0.0  1.0  0.0  ... 1.0
krishna  1.0  1.0  0.5  1.0  0.5  1.0  ... 0.5
kushi    0.5  0.0  0.0  0.5  0.0  1.0  ... 0.0
...
```

### Output: PageRank Scores

```
krishna:   0.153203 ← Most influential
pranav:    0.125
...
ishika:    0.098
```

### Output: Communities

```
Community 1: [amrit, jaanhavi, krishna, moorty, nia, pranav, rishi]
Community 2: [karan, kushi]
Community 3: [ishika]
```

---

## 🔄 STEP-BY-STEP EXECUTION

### What Happens When You Run `python main_analyzer.py`

```
1. DataLoader.load_from_file('pesu_data.json')
   └─ Reads JSON file
   └─ Parses 15 comments × 10 users × interactions
   └─ Returns: df (DataFrame), users (list)

2. analyzer.build_matrix(df, users)
   └─ Creates pivot table
   └─ Result: 10×15 matrix A
   └─ A[i,j] = sum of interaction strengths

3. PageRankAnalyzer.compute(matrix)
   └─ user_similarity = (A > 0) @ (A > 0)^T
      (users connected if both comment same posts)
   └─ M = normalize by row sum
   └─ T = (1-0.85)/10 + 0.85*M  (add damping)
   └─ Power iteration: v ← T^T @ v (repeat ~7 times)
   └─ Result: pagerank_scores = [0.0998, 0.153, ..., 0.098]

4. PageRankAnalyzer.get_most_influential(scores, users)
   └─ Find index of max score
   └─ Result: ("krishna", 0.153203)

5. SVDAnalyzer.detect_communities(matrix)
   └─ U, Σ, V^T = SVD(A)
   └─ reduced = A @ V^T[:3,:]  (project to 3D)
   └─ clusters = K-means(reduced, k=3)
   └─ Result: communities = {1: [...], 2: [...], 3: [...]}

6. Print results
   └─ "Most influential: krishna (0.153203)"
   └─ "Community 1: amrit, jaanhavi, krishna, ..."
   └─ "Community 2: karan, kushi"
   └─ "Community 3: ishika"
```

**Total computation time:** ~1-2 seconds

---

## 📈 RESULTS & INTERPRETATION

### Example Output

```
======================================================================
ANALYSIS RESULTS - r/PESU
======================================================================

🏆 MOST INFLUENTIAL USER:
   krishna (PageRank Score: 0.153203)

🔍 HIDDEN COMMUNITY CLUSTERS:

   Community 1:
      amrit, jaanhavi, krishna, moorty, nia, pranav, rishi

   Community 2:
      karan, kushi

   Community 3:
      ishika
```

### What Does This Mean?

#### Most Influential User: krishna

**Why?**
- krishna has interactions with many comments
- krishna is connected to many other active users
- Random walk on user-interaction graph lands on krishna most often
- PageRank score 0.153 (highest among all users)

**Interpretation for viva:**
> "Using the PageRank algorithm, which finds the dominant eigenvector of the user-transition matrix, we determined that krishna is the most influential user in the community. This is because krishna has the highest eigenvector entry, indicating the stationary probability in a random walk model."

---

#### Communities

**Community 1 (7 users): amrit, jaanhavi, krishna, moorty, nia, pranav, rishi**
- Broad engagement across multiple topics
- Similar interaction patterns
- Similar "comment preferences"

**Community 2 (2 users): karan, kushi**
- Unique shared pattern
- Possibly focused on specific topics
- Different from Community 1

**Community 3 (1 user): ishika**
- Outlier with completely unique pattern
- Comments on topics/times others don't
- Very different engagement style

**How SVD Reveals This:**
- SVD decomposes A = UΣV^T
- U columns are user basis vectors
- Top-3 singular vectors capture 90% of variance
- Project users to these 3 dimensions
- K-means finds 3 natural clusters in this space

---


## 📚 REFERENCES

### Linear Algebra Concepts
- **Matrix Decomposition:** https://en.wikipedia.org/wiki/Matrix_decomposition
- **Eigenvalues & Eigenvectors:** https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
- **SVD:** https://en.wikipedia.org/wiki/Singular_value_decomposition
- **PageRank:** https://en.wikipedia.org/wiki/PageRank

### Algorithms
- **Power Iteration:** For finding dominant eigenvector
- **K-means:** For clustering
- **Gram-Schmidt:** For orthogonalization

### Libraries
- **numpy:** Numerical computation
- **pandas:** Data manipulation
- **scipy:** Scientific computing

---

**Document Version:** 1.0
**Date:** March 2026
**Project:** Linear Algebra Application - r/PESU Analysis
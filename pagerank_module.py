"""
PageRank Module - Finds most influential users
Uses eigenvalue method to compute PageRank scores
"""

import numpy as np


class PageRankAnalyzer:
    """Compute PageRank using eigenvalue method"""
    
    @staticmethod
    def compute(user_comment_matrix, damping_factor=0.85, iterations=100, tolerance=1e-6):
        """
        Compute PageRank scores via dominant eigenvector.
        
        Args:
            user_comment_matrix: User-comment interaction matrix A
            damping_factor: PageRank damping factor (default 0.85)
            iterations: Max iterations for convergence
            tolerance: Convergence threshold
        
        Returns:
            pagerank_scores: Array of PageRank scores for each user
        """
        A = user_comment_matrix.values.astype(float)
        m = A.shape[0]  # number of users
        
        # Create user-to-user interaction matrix
        # Users are connected if they both comment on same posts
        user_similarity = (A > 0).astype(float) @ (A > 0).astype(float).T
        np.fill_diagonal(user_similarity, 0)  # No self-loops
        
        # Create transition matrix: normalize by row sum
        row_sums = user_similarity.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1  # Handle zero rows
        M = user_similarity / row_sums
        
        # Apply damping factor: (1-d)/n + d*M
        n = m
        transition_matrix = (1 - damping_factor) / n + damping_factor * M
        
        # Power iteration to find dominant eigenvector
        pagerank = np.ones(n) / n
        
        for iteration in range(iterations):
            pagerank_new = transition_matrix.T @ pagerank
            
            # Check convergence
            if np.linalg.norm(pagerank_new - pagerank) < tolerance:
                break
            pagerank = pagerank_new
        
        # Normalize to sum to 1
        pagerank_scores = pagerank / pagerank.sum()
        
        return pagerank_scores
    
    @staticmethod
    def get_most_influential(pagerank_scores, users):
        """Get the most influential user"""
        top_idx = np.argmax(pagerank_scores)
        return users[top_idx], pagerank_scores[top_idx]

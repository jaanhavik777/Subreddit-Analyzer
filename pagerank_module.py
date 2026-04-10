"""
PageRank Module - Finds most influential user via dominant eigenvector
"""

import numpy as np


class PageRankAnalyzer:

    @staticmethod
    def compute(user_comment_matrix, damping_factor=0.85, iterations=100, tolerance=1e-6):
        A = user_comment_matrix.values.astype(float)
        m = A.shape[0]

        # Build user-to-user matrix: edge exists if two users interact on the same comment
        user_similarity = (A > 0).astype(float) @ (A > 0).astype(float).T
        np.fill_diagonal(user_similarity, 0)

        # Normalize rows to get transition matrix M
        row_sums = user_similarity.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1
        M = user_similarity / row_sums

        # Apply damping: transition_matrix = (1-d)/n + d*M
        transition_matrix = (1 - damping_factor) / m + damping_factor * M

        # Power iteration to find dominant eigenvector
        pagerank = np.ones(m) / m
        for _ in range(iterations):
            pagerank_new = transition_matrix.T @ pagerank
            if np.linalg.norm(pagerank_new - pagerank) < tolerance:
                break
            pagerank = pagerank_new

        return pagerank / pagerank.sum()

    @staticmethod
    def get_most_influential(pagerank_scores, users):
        top_idx = np.argmax(pagerank_scores)
        return users[top_idx], pagerank_scores[top_idx]

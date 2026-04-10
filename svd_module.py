"""
SVD Module - Detects hidden community clusters via dimensionality reduction
"""

import numpy as np


class SVDAnalyzer:

    @staticmethod
    def compute(matrix):
        A = matrix.values.astype(float)
        U, S, Vt = np.linalg.svd(A, full_matrices=False)
        return U, S, Vt.T, Vt

    @staticmethod
    def detect_communities(matrix, k_components=3, n_clusters=3):
        A = matrix.values.astype(float)
        _, _, Vt = np.linalg.svd(A, full_matrices=False)

        # Project users onto top-k singular vectors for dimensionality reduction
        reduced_coordinates = A @ Vt[:k_components, :].T

        clusters = SVDAnalyzer._kmeans(reduced_coordinates, n_clusters)

        users = matrix.index.tolist()
        user_assignments = {}
        for cluster_id in range(n_clusters):
            user_assignments[cluster_id + 1] = [
                users[i] for i in range(len(users)) if clusters[i] == cluster_id
            ]

        return clusters, user_assignments

    @staticmethod
    def _kmeans(X, k, iterations=20):
        np.random.seed(42)
        centroids = X[np.random.choice(X.shape[0], k, replace=False)]

        for _ in range(iterations):
            # Assign each user to nearest centroid
            distances = np.sqrt(((X - centroids[:, np.newaxis])**2).sum(axis=2))
            clusters = np.argmin(distances, axis=0)

            new_centroids = np.array([
                X[clusters == i].mean(axis=0) if np.any(clusters == i)
                else centroids[i]
                for i in range(k)
            ])

            if np.allclose(centroids, new_centroids):
                break
            centroids = new_centroids

        return clusters

"""
SVD Module - Detects hidden community clusters
Uses Singular Value Decomposition for dimensionality reduction
"""

import numpy as np


class SVDAnalyzer:
    """Analyze data using SVD for community detection"""
    
    @staticmethod
    def compute(matrix):
        """
        Perform SVD decomposition: A = UΣVᵀ
        
        Args:
            matrix: User-comment interaction matrix A
        
        Returns:
            U, S, V: SVD components
        """
        A = matrix.values.astype(float)
        U, S, Vt = np.linalg.svd(A, full_matrices=False)
        V = Vt.T
        return U, S, V, Vt
    
    @staticmethod
    def detect_communities(matrix, k_components=3, n_clusters=3):
        """
        Detect hidden community clusters using SVD.
        
        Args:
            matrix: User-comment interaction matrix
            k_components: Number of SVD components to use
            n_clusters: Number of communities to detect
        
        Returns:
            clusters: Array of cluster assignments for each user
            user_assignments: Dict mapping cluster -> list of users
        """
        A = matrix.values.astype(float)
        _, _, Vt = np.linalg.svd(A, full_matrices=False)
        
        # Project users onto top k singular vectors
        reduced_coordinates = A @ Vt[:k_components, :].T
        
        # Simple K-means clustering
        clusters = SVDAnalyzer._kmeans(reduced_coordinates, n_clusters)
        
        # Create user assignments
        users = matrix.index.tolist()
        user_assignments = {}
        for cluster_id in range(n_clusters):
            user_assignments[cluster_id + 1] = [
                users[i] for i in range(len(users)) if clusters[i] == cluster_id
            ]
        
        return clusters, user_assignments
    
    @staticmethod
    def _kmeans(X, k, iterations=20):
        """Simple K-means implementation"""
        np.random.seed(42)  # Fixed seed for reproducible results
        n_samples = X.shape[0]
        centroids = X[np.random.choice(n_samples, k, replace=False)]
        
        for _ in range(iterations):
            # Assign clusters
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

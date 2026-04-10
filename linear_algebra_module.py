"""
Linear Algebra Module - Linear Independence, Gram-Schmidt, Projections, Least Squares
"""

import numpy as np


class LinearAlgebraAnalyzer:

    @staticmethod
    def find_independent_basis(matrix):
        A = matrix.copy()
        n_users = A.shape[0]
        rank = np.linalg.matrix_rank(A)

        is_independent = np.zeros(n_users, dtype=bool)
        selected = []
        current_rank = 0

        for i in range(n_users):
            candidate = selected + [i]
            new_rank = np.linalg.matrix_rank(A[candidate, :])
            if new_rank > current_rank:
                is_independent[i] = True
                selected.append(i)
                current_rank = new_rank
            if current_rank == rank:
                break

        return A[selected, :], selected, is_independent

    @staticmethod
    def gram_schmidt(basis_vectors):
        vectors = basis_vectors.astype(float).copy()
        n, m = vectors.shape
        Q = np.zeros_like(vectors)

        for i in range(n):
            u = vectors[i].copy()
            for j in range(i):
                u -= np.dot(u, Q[j]) * Q[j]  # subtract projection onto each previous vector
            norm = np.linalg.norm(u)
            Q[i] = u / norm if norm > 1e-10 else np.zeros(m)

        return Q

    @staticmethod
    def orthogonal_projection(matrix, Q):
        A = matrix.astype(float)
        projection_matrix = Q.T @ Q  # P = QᵀQ, shape (15x15)
        A_projected = A @ projection_matrix
        return A_projected, projection_matrix

    @staticmethod
    def least_squares_approximation(matrix, Q):
        A = matrix.astype(float)
        X = A @ Q.T           # coefficients: minimises ||A - XQ||²
        A_approx = X @ Q      # reconstruction: A_approx = AQᵀQ
        reconstruction_error = np.linalg.norm(A - A_approx, 'fro')
        return A_approx, reconstruction_error, X

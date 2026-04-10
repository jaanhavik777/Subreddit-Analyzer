"""
r/PESU Analysis Using Linear Algebra
PageRank & SVD on Synthetic Community Data

Linear Algebra Pipeline:
  Real-World Data
    -> Matrix Representation
    -> RREF / Gaussian Elimination
    -> Rank & Nullity
    -> Linear Independence & Basis Selection
    -> Gram-Schmidt Orthogonalization
    -> Orthogonal Projections
    -> Least Squares Approximation
    -> Eigenvalues & Eigenvectors  (PageRank)
    -> SVD & Diagonalization       (Community Detection)
    -> Final Output
"""

import numpy as np
import pandas as pd
from pagerank_module import PageRankAnalyzer
from svd_module import SVDAnalyzer
from data_loader import DataLoader
from linear_algebra_module import LinearAlgebraAnalyzer


class PESUAnalyzer:

    def __init__(self):
        self.user_comment_matrix = None
        self.users = None
        self.pagerank_scores = None

    def build_matrix(self, df, users):
        matrix = df.pivot_table(
            index='user',
            columns='comment_id',
            values='interaction_strength',
            fill_value=0,
            aggfunc='sum'
        )
        matrix = matrix.reindex(users)
        self.user_comment_matrix = matrix
        self.users = users
        return matrix

    def analyze(self):
        df, users = DataLoader.load_from_file('pesu_data.json')
        DataLoader.get_summary(df, users)
        matrix = self.build_matrix(df, users)
        A = matrix.values.astype(float)

        print("\n" + "=" * 70)
        print("LINEAR ALGEBRA PIPELINE - r/PESU")
        print("=" * 70)

        print("\nSTEP 1 - MATRIX REPRESENTATION (10x15):")
        print("   Rows = Users | Columns = Comment IDs | Values = Interaction Strength")
        print(matrix.to_string())

        print("\nSTEP 2 - RREF (Reduced Row Echelon Form):")
        rref_matrix, pivot_columns = DataLoader.compute_rref(matrix)
        print(f"   Pivot columns: {pivot_columns}")
        print(f"   Number of pivots = {len(pivot_columns)} (= Rank of matrix)")

        print("\nSTEP 3 - RANK & NULLITY:")
        rank, nullity = DataLoader.compute_rank_nullity(matrix)
        print(f"   Rank    = {rank}  -> {rank} truly independent user interaction patterns")
        print(f"   Nullity = {nullity}  -> {nullity} redundant/dependent comment dimensions")
        print(f"   Rank-Nullity Theorem: {rank} + {nullity} = {rank + nullity} (= no. of columns)")

        print("\nSTEP 4 - LINEAR INDEPENDENCE & BASIS SELECTION:")
        basis_vectors, basis_indices, is_independent = LinearAlgebraAnalyzer.find_independent_basis(A)
        independent_users = [users[i] for i in basis_indices]
        dependent_users = [users[i] for i in range(len(users)) if not is_independent[i]]
        print(f"   Independent users (basis): {independent_users}")
        if dependent_users:
            print(f"   Dependent users (excluded): {dependent_users}")
        else:
            print(f"   All 10 users are linearly independent -> basis spans full interaction space")
        print(f"   Basis size = {len(basis_indices)} vectors in R^15")

        print("\nSTEP 5 - GRAM-SCHMIDT ORTHOGONALIZATION:")
        Q = LinearAlgebraAnalyzer.gram_schmidt(basis_vectors)
        is_identity = np.allclose(Q @ Q.T, np.eye(len(basis_vectors)), atol=1e-6)
        print(f"   Converted {len(basis_vectors)} basis vectors -> orthonormal basis Q")
        print(f"   Orthonormality check (QQ^T = I): {'Passed' if is_identity else 'Failed'}")

        print("\nSTEP 6 - ORTHOGONAL PROJECTIONS:")
        A_projected, P = LinearAlgebraAnalyzer.orthogonal_projection(A, Q)
        projection_error = np.linalg.norm(A - A_projected, 'fro')
        print(f"   Projection matrix P = Q^TQ built (15x15)")
        print(f"   Projected all 10 user vectors onto the orthogonal subspace")
        print(f"   Projection error ||A - A_proj||_F = {projection_error:.6f}")

        print("\nSTEP 7 - LEAST SQUARES APPROXIMATION:")
        A_approx, recon_error, X = LinearAlgebraAnalyzer.least_squares_approximation(A, Q)
        print(f"   Minimised ||A - XQ||^2")
        print(f"   Coefficient matrix X = AQ^T computed")
        print(f"   Reconstruction error ||A - A_approx||_F = {recon_error:.6f}")

        print("\nSTEP 8 - PAGERANK (Eigenvalues & Eigenvectors):")
        self.pagerank_scores = PageRankAnalyzer.compute(matrix)
        most_influential_user, score = PageRankAnalyzer.get_most_influential(self.pagerank_scores, users)
        print(f"   Built 10x10 user-to-user transition matrix")
        print(f"   Power iteration -> dominant eigenvector converged")
        sorted_users = sorted(zip(users, self.pagerank_scores), key=lambda x: -x[1])
        print(f"   PageRank scores (top 5):")
        for u, s in sorted_users[:5]:
            print(f"      {u}: {s:.6f}")

        print("\nSTEP 9 - SVD & COMMUNITY DETECTION:")
        clusters, communities = SVDAnalyzer.detect_communities(matrix)
        U, S, V, Vt = SVDAnalyzer.compute(matrix)
        print(f"   SVD decomposition: A = U*Sigma*V^T")
        print(f"   Top-3 singular values: {np.round(S[:3], 4)}")
        print(f"   Users projected into 3D space -> K-Means applied")

        print("\n" + "=" * 70)
        print("ANALYSIS RESULTS - r/PESU")
        print("=" * 70)

        print("\nMOST INFLUENTIAL USER:")
        print(f"   {most_influential_user} (PageRank Score: {score:.6f})")

        print(f"\nHIDDEN COMMUNITY CLUSTERS:")
        for cluster_num, members in communities.items():
            print(f"\n   Community {cluster_num}:")
            print(f"      {', '.join(members)}")


def main():
    analyzer = PESUAnalyzer()
    analyzer.analyze()


if __name__ == "__main__":
    main()

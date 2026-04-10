"""
Data Loader Module - Loads r/PESU data from JSON file
Includes Matrix Representation, RREF, Rank & Nullity analysis
"""

import json
import numpy as np
import pandas as pd
from sympy import Matrix


class DataLoader:

    @staticmethod
    def load_from_file(filename='pesu_data.json'):
        with open(filename, 'r') as f:
            data_dict = json.load(f)

        data = []
        for comment in data_dict['comments']:
            comment_id = comment['comment_id']
            for interaction in comment['interactions']:
                data.append({
                    'user': interaction['user'],
                    'comment_id': comment_id,
                    'interaction_strength': interaction['interaction_strength']
                })

        df = pd.DataFrame(data)
        users = sorted(df['user'].unique().tolist())
        return df, users

    @staticmethod
    def compute_rref(matrix):
        A = Matrix(matrix.values.tolist())
        rref_matrix, pivot_columns = A.rref()
        return rref_matrix, pivot_columns

    @staticmethod
    def compute_rank_nullity(matrix):
        rank = np.linalg.matrix_rank(matrix.values)
        nullity = matrix.shape[1] - rank  # nullity = columns - rank
        return rank, nullity

    @staticmethod
    def get_summary(df, users):
        print(f"Loaded r/PESU data:")
        print(f"  - Users: {len(users)}")
        print(f"  - Total comments: {df['comment_id'].nunique()}")
        print(f"  - Total interactions: {len(df)}")
        print(f"  - Users: {', '.join(users[:5])}...")

"""
Data Loader Module - Loads r/PESU data from JSON file
"""

import json
import pandas as pd


class DataLoader:
    """Load and parse r/PESU community data from JSON"""
    
    @staticmethod
    def load_from_file(filename='pesu_data.json'):
        """
        Load r/PESU data from JSON file.
        
        Args:
            filename: Path to JSON file
        
        Returns:
            df: DataFrame with columns [user, comment_id, interaction_strength]
            users: List of unique usernames
        """
        with open(filename, 'r') as f:
            data_dict = json.load(f)
        
        # Parse JSON into flat structure
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
    def get_summary(df, users):
        """Print data summary"""
        print(f"Loaded r/PESU data:")
        print(f"  - Users: {len(users)}")
        print(f"  - Total comments: {df['comment_id'].nunique()}")
        print(f"  - Total interactions: {len(df)}")
        print(f"  - Users: {', '.join(users[:5])}...")

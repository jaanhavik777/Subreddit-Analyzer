"""
r/PESU Analysis Using Linear Algebra
PageRank & SVD on Synthetic Community Data

Main orchestrator that uses modular components
Loads data from pesu_data.json
"""

import numpy as np
import pandas as pd
from pagerank_module import PageRankAnalyzer
from svd_module import SVDAnalyzer
from data_loader import DataLoader


class PESUAnalyzer:
    """Main analyzer orchestrating all components"""
    
    def __init__(self):
        self.user_comment_matrix = None
        self.users = None
        self.pagerank_scores = None
    
    def build_matrix(self, df, users):
        """Build user-comment interaction matrix"""
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
        """Run full analysis: PageRank + SVD"""
        
        # Load data from file
        df, users = DataLoader.load_from_file('pesu_data.json')
        matrix = self.build_matrix(df, users)
        
        # PageRank analysis
        self.pagerank_scores = PageRankAnalyzer.compute(matrix)
        most_influential_user, score = PageRankAnalyzer.get_most_influential(
            self.pagerank_scores, users
        )
        
        # SVD community detection
        clusters, communities = SVDAnalyzer.detect_communities(matrix)
        
        # Print results
        print("\n" + "="*70)
        print("ANALYSIS RESULTS - r/PESU")
        print("="*70)
        
        print("\n🏆 MOST INFLUENTIAL USER:")
        print(f"   {most_influential_user} (PageRank Score: {score:.6f})")
        
        print(f"\n🔍 HIDDEN COMMUNITY CLUSTERS:")
        for cluster_num, members in communities.items():
            print(f"\n   Community {cluster_num}:")
            print(f"      {', '.join(members)}")


def main():
    """Main entry point"""
    analyzer = PESUAnalyzer()
    analyzer.analyze()


if __name__ == "__main__":
    main()
"""
Day 2: Data Loader
Loads Kaggle dataset and prepares it for analysis
"""

import pandas as pd
import os
from pathlib import Path

class KaggleDataLoader:
    def __init__(self, data_path='data/raw/'):
        """Initialize the data loader"""
        self.data_path = data_path
        self.df = None
        self.original_df = None
    
    def find_csv_file(self):
        """Find CSV file in data/raw folder"""
        csv_files = [f for f in os.listdir(self.data_path) if f.endswith('.csv')]
        
        if not csv_files:
            raise FileNotFoundError(f"No CSV files found in {self.data_path}")
        
        return os.path.join(self.data_path, csv_files[0])
    
    def load_data(self):
        """Load the dataset"""
        try:
            file_path = self.find_csv_file()
            print(f"📂 Loading dataset from: {file_path}")
            
            self.df = pd.read_csv(file_path)
            self.original_df = self.df.copy()
            
            print(f"✅ Dataset loaded successfully!")
            print(f"   Shape: {self.df.shape}")
            
            return self.df
        
        except Exception as e:
            print(f"❌ Error loading dataset: {e}")
            return None
    
    def get_column_names(self):
        """Get all column names"""
        if self.df is None:
            print("❌ No data loaded. Call load_data() first.")
            return None
        return list(self.df.columns)
    
    def get_data_summary(self):
        """Get summary of the dataset"""
        if self.df is None:
            print("❌ No data loaded. Call load_data() first.")
            return None
        
        summary = {
            'shape': self.df.shape,
            'columns': self.get_column_names(),
            'dtypes': self.df.dtypes.to_dict(),
            'missing_values': self.df.isnull().sum().to_dict(),
            'duplicates': self.df.duplicated().sum()
        }
        return summary
    
    def save_processed_data(self, filename='processed_data.csv'):
        """Save processed data to processed folder"""
        if self.df is None:
            print("❌ No data to save. Process data first.")
            return None
        
        output_path = 'data/processed/'
        Path(output_path).mkdir(parents=True, exist_ok=True)
        
        file_path = os.path.join(output_path, filename)
        self.df.to_csv(file_path, index=False)
        
        print(f"✅ Data saved to: {file_path}")
        return file_path
    
    def get_data(self):
        """Return the dataframe"""
        return self.df


# Main execution
if __name__ == "__main__":
    print("=" * 70)
    print("DATA LOADER - KAGGLE NAMMAMETRO DATASET")
    print("=" * 70)
    
    # Initialize loader
    loader = KaggleDataLoader(data_path='data/raw/')
    
    # Load data
    df = loader.load_data()
    
    if df is not None:
        # Get summary
        print("\n📊 DATA SUMMARY:")
        summary = loader.get_data_summary()
        
        print(f"\n   Shape: {summary['shape']}")
        print(f"\n   Columns: {summary['columns']}")
        print(f"\n   Data Types:\n{summary['dtypes']}")
        
        if any(summary['missing_values'].values()):
            print(f"\n   Missing Values:\n{summary['missing_values']}")
        else:
            print(f"\n   ✅ No missing values!")
        
        print(f"\n   Duplicates: {summary['duplicates']}")
        
        # Save processed data (copy)
        print("\n💾 Saving processed data...")
        loader.save_processed_data('nammametro_processed_day2.csv')
        
        print("\n" + "=" * 70)
        print("✅ Day 2 Data Loading Complete!")
        print("=" * 70)
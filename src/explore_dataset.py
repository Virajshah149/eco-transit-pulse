"""
Explore Kaggle Dataset
This script loads and displays the structure of the downloaded dataset
"""

import pandas as pd
import os

def explore_dataset(file_path):
    """Load and explore the dataset"""
    
    print("=" * 70)
    print("EXPLORING KAGGLE DATASET")
    print("=" * 70)
    
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Basic info
    print(f"\n📊 DATASET SHAPE: {df.shape}")
    print(f"   Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    
    # Column names and types
    print(f"\n📋 COLUMN NAMES & TYPES:")
    print(df.dtypes)
    
    # First few rows
    print(f"\n📈 FIRST 5 ROWS:")
    print(df.head())
    
    # Last few rows
    print(f"\n📉 LAST 5 ROWS:")
    print(df.tail())
    
    # Missing values
    print(f"\n❌ MISSING VALUES:")
    missing = df.isnull().sum()
    if missing.sum() == 0:
        print("   ✅ No missing values!")
    else:
        print(missing[missing > 0])
    
    # Basic statistics
    print(f"\n📊 BASIC STATISTICS:")
    print(df.describe())
    
    # Unique values for categorical columns
    print(f"\n🏷️  CATEGORICAL COLUMNS:")
    for col in df.select_dtypes(include='object').columns:
        print(f"   {col}: {df[col].nunique()} unique values")
        print(f"      Sample: {df[col].unique()[:5]}")
    
    # Date range
    if 'date' in df.columns or 'Date' in df.columns:
        date_col = 'date' if 'date' in df.columns else 'Date'
        print(f"\n📅 DATE RANGE:")
        print(f"   From: {df[date_col].min()}")
        print(f"   To: {df[date_col].max()}")
    
    print("\n" + "=" * 70)
    
    return df

if __name__ == "__main__":
    # Find the CSV file in data/raw folder
    raw_data_path = 'data/raw/'
    
    # List all CSV files
    csv_files = [f for f in os.listdir(raw_data_path) if f.endswith('.csv')]
    
    if not csv_files:
        print("❌ No CSV files found in data/raw/")
        print(f"   Please download the dataset and place it in {raw_data_path}")
    else:
        # Use the first CSV file found
        file_path = os.path.join(raw_data_path, csv_files[0])
        print(f"📁 Using file: {csv_files[0]}\n")
        
        # Explore the dataset
        df = explore_dataset(file_path)
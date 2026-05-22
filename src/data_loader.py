import os
import pandas as pd

class AutoInsuranceDataLoader:
    """Handles secure loading and initial type-casting of the ACIS insurance dataset."""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Insurance data file not found at: {file_path}")
            
    def load_data(self) -> pd.DataFrame:
        """Loads dataset and performs standard structural adjustments."""
        print(f"Reading dataset from {self.file_path}...")
        df = pd.read_csv(self.file_path)
        
        # Standardize structural date/temporal groupings
        if 'TransactionMonth' in df.columns:
            df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])
            
        return df
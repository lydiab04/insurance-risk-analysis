import pandas as pd
import numpy as np

class InsuranceEDAAnalyzer:
    """Encapsulates descriptive statistics, financial KPIs, and deep risk metrics profiling."""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self._calculate_base_metrics()
        
    def _calculate_base_metrics(self):
        """Pre-calculates core insurance KPIs anchored to the portfolio analysis."""
        self.df['TotalPremium'] = pd.to_numeric(self.df['TotalPremium'], errors='coerce').fillna(0)
        self.df['TotalClaims'] = pd.to_numeric(self.df['TotalClaims'], errors='coerce').fillna(0)
        
        # Handle zero premium edge-cases gracefully to protect against Division by Zero errors
        self.df['LossRatio'] = np.where(
            self.df['TotalPremium'] > 0, 
            self.df['TotalClaims'] / self.df['TotalPremium'], 
            0.0
        )
        self.df['Margin'] = self.df['TotalPremium'] - self.df['TotalClaims']

    def get_portfolio_summary(self) -> dict:
        """Computes executive high-level metrics for the entire portfolio."""
        total_premium = self.df['TotalPremium'].sum()
        total_claims = self.df['TotalClaims'].sum()
        overall_loss_ratio = total_claims / total_premium if total_premium > 0 else 0
        
        return {
            "Total Portfolio Volume (Rows)": self.df.shape[0],
            "Total Written Premium (ZAR)": total_premium,
            "Total Incurred Claims (ZAR)": total_claims,
            "Overall Portfolio Loss Ratio": overall_loss_ratio,
            "Net Profit Margin (ZAR)": total_premium - total_claims
        }

    def assess_data_quality(self) -> pd.DataFrame:
        """Profiles missing data points across features."""
        missing_count = self.df.isnull().sum()
        missing_pct = (missing_count / len(self.df)) * 100
        quality_df = pd.DataFrame({
            'Missing Values': missing_count,
            'Percentage (%)': missing_pct,
            'DataType': self.df.dtypes
        })
        return quality_df[quality_df['Missing Values'] > 0].sort_values(by='Missing Values', ascending=False)

    def analyze_risk_by_dimension(self, dimension: str) -> pd.DataFrame:
        """Aggregates financial exposure metrics based on an input dimension."""
        if dimension not in self.df.columns:
            raise ValueError(f"Column '{dimension}' does not exist in dataset.")
            
        summary = self.df.groupby(dimension).agg(
            Total_Premium=('TotalPremium', 'sum'),
            Total_Claims=('TotalClaims', 'sum'),
            Policy_Count=(dimension, 'count')
        ).reset_index()
        
        summary['LossRatio'] = np.where(
            summary['Total_Premium'] > 0,
            summary['Total_Claims'] / summary['Total_Premium'],
            0.0
        )
        summary['Average_Premium'] = summary['Total_Premium'] / summary['Policy_Count']
        return summary.sort_values(by='LossRatio', ascending=False)

    def get_temporal_trends(self) -> pd.DataFrame:
        """Traces monthly movements in risk exposure over the 18-month duration."""
        if 'TransactionMonth' not in self.df.columns:
            # Fallback if column name is different
            return pd.DataFrame()
            
        trend = self.df.groupby('TransactionMonth').agg(
            Total_Premium=('TotalPremium', 'sum'),
            Total_Claims=('TotalClaims', 'sum'),
            Claim_Count=('TotalClaims', lambda x: (x > 0).sum()),
            Exposure_Units=('PolicyID', 'count')
        ).reset_index()
        
        trend['LossRatio'] = trend['Total_Claims'] / trend['Total_Premium']
        trend['Claim_Frequency (%)'] = (trend['Claim_Count'] / trend['Exposure_Units']) * 100
        trend['Claim_Severity'] = np.where(
            trend['Claim_Count'] > 0,
            trend['Total_Claims'] / trend['Claim_Count'],
            0.0
        )
        return trend.sort_values('TransactionMonth')
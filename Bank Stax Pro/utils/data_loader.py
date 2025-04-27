import pandas as pd
from typing import List, Dict

def load_data(file_path: str) -> pd.DataFrame:
    """Load and validate the data file containing bank financial data."""
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path, engine='openpyxl')
        
        if 'Bank Name' not in df.columns:
            raise ValueError("Missing required column: Bank Name")
            
        return df
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")

def get_financial_ratios(df: pd.DataFrame) -> List[str]:
    """Get list of available financial ratios."""
    financial_ratios = [
        'PAT',
        'Depreciation',
        'Total Liabilities (excluding equity)',
        'Cash & cash equivalents',
        'Total Assets',
        'Current Assets',
        'Current Liabilities',
        'Accounts Receivables',
        'Marketable Securities',
        'Core Deposits',
        'Total Deposits',
        'Loans',
        'Non performing assets'
    ]
    return [col for col in financial_ratios if col in df.columns]

def get_capital_metrics(df: pd.DataFrame) -> List[str]:
    """Get list of capital-related metrics."""
    capital_metrics = [
        'Tier-1 Capital',
        'Tier-2 capital',
        'Risk weighted assets',
        'Common Equity Tier 1 Capital',
        'Tier 1 Capital Ratio',
        'Total Capital',
        'Leverage Ratio',
        'Supplementary Tier 1',
        'Capital Conservation'
    ]
    return [col for col in capital_metrics if col in df.columns]

def get_stress_metrics(df: pd.DataFrame) -> List[str]:
    """Get list of stress test metrics."""
    stress_metrics = [
        'Common Equity Tier 1 Capital',
        'Tier 1 Capital Ratio',
        'Total Capital',
        'Leverage Ratio'
    ]
    return [col for col in stress_metrics if col in df.columns]

def get_market_standards() -> Dict[str, float]:
    """Get market standard values for different metrics."""
    return {
        'PAT': 10000,
        'Core Deposits': 0.80,
        'Non performing assets': 0.015,
        'Tier-1 Capital': 11.0,
        'Tier-2 capital': 2.0,
        'Common Equity Tier 1 Capital': 11.0,
        'Tier 1 Capital Ratio': 10.5,
        'Total Capital': 15.0,
        'Leverage Ratio': 7.5,
        'Supplementary Tier 1': 2.0,
        'Capital Conservation': 2.5,
        'Current Ratio': 1.5,
        'Total Assets': 100000,
        'Loans': 50000
    }

def check_stress_threshold(metric: str, value: float) -> bool:
    """Check if a metric passes its threshold."""
    standards = get_market_standards()
    
    # Metrics where lower is better
    lower_is_better = ['Non performing assets']
    
    if metric in lower_is_better:
        return value <= standards.get(metric, float('inf'))
    else:
        return value >= standards.get(metric, float('-inf'))

def get_metric_type(metric: str) -> str:
    """Get the type of metric (financial, stress, or capital)."""
    capital_metrics = [
        'Tier-1 Capital',
        'Tier-2 capital',
        'Risk weighted assets',
        'Common Equity Tier 1 Capital',
        'Tier 1 Capital Ratio',
        'Total Capital',
        'Leverage Ratio',
        'Supplementary Tier 1',
        'Capital Conservation'
    ]
    
    stress_metrics = [
        'Common Equity Tier 1 Capital',
        'Tier 1 Capital Ratio',
        'Total Capital',
        'Leverage Ratio'
    ]
    
    if metric in stress_metrics:
        return 'stress'
    elif metric in capital_metrics:
        return 'capital'
    else:
        return 'financial'

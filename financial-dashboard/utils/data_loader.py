import pandas as pd
from typing import Tuple, List

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load and validate the data file containing bank financial data.
    
    Args:
        file_path (str): Path to the data file (Excel or CSV)
        
    Returns:
        pd.DataFrame: Validated dataframe containing bank data
    """
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path, engine='openpyxl')
        
        # Validate required columns
        required_columns = [
            'Bank Name',
            'Liquidity Ratio',
            'Capital Adequacy Ratio',
            'ROE',
            'Post Stress CET1 Ratio',
            'Stress Loss %',
            'Minimum Capital Requirement'
        ]
        
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
            
        return df
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")

def get_financial_ratios() -> List[str]:
    """
    Get list of available financial ratios.
    
    Returns:
        List[str]: List of financial ratio names
    """
    return ['Liquidity Ratio', 'Capital Adequacy Ratio', 'ROE']

def get_stress_metrics() -> List[str]:
    """
    Get list of available CCAR stress test metrics.
    
    Returns:
        List[str]: List of stress test metric names
    """
    return ['Post Stress CET1 Ratio', 'Stress Loss %']

def check_stress_threshold(metric: str, value: float) -> bool:
    """
    Check if a stress metric passes regulatory threshold.
    
    Args:
        metric (str): Name of the stress metric
        value (float): Value to check
        
    Returns:
        bool: True if passes threshold, False otherwise
    """
    thresholds = {
        'Post Stress CET1 Ratio': 4.5,  # Minimum required CET1 ratio
        'Stress Loss %': 3.0   # Maximum acceptable loss percentage
    }
    
    if metric == 'Post Stress CET1 Ratio':
        return value >= thresholds[metric]
    elif metric == 'Stress Loss %':
        return value <= thresholds[metric]
    return True

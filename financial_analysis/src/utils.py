import pandas as pd
import numpy as np
import plotly.graph_objects as go

def load_data():
    """Load and prepare the bank data"""
    try:
        df = pd.read_excel('../data/bank_data.xlsx')
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def calculate_grade(value, series):
    """Calculate grade based on percentiles"""
    p75 = np.percentile(series, 75)
    p25 = np.percentile(series, 25)
    
    if value >= p75:
        return 'A'
    elif value >= p25:
        return 'B'
    else:
        return 'C'

def get_role_metrics(role):
    """Return relevant metrics based on user role"""
    depositor_metrics = {
        'Capital Ratio': {'threshold': 12, 'description': 'Measures bank\'s capital strength'},
        'Liquidity Ratio': {'threshold': 100, 'description': 'Indicates bank\'s ability to meet short-term obligations'},
        'NPL Ratio': {'threshold': 3, 'description': 'Shows quality of loan portfolio (lower is better)'},
        'ROE': {'threshold': 15, 'description': 'Indicates profitability and efficiency'}
    }
    
    borrower_metrics = {
        'Interest Coverage Ratio': {'threshold': 2.5, 'description': 'Ability to pay interest on debt'},
        'Debt Service Coverage Ratio': {'threshold': 1.8, 'description': 'Ability to service total debt'},
        'Cost-to-Income Ratio': {'threshold': 55, 'description': 'Operational efficiency (lower is better)'},
        'Loan-to-Deposit Ratio': {'threshold': 85, 'description': 'Lending practice sustainability'}
    }
    
    return depositor_metrics if role == "Depositor" else borrower_metrics

def create_radar_chart(bank_data, selected_bank, metrics):
    """Create a radar chart for the selected bank's metrics"""
    bank_values = []
    metric_names = list(metrics.keys())
    
    for metric in metric_names:
        bank_values.append(bank_data[bank_data['Bank Name'] == selected_bank][metric].values[0])
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=bank_values,
        theta=metric_names,
        fill='toself',
        name=selected_bank
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(bank_values) * 1.2]
            )),
        showlegend=True,
        template="plotly_dark",
        title=f"Financial Metrics Radar Chart - {selected_bank}"
    )
    
    return fig

def get_metric_analysis(bank_data, selected_bank, metrics):
    """Generate detailed analysis for each metric"""
    analysis = {}
    bank_row = bank_data[bank_data['Bank Name'] == selected_bank]
    
    for metric, info in metrics.items():
        value = bank_row[metric].values[0]
        grade = calculate_grade(value, bank_data[metric])
        
        analysis[metric] = {
            'value': value,
            'grade': grade,
            'description': info['description'],
            'threshold': info['threshold'],
            'status': 'Good' if value >= info['threshold'] else 'Needs Improvement'
        }
    
    return analysis

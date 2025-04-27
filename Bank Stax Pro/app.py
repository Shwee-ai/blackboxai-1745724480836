import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path
import sys

# Add the project root to Python path
sys.path.append(str(Path(__file__).parent))

from utils.styling import get_css_styles, get_plotly_config, get_color_scale
from utils.data_loader import (
    load_data,
    check_stress_threshold,
    get_market_standards
)

# Page configuration
st.set_page_config(
    page_title="Bank Stax Pro",
    page_icon="📊",
    layout="wide"
)

# Apply custom styling
st.markdown(get_css_styles(), unsafe_allow_html=True)

def create_bar_chart(df: pd.DataFrame, metric: str) -> go.Figure:
    colors = get_color_scale()
    standards = get_market_standards()

    bar_colors = [colors['neutral']] * len(df)

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=df['Bank Name'],
            y=df[metric],
            marker_color=bar_colors,
            text=df[metric].round(3),
            textposition='auto',
            name='Bank Values'
        )
    )

    if metric in standards:
        fig.add_trace(
            go.Scatter(
                x=df['Bank Name'],
                y=[standards[metric]] * len(df),
                mode='lines',
                name='Market Standard',
                line=dict(color='red', width=2, dash='dash'),
            )
        )

    config = get_plotly_config()
    fig.update_layout(
        **config['layout'],
        title=f"{metric} by Bank",
        xaxis_title="Banks",
        yaxis_title=metric,
        height=400
    )

    return fig

def main():
    st.markdown('<h1 class="main-title">Bank Stax Pro</h1>', unsafe_allow_html=True)

    try:
        df = pd.read_excel("data/bank_data_processed.xlsx")

        bank_names = df['Bank Name'].tolist()
        selected_bank = st.selectbox("Select Bank for Peer Comparison", bank_names)

        key_financials = [
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
            'Non performing assets',
            'Tier-1 Capital',
            'Tier-2 capital',
            'Risk weighted assets'
        ]
        available_financials = [f for f in key_financials if f in df.columns]
        selected_financial = st.selectbox("Select Key Financial", available_financials)

        fig_financial = create_bar_chart(df, selected_financial)
        st.plotly_chart(fig_financial, use_container_width=True)

        # Add Key Metrics section
        st.subheader("Key Metrics")
        key_metrics = [
            'Core Deposits to Total Deposits',
            'NPAs to Total Loans',
            'Liquidity Ratio',
            'Capital Adequacy Ratio',
            'Solvency Ratio',
            'Loans to Deposit Ratio'
        ]
        available_metrics = [m for m in key_metrics if m in df.columns]
        selected_metric = st.selectbox("Select Key Metric", available_metrics)

        fig_metric = create_bar_chart(df, selected_metric)
        st.plotly_chart(fig_metric, use_container_width=True)

        # Add CCAR Stress Test Analysis section
        st.subheader("CCAR Stress Test Analysis")
        ccar_metrics = [
            'Common Equity Tier 1 Capital',
            'Tier 1 Capital Ratio',
            'Total Capital',
            'Leverage Ratio',
            'Supplementary Tier 1'
        ]
        available_ccar = [c for c in ccar_metrics if c in df.columns]
        selected_ccar = st.selectbox("Select CCAR Metric", available_ccar)

        fig_ccar = create_bar_chart(df, selected_ccar)
        st.plotly_chart(fig_ccar, use_container_width=True)

    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.stop()

if __name__ == "__main__":
    main()

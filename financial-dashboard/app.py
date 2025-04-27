import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path
import sys

# Add the project root to Python path
sys.path.append(str(Path(__file__).parent))

from utils.data_loader import (
    load_data, 
    get_financial_ratios, 
    get_stress_metrics, 
    check_stress_threshold
)
from utils.styling import get_css_styles, get_plotly_config, get_color_scale

# Page configuration
st.set_page_config(
    page_title="Bank Financial Analysis",
    page_icon="📊",
    layout="wide"
)

# Apply custom styling
st.markdown(get_css_styles(), unsafe_allow_html=True)

def create_bar_chart(df: pd.DataFrame, metric: str, is_stress_metric: bool = False) -> go.Figure:
    """
    Create a bar chart for the selected metric.
    
    Args:
        df (pd.DataFrame): Data frame containing bank data
        metric (str): Selected metric to display
        is_stress_metric (bool): Whether the metric is a stress test metric
        
    Returns:
        go.Figure: Plotly figure object
    """
    colors = get_color_scale()
    
    if is_stress_metric:
        bar_colors = [
            colors['pass'] if check_stress_threshold(metric, value) else colors['fail']
            for value in df[metric]
        ]
    else:
        bar_colors = [colors['neutral']] * len(df)
    
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=df['Bank Name'],
            y=df[metric],
            marker_color=bar_colors,
            text=df[metric].round(2),
            textposition='auto',
        )
    )
    
    # Update layout with custom styling
    config = get_plotly_config()
    fig.update_layout(
        **config['layout'],
        title=f"{metric} by Bank",
        xaxis_title="Banks",
        yaxis_title=metric,
        showlegend=False,
        height=400
    )
    
    return fig

def main():
    """Main application function"""
    
    # Title
    st.markdown('<h1 class="main-title">Bank Financial Analysis Dashboard</h1>', unsafe_allow_html=True)
    
    try:
        # Load data
        df = load_data("data/bank_data.csv")
        
        # Create two columns for the dropdowns
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Financial Ratios Analysis")
            selected_ratio = st.selectbox(
                "Select Financial Ratio",
                options=get_financial_ratios(),
                key="financial_ratio"
            )
            
            # Display financial ratio chart
            with st.container():
                st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                fig_ratio = create_bar_chart(df, selected_ratio)
                st.plotly_chart(fig_ratio, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.subheader("CCAR Stress Test Analysis")
            selected_stress = st.selectbox(
                "Select Stress Test Metric",
                options=get_stress_metrics(),
                key="stress_metric"
            )
            
            # Display stress test chart
            with st.container():
                st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                fig_stress = create_bar_chart(df, selected_stress, is_stress_metric=True)
                st.plotly_chart(fig_stress, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
        
        # Add metric cards
        st.subheader("Key Insights")
        metric_cols = st.columns(3)
        
        # Display key metrics
        with metric_cols[0]:
            st.markdown(
                f'''<div class="metric-card">
                    <h3>Average {selected_ratio}</h3>
                    <p>{df[selected_ratio].mean():.2f}</p>
                </div>''',
                unsafe_allow_html=True
            )
        
        with metric_cols[1]:
            st.markdown(
                f'''<div class="metric-card">
                    <h3>Highest {selected_ratio}</h3>
                    <p>{df[selected_ratio].max():.2f}</p>
                </div>''',
                unsafe_allow_html=True
            )
        
        with metric_cols[2]:
            st.markdown(
                f'''<div class="metric-card">
                    <h3>Lowest {selected_ratio}</h3>
                    <p>{df[selected_ratio].min():.2f}</p>
                </div>''',
                unsafe_allow_html=True
            )
            
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.stop()

if __name__ == "__main__":
    main()

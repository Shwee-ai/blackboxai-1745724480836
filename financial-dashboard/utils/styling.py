def get_css_styles() -> str:
    """
    Returns custom CSS styles for the Streamlit app.
    
    Returns:
        str: CSS styles as a string
    """
    return """
    <style>
        /* Main gradient background */
        .stApp {
            background: linear-gradient(to bottom right, #1a1a2e, #16213e, #1a1a2e);
        }
        
        /* Custom styling for titles */
        .main-title {
            color: #ffffff;
            font-size: 2.5rem;
            font-weight: 700;
            text-align: center;
            margin-bottom: 2rem;
            padding: 1rem;
            background: linear-gradient(120deg, #2980b9, #2c3e50);
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        /* Styling for metric cards */
        .metric-card {
            background: rgba(255, 255, 255, 0.1);
            padding: 1.5rem;
            border-radius: 10px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 1rem;
        }
        
        /* Custom styling for dropdowns */
        .stSelectbox > div > div {
            background-color: rgba(255, 255, 255, 0.05) !important;
            border-color: rgba(255, 255, 255, 0.1) !important;
        }
        
        /* Custom styling for charts */
        .chart-container {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 1rem;
            margin: 1rem 0;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        /* Responsive design adjustments */
        @media screen and (max-width: 768px) {
            .main-title {
                font-size: 1.8rem;
                padding: 0.8rem;
            }
            
            .metric-card {
                padding: 1rem;
            }
        }
    </style>
    """

def get_plotly_config() -> dict:
    """
    Returns configuration for Plotly charts.
    
    Returns:
        dict: Plotly chart configuration
    """
    return {
        'layout': {
            'template': 'plotly_dark',
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'font': {
                'color': '#ffffff'
            },
            'margin': {'t': 50, 'b': 50, 'l': 50, 'r': 50}
        }
    }

def get_color_scale() -> dict:
    """
    Returns color scales for different metrics.
    
    Returns:
        dict: Color configurations for different metrics
    """
    return {
        'pass': '#00cc96',  # Green for passing metrics
        'fail': '#ef553b',  # Red for failing metrics
        'neutral': '#636efa'  # Blue for neutral metrics
    }

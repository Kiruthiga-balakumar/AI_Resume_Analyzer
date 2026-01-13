"""
Chart generation for the dashboard.
"""

import plotly.graph_objects as go
import plotly.express as px
from typing import List

def create_match_gauge(score: float) -> go.Figure:
    """
    Create a gauge chart for match score.

    Args:
        score (float): Match score percentage.

    Returns:
        go.Figure: Plotly gauge figure.
    """
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': "Match Score"},
        gauge={'axis': {'range': [0, 100]},
               'bar': {'color': "darkblue"},
               'steps': [
                   {'range': [0, 50], 'color': "red"},
                   {'range': [50, 75], 'color': "yellow"},
                   {'range': [75, 100], 'color': "green"}]}
    ))
    fig.update_layout(height=300)
    return fig

def create_skills_bar_chart(matched: List[str], missing: List[str]) -> go.Figure:
    """
    Create a bar chart for matched and missing skills.

    Args:
        matched (List[str]): List of matched skills.
        missing (List[str]): List of missing skills.

    Returns:
        go.Figure: Plotly bar chart figure.
    """
    categories = ['Matched Skills', 'Missing Skills']
    values = [len(matched), len(missing)]

    fig = px.bar(x=categories, y=values, color=categories,
                 color_discrete_map={'Matched Skills': 'green', 'Missing Skills': 'red'},
                 title="Skills Comparison")
    fig.update_layout(height=300)
    return fig
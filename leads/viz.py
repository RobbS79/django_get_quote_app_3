import pandas as pd
import plotly.express as px
from plotly.io import to_html


def viz_compare_volumes(leads_df: pd.DataFrame):
    # Grouping the DataFrame by preferred mean of transportation and calculating the mean amount
    avg_amounts = leads_df.groupby("preferred_mean_of_transportation_id")["amount"].mean().reset_index()

    # Creating the area chart using Plotly
    fig = px.area(
        avg_amounts,
        x="preferred_mean_of_transportation_id",
        y="amount",
        title="Average Amount by Preferred Mean of Transportation",
        labels={"preferred_mean_of_transportation_id": "Preferred Mean of Transportation", "amount": "Average Amount"}
    )

    # Converting the Plotly figure to HTML
    plot_html = to_html(fig, full_html=False)

    # Return the HTML containing the plot
    return plot_html
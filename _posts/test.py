import pandas as pd
import plotly.express as px

# Create a simple dataset
data = {
    'Product': ['A', 'B', 'C', 'D'],
    'Sales': [400, 600, 800, 300]
}

df = pd.DataFrame(data)

# Create a bar chart using Plotly Express
fig = px.bar(df, x='Product', y='Sales', title='Sales Data')

# Save the chart as an HTML file
fig.write_html('sales_chart.html')

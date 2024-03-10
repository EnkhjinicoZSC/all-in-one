import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown("# Simplify 🎉")
st.sidebar.markdown("# Simplify 🎉")


# Parse the data from Simplify
file_path = 'data/simplify.csv'
df_simplify = pd.read_csv(file_path)
df_simplify['Location'] = df_simplify['Location'].str.split(',').str[0]

# Create a bar chart showing the top 20 locations and the number of recently posted jobs
top_locations = df_simplify['Location'].value_counts().head(20)
fig = px.bar(top_locations, x=top_locations.index, y=top_locations.values)
fig.update_layout(title='Top 20 Locations with Recently Posted Jobs', xaxis_title='Location', yaxis_title='Number of Jobs')
st.plotly_chart(fig)


st.write("""
More graphs are coming along.
""")


import streamlit as st
import pandas as pd
import plotly.express as px

 
st.write("""
# My first app
Hello *world!*
""")


# Parse the data
file_path = 'data/job_pulse.csv'
df = pd.read_csv(file_path)
df['Time'] = pd.to_datetime(df['Time'] + ' 2024', format='%b %d %Y')


# JOB POSTINGS OVER TIME
st.title('Job Postings Over Time - Scatter Plot')

# Slider for selecting YoE
selected_yoe = st.slider('Select Years of Experience (YoE)', min_value=0, max_value=2, step=1)
filtered_df = df[df['YoE'] == selected_yoe]
daily_job_counts = filtered_df.groupby(filtered_df['Time'].dt.date).size().reset_index(name='Job Count')

# Scatter plot using Plotly Express
fig = px.scatter(daily_job_counts, x='Time', y='Job Count', title='Job Postings Over Time',
                 labels={'Job Count': 'Number of Jobs Posted', 'Time': 'Date'})
st.plotly_chart(fig)

# Bar plot showing the total number of job postings for each YoE
st.subheader('Total Number of Job Postings for Each Year of Experience Required')
fig_bar = px.bar(df.groupby('YoE').size().reset_index(name='Job Count'),
                 x='YoE', y='Job Count', labels={'Job Count': 'Total Job Postings', 'YoE': 'Years of Experience'})
st.plotly_chart(fig_bar)



import streamlit as st
import pandas as pd
import plotly.express as px


def parse_data(file_path, date_column):
    df = pd.read_csv(file_path)
    df[date_column] = pd.to_datetime(df[date_column] + ' 2024', format='%b %d %Y')
    return df


def plot_job_postings_over_time(df):
    st.subheader('Job Postings Over Time - Scatter Plot')

    selected_yoe = st.slider('Select Years of Experience (YoE)', min_value=0, max_value=2, step=1)
    filtered_df = df[df['YoE'] == selected_yoe]
    monthly_job_counts = filtered_df.resample('M', on='Time').size().reset_index(name='Job Count')

    # Bar plot using Plotly Express
    fig = px.bar(monthly_job_counts, x='Time', y='Job Count', title='Job Postings Over Time',
                 labels={'Job Count': 'Number of Jobs Posted', 'Time': 'Month'})
    st.plotly_chart(fig)


def plot_total_job_postings_by_experience(df):
    st.subheader('Total Number of Job Postings for Each Year of Experience Required')
    fig_bar = px.bar(df.groupby('YoE').size().reset_index(name='Job Count'),
                     x='YoE', y='Job Count', labels={'Job Count': 'Total Job Postings', 'YoE': 'Years of Experience'})
    st.plotly_chart(fig_bar)


def plot_top_locations_with_most_job_postings(df, location_column):
    location_counts = df[location_column].value_counts().reset_index()
    location_counts.columns = ['Location', 'Job Count']

    # Get the top 5 locations
    top_locations = location_counts.head(5)

    # Streamlit App
    st.subheader('Top 5 Locations with Most Job Postings')

    # Bar plot using Plotly Express
    fig = px.bar(top_locations, x='Location', y='Job Count',
                 title='Top 5 Locations with Most Job Postings',
                 labels={'Job Count': 'Number of Job Postings', 'Location': 'Location'})
    st.plotly_chart(fig)


# Main Streamlit app
st.title(""" State of the Market: Insightful Data Driven Approach""")

# Parse data for the first section
job_pulse_file_path = 'data/job_pulse.csv'
job_pulse_df = parse_data(job_pulse_file_path, 'Time')

# Plotting job postings over time
plot_job_postings_over_time(job_pulse_df)
plot_total_job_postings_by_experience(job_pulse_df)

# Parse data for the second section
simplify_file_path = 'data/simplify.csv'
simplify_df = parse_data(simplify_file_path, 'Date Posted')

# Plotting top locations with most job postings
plot_top_locations_with_most_job_postings(simplify_df, 'Location')

# All-In-One

This GitHub repo serves as a codebase for Hackathon project.

# Introduction
This project aims to provide Job Seekers with insightful data visualizations to help them grasp and assess the job market in a data-driven way. 
This is not a place to find job postings. You can use this web app to get a feel for which positions are being hired at what rate, in which location and with what qualifications. 

We started this idea because this is something that we definitely need as current job seekers and we hope others find it useful as well. 

# Codebase
The codebase here does the following:
- Scrapes reliable sources of job postings: jobpulse.fyi, simplify.com
- Provides data visualizations with a degree of interactive features using streamlit

We hope to provide the following features in the future:
- Bigger job postings database
- Personalized job recommendations
- Funnel visualizer for job applications
- etc ...

Frameworks used: Streamlit, Pandas, Plotly


# Setup:

## To initiliaze

```bash
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
```

**To run the app:** `streamlit run Main.py`

And then the server is running up on the local host: `http://localhost:8501/`

To stop the Streamlit server, press ```Ctrl+C``` in the terminal



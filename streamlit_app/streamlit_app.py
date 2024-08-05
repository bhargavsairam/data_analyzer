import streamlit as st
import requests
import time

st.title('Streamlit and Flask Integration Example')

# Retry mechanism
max_retries = 10
retry_delay = 2
flask_url = 'http://localhost:5000/data'

for attempt in range(max_retries):
    try:
        response = requests.get(flask_url)
        if response.status_code == 200:
            data = response.json()
            st.write(data['message'])
            break
    except requests.exceptions.ConnectionError:
        st.write(f"Attempt {attempt+1} of {max_retries} failed. Retrying in {retry_delay} seconds...")
        time.sleep(retry_delay)
else:
    st.write('Error: Could not fetch data from Flask after multiple attempts')

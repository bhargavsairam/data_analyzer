from threading import Thread
import subprocess
import time

def run_flask():
    subprocess.run(['python', 'app.py'])

def run_streamlit():
    subprocess.run(['streamlit', 'run', 'streamlit_app/streamlit_app.py'])

if __name__ == '__main__':
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    # Wait for Flask to start
    time.sleep(5)

    streamlit_thread = Thread(target=run_streamlit)
    streamlit_thread.start()

    flask_thread.join()
    streamlit_thread.join()

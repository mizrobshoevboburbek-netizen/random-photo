# Random Photo Generator

A small web project built with HTML, CSS, JavaScript, and Python (Flask).

## Run it on your computer

1. Install Python 3.
2. Open a terminal in this project folder.
3. (Optional but recommended) create and activate a virtual environment.
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the server:

   ```bash
   python app.py
   ```

6. Open http://127.0.0.1:5000 in your browser.

## How it works

- `templates/index.html` contains the page structure.
- `static/style.css` controls the design.
- `static/script.js` sends a request when the button is clicked and updates the image.
- `app.py` is the Python Flask server. It returns a random photo from `/api/random-photo`.

## Publish it as one public link

This project uses a Python backend, so GitHub Pages alone cannot run the whole app. Deploy the folder to a Python hosting service such as Render, using:

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`

Add `gunicorn` to `requirements.txt` before deploying (`gunicorn>=21,<24`). After deployment, the hosting service gives you a public URL to share.

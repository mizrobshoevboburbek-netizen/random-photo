from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

PHOTOS = [
    {
        "url": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=1200&auto=format&fit=crop",
        "title": "Mountain Adventure",
        "category": "Nature"
    },
    {
        "url": "https://images.unsplash.com/photo-1470770841072-f978cf4d019e?w=1200&auto=format&fit=crop",
        "title": "Peaceful Lake",
        "category": "Nature"
    },
    {
        "url": "https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=1200&auto=format&fit=crop",
        "title": "Ocean Waves",
        "category": "Ocean"
    },
    {
        "url": "https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=1200&auto=format&fit=crop",
        "title": "Beautiful Landscape",
        "category": "Travel"
    },
    {
        "url": "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?w=1200&auto=format&fit=crop",
        "title": "Golden Sunrise",
        "category": "Nature"
    },
    {
        "url": "https://images.unsplash.com/photo-1493246507139-91e8fad9978e?w=1200&auto=format&fit=crop",
        "title": "Forest Escape",
        "category": "Nature"
    },
    {
        "url": "https://images.unsplash.com/photo-1519681393784-d120267933ba?w=1200&auto=format&fit=crop",
        "title": "Starry Mountains",
        "category": "Night"
    },
    {
        "url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1200&auto=format&fit=crop",
        "title": "Mountain Peaks",
        "category": "Travel"
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/random-photo")
def random_photo():
    return jsonify(random.choice(PHOTOS))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

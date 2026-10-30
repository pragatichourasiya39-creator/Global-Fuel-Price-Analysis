
from flask import Flask, render_template
from pathlib import Path

# Get project folder locations
BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent

app = Flask(
    __name__,
    template_folder=str(BASE_DIR),
    static_folder=str(PROJECT_DIR / "static"),
    static_url_path="/assets"
)

# Home page
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/story')
def story():
    return render_template("story.html")


if __name__ == '__main__':
    app.run(debug=True)

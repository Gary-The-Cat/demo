from flask import Flask, render_template

app = Flask(__name__)

FEATURES = [
    {
        "title": "Notes API",
        "description": "Create, list, and sync personal notes across devices with Supabase as the data store."
    },
    {
        "title": "Auth-first",
        "description": "Google sign-in keeps private data private while letting you experiment safely."
    },
    {
        "title": "Modular Deploys",
        "description": "Each subdomain ships independently so you can iterate per project without redeploying everything."
    },
]

ENDPOINTS = [
    {
        "method": "GET",
        "path": "/health",
        "summary": "Quick health check used by Render to confirm the service is up."
    },
    {
        "method": "GET",
        "path": "/api/v1/notes",
        "summary": "List notes for the authenticated user. Coming soon once Supabase is wired up."
    },
    {
        "method": "POST",
        "path": "/api/v1/notes",
        "summary": "Create a new note. Requires auth and JSON payload with title/body."
    },
]


@app.route("/")
def home():
    return render_template("home.html", features=FEATURES, endpoints=ENDPOINTS)


@app.route("/health")
def health():
    return {"status": "ok"}

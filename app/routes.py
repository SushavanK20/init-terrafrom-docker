from flask import Blueprint, jsonify, render_template

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "india-devops-platform"
    })


@main.route("/api/status")
def status():
    return jsonify({
        "application": "India DevOps Platform",
        "environment": "local",
        "version": "1.0.0",
        "status": "running"
    })
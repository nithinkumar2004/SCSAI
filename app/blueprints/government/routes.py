from flask import Blueprint, render_template

government_bp = Blueprint("government", __name__)


@government_bp.route("/")
def dashboard():
    return render_template("government/dashboard.html")


@government_bp.route("/complaints")
def complaints_queue():
    return render_template("government/complaints_queue.html")

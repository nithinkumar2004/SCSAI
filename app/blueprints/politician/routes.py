from flask import Blueprint, render_template

politician_bp = Blueprint("politician", __name__)


@politician_bp.route("/")
def dashboard():
    return render_template("politician/dashboard.html")


@politician_bp.route("/analytics")
def analytics():
    return render_template("politician/analytics.html")

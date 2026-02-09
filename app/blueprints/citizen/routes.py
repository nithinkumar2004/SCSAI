from flask import Blueprint, render_template, request

from app.services.complaint_ai import generate_formal_complaint

citizen_bp = Blueprint("citizen", __name__)


@citizen_bp.route("/")
def dashboard():
    return render_template("citizen/dashboard.html")


@citizen_bp.route("/complaints", methods=["GET", "POST"])
def complaints():
    formal_complaint = None
    if request.method == "POST":
        summary = request.form.get("summary", "").strip()
        details = request.form.get("details", "").strip()
        formal_complaint = generate_formal_complaint(summary=summary, details=details)
    return render_template("citizen/complaints.html", formal_complaint=formal_complaint)


@citizen_bp.route("/emergency")
def emergency():
    return render_template("citizen/emergency.html")

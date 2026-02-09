from flask import Blueprint, current_app, redirect, render_template, session, url_for

core_bp = Blueprint("core", __name__)


@core_bp.route("/")
def index():
    return render_template("core/index.html")


@core_bp.route("/set-language/<lang_code>")
def set_language(lang_code: str):
    supported_languages = current_app.config["LANGUAGES"]
    if lang_code in supported_languages:
        session["preferred_language"] = lang_code
    return redirect(url_for("core.index"))

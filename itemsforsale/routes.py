from flask import render_template
from itemsforsale import app, db
from itemsforsale.models import Category, Item


@app.route("/")
def home():
    return render_template("items.html")
from flask import render_template, request, redirect, url_for
from itemsforsale import app, db
from itemsforsale.models import Category, Item


@app.route("/")
def home():
    items = list(Item.query.order_by(Item.id).all())
    return render_template("items.html", items=items)


@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


@app.route("/add_item", methods=["GET", "POST"])
def add_item():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        item = Item(
            item_name=request.form.get("item_name"),
            item_description=request.form.get("item_description"),
            is_crossposted=bool(True if request.form.get("is_crossposted") else False),
            sale_date=request.form.get("sale_date"),
            category_id=request.form.get("category_id")
        )
        db.session.add(item)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_item.html", categories=categories)


@app.route("/edit_item/<int:item_id>", methods=["GET", "POST"])
def edit_item(item_id):
    item = Item.query.get_or_404(item_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        item.item_name = request.form.get("item_name")
        item.item_description = request.form.get("item_description")
        item.is_crossposted = bool(True if request.form.get("is_crossposted") else False)
        item.sale_date = request.form.get("sale_date")
        item.category_id = request.form.get("category_id")
        db.session.commit()
    return render_template("edit_item.html", item=item, categories=categories)


@app.route("/delete_item/<int:item_id>")
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("home"))
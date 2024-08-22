from itemsforsale import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    items = db.relationship("Item", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Item(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50), unique=True, nullable=False)
    item_description = db.Column(db.Text, nullable=False)
    is_crossposted = db.Column(db.Boolean, default=False, nullable=False)
    sale_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Item: {1} | Crossposted: {2}".format(
            self.id, self.item_name, self.is_crossposted
        )
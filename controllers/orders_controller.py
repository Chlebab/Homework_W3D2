from flask import Blueprint
from flask import render_template
from models.order_list import orders

tasks_blueprint = Blueprint("orders",__name__)

@tasks_blueprint.route("/orders/<index>")
def something(index):
    chosen_order = orders[int(index)]
    return render_template("order.html", title = "My Astounding Pizza Place", order = chosen_order)

@tasks_blueprint.route("/orders")
def index():
    return render_template("index.jinja", title = "My Astounding Pizza Place", orders = orders)

@tasks_blueprint.route("/orders/names")
def names():
    return render_template("names.html", title = "My Astounding Pizza Place", orders = orders)

# "/<name>" 
# /john 
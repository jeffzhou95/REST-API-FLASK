from flask import Flask, jsonify

app = Flask(__name__)

store = [
	{
		"name": "My Wonderful Store",
		"item": [
			{
			"name": "Apple",
			"price": 15.99
			}
		]
	}
]

@app.route("/")
def home():
	return "Hello!"

@app.route("/store", methods=["POST"])
def create_store():
	pass

@app.route("/store/<string:name>")
def get_store(name):
	pass

@app.route("/store")
def get_stores():
	return jsonify({"store": stores})

@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
	pass

@app.route("/store/<string:name>")
def get_items_in_store(name):
	pass

app.run(port = 5000)
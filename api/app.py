from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/process-order", methods=["POST"])
def process_order():
    data = request.json

    # Simulation
    result = {
        "status": "processed",
        "order_number": data.get("order_number"),
        "message": "Order successfully received"
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
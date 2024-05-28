from flask import Flask, request, jsonify

app = Flask(__name__)

# @app.route("/")
# def home()->None:
#     return "API Home"

@app.route("/get-user/<user_id>")
def get_user(user_id)->None:
    user_data = {
        "user_id": user_id,
        "name": "Miyamoto Musashi",
        "email": "miyamoto.musashi@japan.jp"
                }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user()->None:
    data = request.get_json()
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=7090,debug=True)
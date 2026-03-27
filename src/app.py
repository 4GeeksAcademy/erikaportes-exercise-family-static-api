import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
family = FamilyStructure("Jackson")

initial_members = [
    {"first_name": "John", "age": 33, "lucky_numbers": [7, 13, 22]},
    {"first_name": "Jane", "age": 35, "lucky_numbers": [10, 14, 3]},
    {"first_name": "Jimmy", "age": 5, "lucky_numbers": [1]}
]

for m in initial_members:
    family.add_member(m)

# GET /members
@app.route('/members', methods=['GET'])
def get_all_members():
    try:
        return jsonify(family.get_all_members()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET /members/<int:member_id>
@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    try:
        member = family.get_member(member_id)

        if member is None:
            return jsonify({"error": "Member not found"}), 400

        return jsonify(member), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# POST /members
@app.route('/members', methods=['POST'])
def add_member():
    try:
        data = request.json

        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        new_member = family.add_member(data)

        return jsonify(new_member), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# DELETE /members/<int:member_id>
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    try:
        success = family.delete_member(member_id)

        if not success:
            return jsonify({"error": "Member not found"}), 400

        return jsonify({"done": True}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)










# # Handle/serialize errors like a JSON object
# @app.errorhandler(APIException)
# def handle_invalid_usage(error):
#     return jsonify(error.to_dict()), error.status_code

# # Generate sitemap with all your endpoints
# @app.route('/')
# def sitemap():
#     return generate_sitemap(app)

# @app.route('/members', methods=['GET'])
# def handle_hello():
#     # This is how you can use the Family datastructure by calling its methods
#     members = jackson_family.get_all_members()
#     response_body = {"hello": "world",
#                      "family": members}
#     return jsonify(response_body), 200



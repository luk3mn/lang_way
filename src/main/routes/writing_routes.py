from flask import Blueprint, jsonify, request
from src.service.gemini import Gemini
from dotenv import load_dotenv
import os

writing_route_bp = Blueprint("writing_route", __name__)

@writing_route_bp.route("/check", methods=["POST"])
def check_level():

    load_dotenv()
    gemini = Gemini(GOOGLE_API_KEI=os.getenv("GOOGLE_API_KEY"))

    data = request.json
    if "prompt" in data and "language" in data:
        prompt = data['prompt']
        language = data['language']
        response = gemini.generate(input=prompt, language=language)

        return jsonify({"message": response}), 201

    return jsonify({"message":"Something went worng!"}), 400

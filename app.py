from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

from ice_breaker import ice_break_with


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form.get("name", "").strip()

    # Validate input
    if not name:
        return (
            jsonify({"success": False, "error": "Please enter a name to continue."}),
            400,
        )

    try:
        summary_and_facts, interests, ice_breakers, profile_pic_url = ice_break_with(
            name=name
        )
        return jsonify(
            {
                "success": True,
                "data": {
                    "summary_and_facts": summary_and_facts.to_dict(),
                    "interests": interests.to_dict(),
                    "ice_breakers": ice_breakers.to_dict(),
                    "picture_url": profile_pic_url,
                },
            }
        )
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        error_msg = f"An unexpected error occurred: {str(e)}"
        print(
            f"Error processing request for '{name}': {error_msg}"
        )  # Log for debugging
        return jsonify({"success": False, "error": error_msg}), 500


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)

from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Configure your Gemini API key
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set.")

genai.configure(api_key=GOOGLE_API_KEY)

# Select the Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')


@app.route('/')
def index():
    """Serve the HTML upload form"""
    return render_template("upload.html")


@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Uploads a file and processes it with Gemini.
    """
    try:
        file = request.files.get("file")
        prompt = request.form.get("prompt") or "Analyze the uploaded file and summarize it."

        if not file:
            return jsonify({"error": "No file uploaded"}), 400

        # Get MIME type
        mime_type = file.mimetype

        # Read file content
        file_content = file.read()

        # Build request parts for Gemini
        file_part = {
            "mime_type": mime_type,
            "data": file_content
        }

        response = model.generate_content(
            [file_part, {"text": prompt}]
        )

        return jsonify({
            "filename": file.filename,
            "content_type": mime_type,
            "gemini_response": getattr(response, "text", "No textual response generated.")
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint"""
    return jsonify({"status": "ok"})


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))

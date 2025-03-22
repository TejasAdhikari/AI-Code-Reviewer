import asyncio
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from google import genai
from db import save_review
from codeReviewer import ai_analyze_code
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Initialize the Flask app
app = Flask(__name__)
# Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "*"}})  
# Initialize the Flask-Restful API
api = Api(app)


# Define the analyze endpoint
@app.route('/analyze', methods=['POST'])
def analyze_code():
    try:
        # Get the code snippet from the request
        data = request.json
        code_snippet = data.get('code', '')
        
        # Call the ai_analyze_code function to analyze the code
        feedback = asyncio.run(ai_analyze_code(code_snippet))
        
        # Store the review in the database
        # Store in database and add the message to the feedback
        # Store the review in the database
        logger.info("Attempting to save review to database.")  # Debug print
        addedToDB = save_review(code_snippet, feedback)
        if addedToDB:
            feedback += "\n\nReview was successfully added to the database."
        else:
            feedback += "\n\nAn error occured while adding the review to the database."

        # Return the feedback
        return jsonify({"feedback": feedback})
    
    except Exception as e:
        print(f"Error: {str(e)}")
        # Return an error response
        return jsonify({"feedback": f"An error occurred: {str(e)}"}), 500

# Define the home route
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) # run our Flask app in debug mode, do not use in production

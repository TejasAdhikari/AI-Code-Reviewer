from urllib import response
from google import genai
from flask import jsonify
from config import GEMINI_API_KEY


# Initialize the gemini genai client
client = genai.Client(api_key=GEMINI_API_KEY)

# Make the gemini API call
async def ai_analyze_code(code_snippet):
    try:
        # Create a prompt that asks for code analysis
        prompt = f"""
        Please analyze the following code and provide feedback on:
        - Code quality
        - Potential bugs
        - Performance issues
        - Best practices
        - Suggestions for improvement

        CODE:
        ```
        {code_snippet}
        ```
        """
        
        # Make the API call to generate content from gemini-2.0-flash model.
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )
        
        # Extract text from the response
        feedback = response.candidates[0].content.parts[0].text
            
        return feedback
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"feedback": f"An error occurred: {str(e)}"}), 500

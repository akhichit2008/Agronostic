from flask import Flask, jsonify, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import re
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure key
CORS(app)
# Define the form
class QueryForm(FlaskForm):
    query = StringField('Query', validators=[DataRequired()])
    submit = SubmitField('Ask')

@app.route('/')
def index():
    form = QueryForm()
    return render_template('assist.html', form=form)

@app.route('/ask', methods=['POST'])
def ask_query():
    form = QueryForm()
    
    # Print incoming data for debugging
    print("Incoming request data:", request.form)
    query = request.form.get('query')

    if query:
        # Process the query with the Gemini API or any other logic
        answer = process_with_gemini_api(query)
        return jsonify({'answer': answer})  # Return a JSON response with the answer
    
    return jsonify({'answer': 'Invalid input.'}), 400  # Return a 400 error if input is invalid

def process_with_gemini_api(query):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(f"You are a friendly helper for a farmer. Your name is AgroAssist. Answer this query asked by the farmer: {query}")
        assist = response.text
        assist = re.sub(r'\*', '', assist)
        assist = re.sub(r'([^:\n]*:[^:\n]*\n)\s*:(.+)', r'\1\2', assist)
        return assist
    except Exception as e:
        return str(e)  # Return error message

if __name__ == '__main__':
    app.run(debug=True,port=3500)

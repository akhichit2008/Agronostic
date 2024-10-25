from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('forestfiremodel.pkl')

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    # Get the input features from the form
    int_features = [float(x) for x in request.form.values()]
    final = [np.array(int_features)]
    prediction = model.predict_proba(final)
    
    # Get the probability of fire occurrence
    output = '{0:.{1}f}'.format(prediction[0][1], 2)
    
    # Define precautionary methods and causes
    precautions = [
        "Clear dry leaves and debris around the forest.",
        "Ensure proper firebreaks between forest areas.",
        "Regularly monitor weather conditions for high temperatures or low humidity.",
        "Ban any open fires or controlled burns during fire-prone seasons."
    ]
    
    fire_causes = [
        "Lightning strikes in dry weather.",
        "Human activities like campfires or discarded cigarettes.",
        "Sparks from machinery or equipment near the forest.",
        "Intentional or accidental arson."
    ]
    
    if output > str(0.5):
        # Forest is in danger, display precautions and causes
        return render_template(
            'index.html',
            pred=f"Your Forest is in Danger. Probability of fire occurring is {output}.",
            precautions="Precautionary Methods: " + ', '.join(precautions),
            fire_causes="Possible Causes of Fire: " + ', '.join(fire_causes)
        )
    else:
        # Forest is safe
        return render_template(
            'index.html',
            pred=f"Your Forest is safe. Probability of fire occurring is {output}.",
            prevention="To keep the forest safe, consider these general safety tips: " + ', '.join(precautions)
        )

if __name__ == '__main__':
    app.run(debug=True, port=5678)
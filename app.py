from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load trained model and vectorizer
model = pickle.load(open('hate_speech_model.pkl', 'rb'))
vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        vectorized = vectorizer.transform([text])
        prediction = model.predict(vectorized)

        result = "Hate Speech" if prediction[0] == 1 else "Not Hate Speech"
        return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        text = request.form['text_input']
        # Here you would add your hate speech detection logic
        # For example, call your model to predict:
        # prediction = model.predict([text])
        # For demo, let's just echo the input:
        result = f"Text received: {text}"  
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

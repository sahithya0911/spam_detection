from flask import Flask, render_template, request
from model import predict_spam

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    result = predict_spam(message)
    return render_template('index.html', prediction=result, message=message)

if __name__ == '__main__':
    app.run(debug=True)
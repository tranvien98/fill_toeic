from flask import Flask, render_template, request
from predict import FillBert
import requests
import re
app = Flask(__name__)

fill_bert = FillBert()
@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    questions = request.form['question'].replace('\r', '').split('\n')
    row = {}
    row['origin'] = request.form['question'].replace('\n', '<br>')
    row['question'] = questions[0].strip()
    print(questions)
    for i in range(1,5):
        print(questions[i])
        row[str(i)] = re.sub('</?.*?>','',questions[i].replace('(','<').replace(')', '>')).strip()
    row['answer'] = fill_bert.predict(row)
    return render_template('result.html', row=row)
@app.route('/example')
def example():
    return render_template('example.html')
if __name__ == "__main__":
     app.run(host='127.0.0.1', port=5050, debug=True, threaded=True)
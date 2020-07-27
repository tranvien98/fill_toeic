from flask import Flask, render_template, request
from predict import FillBert
from fitbert import FitBert
import requests
import re
app = Flask(__name__)

fb = FitBert()
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
        # print(questions[i])
        row[str(i)] = re.sub('</?.*?>','',questions[i].replace('(','<').replace(')', '>')).strip()
    masked_string = row['question'].replace('___', '***mask***')
    options = [row['1'], row['2'], row['3'], row['4']]
    row['answer'] = fb.rank_with_prob(masked_string, options)[0][0]
    return render_template('result.html', row=row)
@app.route('/example')
def example():
    return render_template('example.html')
if __name__ == "__main__":
     app.run(host='0.0.0.0', port=4040, debug=True, threaded=True)
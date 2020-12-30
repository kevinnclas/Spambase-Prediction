# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:12:32 2020

@author: kevin
"""

from flask import Flask, render_template, request
import re 
from collections import Counter
from joblib import load
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title = "Spambase prediction")

def text_to_ind(text):
    all_variables = ['make', 'address', 'all', '3d', 'our', 'over', 'remove', 'internet', 'order', 'mail', 'receive', 'will', 'people', 'report', 'addresses', 'free', 'business', 'email', 'you', 'credit', 'your', 'font', '000', 'money', 'hp', 'hpl', 'george', '650', 'lab', 'labs', 'telnet', '857', 'data', '415', '85', 'technology', '1999', 'parts', 'pm', 'direct', 'cs', 'meeting', 'original', 'project', 're', 'edu', 'table', 'conference', ';', '(', '[', '!', '$', '#', 'capital_run_length_average', 'capital_run_length_longest', 'capital_run_length_total']
    dic = {}
    text_split = re.split(r'\W+', text)
    text_split_count = Counter(text_split)
    for i in range(48):
        if all_variables[i] in text_split_count.keys() : dic[all_variables[i]] = 100*text_split_count[all_variables[i]]/len(text_split)
        else : dic[all_variables[i]] = float(0)

    for i in range(48,54):
        dic[all_variables[i]] = 100*text.count(all_variables[i])/(len(text)- text.count(' '))

    all_uppercase_sequence = re.findall(r"[A-Z]+", text)

    if len(all_uppercase_sequence) == 0:
        dic['capital_run_length_average'] = 0
        dic['capital_run_length_longest'] = 0
        dic['capital_run_length_total'] = 0

    else :
        sum_uppercase = 0

        for sequence in all_uppercase_sequence:
            sum_uppercase += len(sequence)

        dic['capital_run_length_average'] = sum_uppercase/len(all_uppercase_sequence)
        dic['capital_run_length_longest'] = len(max(all_uppercase_sequence, key=len))
        dic['capital_run_length_total'] = sum_uppercase

    return np.array(list(dic.values())).reshape(1,-1)


@app.route('/prediction', methods = ['POST'])
def page_pred():
    mailtotest = request.form['email']
    model = load('model_saved.joblib')
    finalpredict = str(model.predict(text_to_ind(mailtotest))[0])
    return render_template('results.html', title = "Prediction", data = finalpredict)

@app.route('/TrueSpam')
def true_spam():
    return render_template('true_spam.html', title = "True Spam")

@app.route('/FalseSpam')
def false_spam():
    return render_template('false_spam.html', title = "False Spam")

@app.route('/TrueSafeMail')
def true_mail():
    return render_template('true_mail.html', title = "True Safe Mail")

@app.route('/FalseSafeMail')
def false_mail():
    return render_template('false_mail.html', title = "False Safe Mail")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
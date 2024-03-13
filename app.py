import re
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results',methods=['post'])
def r():
    regex = request.form['pattern']
    string = request.form['text']
    matches = re.findall(regex,string)
    return render_template('index.html',pattern=regex,text=string,matches=matches)

@app.route('/email')
def e():
    return render_template('mail.html',valid_mail=None)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    pattern =r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[.][\w]{2,3}$"
    text = request.form['mail']
    mails= re.findall(pattern, text)
    if mails!=[]:
        return render_template('mail.html', valid_mail=True,text=text)
    else:
        return render_template('mail.html', valid_mail=False,text=text)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
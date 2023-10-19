from mycode import func
from flask import Flask, request, render_template
import numpy as np
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    result = None
    if request.method == 'POST':
        al = float(request.form.get('al'))
        la = float(request.form.get('la'))
        pr = float(request.form.get('pr'))
        #pe = float(request.form.get('pe'))
        result = func(al,la,pr)
    return render_template('index.html', result=result)










@app.route('/hello', methods=["GET"])
def HelloWorld():
    return "Hello World"
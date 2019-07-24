from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/sentenceResult',methods=['GET','POST'])
def sentenceResult():
    userData = dict(request.form)
    sentenceRoute = userData["sentenceIndex"][0]
    oddEvenResult = "odd"
    if model.oddEven(sentenceRoute) == True:
        oddEvenResult = "even"
    return render_template('sentenceResult.html',oddEvenResult=oddEvenResult, sentence = sentenceRoute)
    
@app.route('/numResult',methods=['GET','POST'])
def numResult():
    userData = dict(request.form)
    num1=int(userData["num1"][0])
    num2=int(userData["num2"][0])
    operation=userData["operation"][0].lower()
    result = model.mathOperation(num1,num2,operation)
    return render_template('numResult.html',result=result)
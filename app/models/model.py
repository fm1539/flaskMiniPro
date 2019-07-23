def oddEven(sentenceModel):
    return(len(sentenceModel)%2 == 0)
    
def mathOperation(num1,num2,operation):
    if operation == "plus":
        return num1+num2
    elif operation == "minus":
        return num1-num2
    elif operation == "multiply":
        return num1*num2
    elif operation == "divide":
        return num1/num2
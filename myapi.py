#imports-----------------------
from fastapi import FastAPI
import inflect
from googletrans import *

#Translate Instance------------
translator = Translator()

#Instances---------------------
app = FastAPI()
x = inflect.engine()

#Main -------------------------
@app.get("/")
def index():
    return 'Welcome to my A.P.I'

@app.get('/get-result/{lang}/{value}')
def get_result(value: str, lang: str):
    input = value.split(".")

    # [ Conditiion for values like: '50.09' ]
    if len(input)==2 and int(input[0]) != 0:
        number, decimal = int(input[0]),int(input[1])
        op1,op2 = x.number_to_words(number)+' SAR,', x.number_to_words(decimal)+' Halala'
        op = op1+op2
        tr = translator.translate(op, dest=lang)

        return tr.text

    # [ Conditiion for values like: '.956' ]
    if int(input[0])==0 and len(input)==2:
        number= int(input[1])
        op= x.number_to_words(number)+' Halala'
        tr = translator.translate(op, dest=lang)

        return tr.text

    # [ Conditiion for values like: '6700' ]
    if int(input[0])!=0 and len(input)==1:
        number= int(input[0])
        op= x.number_to_words(number)+' SAR'
        tr = translator.translate(op, dest=lang)

        return tr.text

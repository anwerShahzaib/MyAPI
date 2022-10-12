#imports
from fastapi import FastAPI
import inflect
from googletrans import *

# Translate Instance
translator = Translator()

# FastAPI Instance
app = FastAPI()

x = inflect.engine()

inventory = {
    1:{
        "name":"apple",
        "cat" : "fruit",
        "price" : 6.55,
        "U.M": "Kgs"
    },
    2:{
        "name":"eggs",
        "cat" : "dairy",
        "price" : 9.35,
        "U.M": "dozen"
    }
}

@app.get("/")
def index():
    return "Welcome to my A.P.I"

@app.get('/get-result/{value}')
def get_result(value: str):
    input = value.split(".")

    # [ Conditiion for values like: '50.09' ]
    if len(input)==2 and int(input[0]) != 0:
        number, decimal = int(input[0]),int(input[1])
        op1,op2 = x.number_to_words(number)+' SAR,', x.number_to_words(decimal)+' Halala'
        op = op1+op2
        tr = translator.translate(op, dest='ar')
        #print(op)

        return op,tr.text

    # [ Conditiion for values like: '.956' ]
    if int(input[0])==0 and len(input)==2:
        number= int(input[1])
        op= x.number_to_words(number)+' Halala'
        #print(op)
        tr = translator.translate(op, dest='ar')
        return op,tr.text

    # [ Conditiion for values like: '6700' ]
    if int(input[0])!=0 and len(input)==1:
        number= int(input[0])
        op= x.number_to_words(number)+' SAR'
        #print(op)
        tr = translator.translate(op, dest='ar')
        return op,tr.text

    # return tr.text
    # print(value)
    # print(tr.text)



@app.get('/get-item/{item_id}')
def get_item(item_id: int):
    return inventory[item_id]

@app.get('/get-by-name/')
def get_by_name(name: str):
    for item in inventory:
        if inventory[item]["name"]== name:
            return inventory[item]
    return {"Data":"Not Found"}
#http://127.0.0.1:8000/get-by-name/?name=eggs
#imports-----------------------
from fastapi import FastAPI
import inflect
from googletrans import *
from fastapi.middleware.cors import CORSMiddleware
#Translate Instance------------
translator = Translator()

#Instances---------------------
app = FastAPI()

#CORS Handling
# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]

# The url you trying to get request from, if it _ _ _ _ _ _ _ _
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://sgapco.sowaanerp.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

x = inflect.engine()

#Main -------------------------
@app.get("/")
def index():
    return 'Welcome to my A.P.I --UPDATED'

@app.get("/test")
def test():
    return '<-----Endpoints Working Fine----->'

@app.get('/get-result/{lang}/{value}')
def get_result(value: str, lang: str):

    #input = value.split(".")
    #number, decimal = int(input[0]),int(input[1])

    # [ Conditiion for values like: '5000' ]
    if value.isdecimal()==True:
        number= int(value)

        op1= x.number_to_words(number)

        if lang =='ar':
            ar_op = translator.translate(op1, dest='ar').text+" "+translator.translate('SAR', dest='ar').text
            return ar_op
        else:
            en_op = op1+' SAR'
            return en_op
    else:

        input = value.split(".")
        number, decimal = int(input[0]),int(input[1])
    
        # [ Conditiion for values like: '50.9' ]
        if (len(input[1])==1):
            #print("This One working")
            decimal = str(decimal)+'0'
            decimal = int(decimal)
            op1,op2 = x.number_to_words(number),x.number_to_words(decimal)

            if lang =='ar':
                ar_op = translator.translate(op1, dest='ar').text+" "+translator.translate('SAR', dest='ar').text+" "+translator.translate(op2, dest='ar').text+" هللة"
                return ar_op
            else:
                en_op = op1+' SAR and ' +op2+' halalah'#translator.translate(op1, dest='ar').text+" "+translator.translate('SAR', dest='ar').text+" "+translator.translate(op2, dest='ar').text+" هللة"
                return en_op

    
        elif input[1][0]=='0':
            op1,op2 = x.number_to_words(number),x.number_to_words(decimal)

            if lang =='ar':
                ar_op = translator.translate(op1, dest='ar').text+" "+translator.translate('SAR', dest='ar').text+" "+translator.translate(op2, dest='ar').text+" هللة"
                return ar_op
            else:
                en_op = op1+' SAR and ' +op2+' halalah'#translator.translate(op1, dest='ar').text+" "+translator.translate('SAR', dest='ar').text+" "+translator.translate(op2, dest='ar').text+" هللة"
                return en_op
        
        else:
            op1,op2 = x.number_to_words(number),x.number_to_words(decimal)

            if lang =='ar':
                ar_op = translator.translate(op1, dest='ar').text+" "+translator.translate('SAR', dest='ar').text+" "+translator.translate(op2, dest='ar').text+" هللة"
                return ar_op
            else:
                en_op = op1+' SAR and ' +op2+' halalah'#translator.translate(op1, dest='ar').text+" "+translator.translate('SAR', dest='ar').text+" "+translator.translate(op2, dest='ar').text+" هللة"
                return en_op


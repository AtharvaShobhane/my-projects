from flask import Flask,request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
#mongoDB code
import pymongo
client2 = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client2['DBMSandITL']
information= mydb.orders



acc_sid = 'AC91f80b07a3deef5ae6ce9e5b3cf194a9'
auth_token = '90601e4e6120d519dd9572dcad6be49a'
app=Flask(__name__)
client = Client(acc_sid,auth_token)


@app.route('/mybot', methods = ['POST'])

def mybot():
    incoming_msg = request.values.get('Body','').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if  incoming_msg == 'hi':
        client.messages.create(
        to="whatsapp:+919284936420",
        from_="whatsapp:+14155238886",   
        body="Hi , Place your Ice-Cream Order here - \n(Format: MyOrder: FirstName LastName Quantity-Flavour City PhoneNumber)\n|| We have Strawberry , Vanilla , ButterScotch , Mango "
        )
        responded = True

    if 'who are you' in incoming_msg:
        client.messages.create(
        to="whatsapp:+919284936420",
        from_="whatsapp:+14155238886",   
        body="I am a WhatsApp Ordering ChatBot Developed By Group no. 7 for DBMS and ITL Project SY")
        responded=True
    
    if  incoming_msg.split(" ")[0] == 'myorder:':
        dbList = incoming_msg.split(" ")
        print(dbList)
        
        firstName = incoming_msg.split(" ")[1]
        lastName = incoming_msg.split(" ")[2]
        order = incoming_msg.split(" ")[3]
        city = incoming_msg.split(" ")[4]
        phoneNum = incoming_msg.split(" ")[5]
        if len(phoneNum) == 10 :
            records={'firstName':firstName,'lastName':lastName,'order':order,'city':city,'phoneNum':phoneNum}
            information.insert_one(records)
            client.messages.create(
            to="whatsapp:+919284936420",
            from_="whatsapp:+14155238886",   
            body="YAY !! Order Placed. Your Ice-Cream will be delivered soon.")
        else:
            client.messages.create(
            to="whatsapp:+919284936420",
            from_="whatsapp:+14155238886",   
            body="Enter Valid Phone Number. And order Again!")

        

    return str(resp)
    
if __name__ == "__main__":
    app.run()





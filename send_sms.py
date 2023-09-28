from twilio.rest import Client
acc_sid = 'AC91f80b07a3deef5ae6ce9e5b3cf194a9'
auth_token = '90601e4e6120d519dd9572dcad6be49a'

client = Client(acc_sid,auth_token)

client.messages.create(
    to="whatsapp:+919284936420",
    from_="whatsapp:+14155238886",   
    body="Hi Gandu Mein Atharva ka Bot"
)


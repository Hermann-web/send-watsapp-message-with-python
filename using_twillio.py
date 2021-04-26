import os
from twilio.rest import Client

#creer un 'twilio API rest client'
client = Client()

#envoyeur et destinataire
numero_envoi = 'whatsapp:+14155238886'
numero_reception = 'whatsapp:+22967531395'

#le message
client.message.create(body='le message', from_ = numero_envoi, to= numero_reception)

'''
Il faut des autorizations de compte twilio
	- avoir un compte twilio
	- mettre les credentials(TWILIO_ACCOUNT_SID et TWILIO_ACCOUNT_TOKEN) dans les variables d'envoronnement
'''

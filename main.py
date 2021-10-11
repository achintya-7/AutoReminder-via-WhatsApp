from twilio.rest import Client as Client2
import os

from appwrite.client import Client
from appwrite.services.database import Database



# account_sid = os.environ['ACCOUNT_SID']
# auth_token = os.environ["AUTH_TOKEN"]

account_sid = 'ACed6990b7175b248dc25f724c76ca40cf' 
auth_token = '3b5a2ba75652cb6ba0eb1b1389e5bb6b' 
client = Client2(account_sid, auth_token) 

client_aw = Client()
client_aw.set_endpoint("http://192.168.1.9/v1") 
client_aw.set_project("615d8b0e5f3f3") # this is available by default.
client_aw.set_key("98819b363864e759f998ad32d5c533c0790516b44bc65572511c7b57e6f6b6b7b0ed6387c323aa0d03b01a8d148f57712a72862471821d58f5da570d72139844ba8ef1792b6990d79f5185e989b2819ea85f3e8f0a2b81f181de3797c417d244447d0e6996624f31d3da13f0685272d6ca84a72515536a152b63cf391958f429") 

database = Database(client_aw)

result = database.list_documents('61642c7a715bf', limit=100)
collection_list = result['documents']

numbers = []
names = []
for i in range(result["sum"]):
    numbers.append(collection_list[i]["db_num"])
    names.append(collection_list[i]["db_name"])

text = "Join the class at 8:15 using the link provided <ANY LINK>" 

try: 
    for x in range(result["sum"]):
        message = client.messages.create( 
                                    from_='whatsapp:+14155238886',  
                                    body="Reminder!" + names[x] + text,      
                                    to='whatsapp:+91' + str(numbers[x]) 
                                ) 
except Exception as e:
    print(e)

print("message sent!")
# A python wrapper for lasagna.email

``pip install lasagnamail`` 

```py
from lasagnamail import LasagnaMail

client = LasagnaMail()

address = client.createAddress()
print(address)

inbox = client.getInbox()
print(inbox)

email = client.waitForEmail()
print(email)

```
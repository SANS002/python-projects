import pywhatkit

import requests
import json
from random import choice

number = input("Enter your Whatsapp number With country code (eg ,+91):")

url = 'https://type.fit/api/quotes' 
quotes = json.loads(requests.get(url).text)#request.get()used for get the quotes and .text was converted into text form

quote = choice(quotes)

quote_text = quote.get('text')
author = quote.get('author')

mobilenumber = f"{number}"
message = f"{quote_text} - {author}"
 
pywhatkit.sendwhatmsg(mobilenumber,message,17,40)

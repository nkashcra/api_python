########## Example request #############
# POST /learn-http HTTP/1.1
# Host: www.codecademy.com
# Content-Type: text/html; charset=UTF-8
# Name=Eric&Age=26

import requests

body = {'Name': 'Eric', 'Age': '26'}

# Make the POST request here, passing body as the data:
response = requests.post("http://codecademy.com/learn-http/", data=body)  


########################################

# Get Status Code
import requests

response = requests.get('http://placekitten.com/')

# Add your code below!
print response.status_code


########################################


# print the header information from the response
print response.headers



########################################
# Basic Auth:

from requests.auth import HTTPBasicAuth
requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
<Response [200]>
#In fact, HTTP Basic Auth is so common that Requests provides a handy shorthand for using it:

requests.get('https://api.github.com/user', auth=('user', 'pass'))
<Response [200]>
#Providing the credentials in a tuple like this is exactly the same as the HTTPBasicAuth example above.


########################################


#Parse XML from a local file
from xml.dom import minidom

f = open('pets.txt', 'r')
pets = minidom.parseString(f.read())
f.close()

names = pets.getElementsByTagName('name')
for name in names:
	print name.firstChild.nodeValue


###########################################


#Parse JSON from local file
import json
from pprint import pprint

f = open('pets.txt', 'r')
pets = json.loads(f.read())
f.close()

pprint(pets)


########################################

#Read page with a slice

rom urllib2 import urlopen

# Add your code here!
website = urlopen('http://placekitten.com/') 
kittens = website.read()

print kittens[559:1000]	


########################################

#Poll NPR by story ID# and print story titles

from urllib2 import urlopen
from json import load

url = "http://api.npr.org/query?apiKey="

key = "API_KEY"
url += key
url += "&numResults=3"
url += "&format=json"
url += "&id=" 
npr_id = raw_input("Which NPR ID do you want to query?")
url += npr_id

print url

#Open API call URL and load JSON response
#Iterate over returned stories to print each story title
response = urlopen(url)
json_obj = load(response)

for story in json_obj['list']['story']:
    print story['title']['$text']


########################################
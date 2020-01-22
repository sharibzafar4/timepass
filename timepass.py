'''def sentence_maker(phrase):
    interrogatives = ("how","who","what","where","why", "when")
    phrase_caps = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(phrase_caps)
    else:
        return "{}.".format(phrase_caps)

final_sentence = []

while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        new_sentence = sentence_maker(user_input)
        final_sentence.append(new_sentence)

print(" ".join(final_sentence))'''
import requests
import json

API_KEY = 'dnhoWvJ8wvjASezcdwSs'
dic=[]
dic1=[]
header_string = {
       'Accept': 'application/vnd.pagerduty+json;version=2',
       'Authorization': 'Token token={token}'.format(token=API_KEY)
         }


def get_acked_incidents():
    url='https://api.pagerduty.com/incidents/306282'
    r=requests.get(url, headers=header_string)
    j = json.loads(r.text)
    print(type(j['incident']))
    
    for key, value in j['incident'].items():
        print (key,":", value)
    
get_acked_incidents()
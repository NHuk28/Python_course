import json
from difflib import get_close_matches

user_input = input("Enter path to dictionary database:")
try:
    data = json.load(open(user_input))
except FileNotFoundError:
    print ("Wrong path to dictionary database")

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input( "Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'N':
            return "The word doesn't exist. Please check it again."
        else:
            return "We didn't undestend you..."  
    else:
        return "The word doesn't exist. Please check it again."

word = input("Write your word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
import requests
from bs4 import BeautifulSoup
import spacy

URL = [
"https://www.google.com/finance/quote/TSLA:NASDAQ?hl=en", 
]

page = requests.get(URL[0])
soup = BeautifulSoup(page.text, "html.parser")
nlp = nlp = spacy.load("en_core_web_sm")

for i in soup.stripped_strings:
    text = (repr(i))
doc = nlp(text)
for token in doc:
    print(token.text, token.pos_, token.dep_)


"""


nlp = spacy.load("en_core_web_sm")
user_input = input("Enter a sentence: ")
doc = nlp(user_input)
for token in doc:
    print(token.text, token.pos_, token.dep_)

"""
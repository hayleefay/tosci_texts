from twilio.rest import Client
import requests
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
load_dotenv()
import os
TOKEN = os.getenv('TOKEN')
SID = os.getenv('SID')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')
from people_data import people

# prep the Twilio text
account_sid = SID 
auth_token = TOKEN 
client = Client(account_sid, auth_token) 


def get_flavors():
    # pull the HTML
    r = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vT69N7qb2TFMyzkuJOYhZb2YrQPGoyiGXwj2OFlTAdJIglX2RWWUbCIzvpp8MZxoxUer0wQHuHet_4k/pubhtml?gid=799563681&amp;single=true&amp;widget=false&amp;headers=false&amp;range=A1:B40&amp;chrome=false')
    
    if r.status_code == 200:
        soup = bs(r.text, 'html.parser')
        # find the flavors
        flavors_objects = soup.find_all('td', {"class": "s8"})
        flavors = [f.text for f in flavors_objects]
        return flavors

    else:
        # text Haylee
        message = client.messages.create( 
                        from_=TWILIO_NUMBER,        
                        to=people['Haylee']['phone_number'],
                        body=f'Op. Broken. Code: {r.status_code}' 
                    )
        return None


def spread_the_cheer(person, your_flavors):
    if len(your_flavors) == 2:
        flavors_str = "{} and {}".format(", ".join(flavors[:-1]),  flavors[-1])
        text_body = f'🍦 {flavors_str} are at Tosci\'s today!'
    elif len(your_flavors) > 2:
        flavors_str = "{}, and {}".format(", ".join(flavors[:-1]),  flavors[-1])
        text_body = f'🍦 {flavors_str} are at Tosci\'s today!'
    else:
        flavors_str = your_flavors[0]
        text_body = f'🍦 {flavors_str} is at Tosci\'s today!'
    message = client.messages.create( 
                from_=TWILIO_NUMBER,        
                to=people[person]['phone_number'],
                body= text_body
            )


def match_and_text(flavors):
    for person in people:
        your_flavors = []
        for flavor in flavors:
            if flavor in people[person]['faves']:
                your_flavors.append(flavor)
        
        if len(your_flavors) > 0:
            print(person, your_flavors)
            spread_the_cheer(person, your_flavors)


if __name__ == "__main__":
    flavors = get_flavors()
    if flavors is not None:
        match_and_text(flavors)
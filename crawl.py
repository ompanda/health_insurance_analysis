#import the library used to query a website
import urllib2
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
import  pandas as pd
#Create a JSON file

def get_all_polices():
    #url= "https://www.bankbazaar.com/insurance/health-insurance.html"#"https://www.policybazaar.com/health-insurance/"
    read_text()



def read_text():
    #page = urllib2.urlopen(url)
    with open("plans.html", 'r') as f:
        page = f.read()

    #page= pd.read_html()

    # Parse the html in the 'page' variable, and store it in Beautiful Soup format
    soup = BeautifulSoup(page,"lxml")
    #print(soup.prettify())
    main_div_content = soup.find("div", class_="item")

    print(main_div_content.prettify())





















get_all_polices()
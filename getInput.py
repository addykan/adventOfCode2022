'''
As requested by Raaid, webscrapes the input off the advent of code website
'''
import requests, datetime
from dotenv import dotenv_values



def getDefaultDay():
    return int(datetime.datetime.now().strftime('%d'))


def getData(day=getDefaultDay()):
    url = f'https://adventofcode.com/2022/day/{day}/input'
    '''
    To fill in the headersDict, open up the advent website and right click, 
    click "Inspect", go to the Network tab, and reload the page. 
    Then go to the Headers section for the 'input' request and find the 
    cookie header under Request Headers. Copy everything into the below dict
    as a single long string. 

    Not sure if we need to do this repeatedly or if it works for 
    '''
    headersDict = dotenv_values('.env')
    response = requests.get(url, headers=headersDict)
    return response.text

#! python3
# searchNet.py - Opens several search results on a topic currently Amazon and pypi
#Amazon broken investigate anti bot measures maybe?

import webbrowser, sys, requests, bs4

def pypi(term):
    print('Searching...')
    res = requests.get('https://pypi.org/search/?q=' + ' '.join(term))
    res.raise_for_status()

    #retrieve top search result  links
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #opens a browser for each result
    linkList = soup.find_all('a', attrs={'class' : 'package-snippet'})
    numToOpen = min(5, len(linkList))
    for i in range(numToOpen):
        urlOpening = 'https://pypi.org' + linkList[i].get('href')
        print('Opening', urlOpening)
        webbrowser.open(urlOpening)

def amazon(item):
    print('Searching...')
    amazonUrl = 'https://www.amazon.com/s?k='

    res = requests.get((amazonUrl + ' '.join(item)))
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    linkList = soup.find_all('a', attrs={'class' : 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    numOpen = min(1, len(linkList))
    for i in range(numOpen):
        urlOpen = amazonUrl + linkList[i].get('href')
        print('Opening' + urlOpen)
        webbrowser.open(urlOpen)



def main():
    print("Amazon or pypi?")
    typeSearch = input()
    typeSearch = typeSearch.lower()
    while (typeSearch != 'exit'):
        if (typeSearch == 'amazon'):
            print('Amazon Item to search for: ')
            item = input()
            amazon(item)
        elif (typeSearch == 'pypi'):
            print("Project to Search: ")
            term = input()
            pypi(term)
        else:
            print('command not recognized. try again? ')
            typeSearch = input
            typeSearch = typeSearch.lower()

main()
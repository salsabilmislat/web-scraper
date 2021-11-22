import requests
from bs4 import BeautifulSoup


URL='https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(URL):
    response = requests.get(URL)
    # print(response.text)
    # print(response.content)
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup)
    citation_needed= soup.find_all('a',title="Wikipedia:Citation needed")
    return len(citation_needed)


def get_citations_needed_report(URL):
    newArr=[]
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_needed= soup.find_all('a',title="Wikipedia:Citation needed")
    for i in citation_needed:
        newArr.append(i.parent.parent.parent.get_text())
    # print(len(newArr))

    return "\n".join(newArr)

# print(get_citations_needed_count(URL))
# print(get_citations_needed_report(URL))
# print(type(get_citations_needed_report()))

if __name__=="__main__":
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))


# import json

# with open('citation_needed.json', 'w') as f:
#     content = json.dumps(newArr)
#     f.write(content)

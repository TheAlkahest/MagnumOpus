import requests
# add import of BeautifulSoup
from bs4 import BeautifulSoup
import time

if __name__ == '__main__':
    response = requests.get("http://andythemoron.com")
    # Add use of BeautifulSoup to parse response
    soup = BeautifulSoup(response.content, "lxml")
    # Now we print the BeautifulSoup Object
    post_titles = soup.find_all("a", class_="post-title")
    extracted = []
    for post_title in post_titles:
        extracted.append({
            'title' : post_title['title'],
            'link' : "andythemoron.com" + post_title['href'] 
        })
        #Verify that data
        for data in extracted:
            print(data)
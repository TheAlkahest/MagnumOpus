import requests

if __name__ == '__main__':
    response = requests.get("http://andythemoron.com")
    # Let's print out the response for now to make sure we got some valid data back
    print(response.text)
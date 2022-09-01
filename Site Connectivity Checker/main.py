# import urllib
# use urllib.request to get data from the url
# write a function that takes a url
# returns a response

import urllib.request as urllib

def main(url):
    print("check connectivity ")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("The response code was", response.getcode())

print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")

main(input_url)

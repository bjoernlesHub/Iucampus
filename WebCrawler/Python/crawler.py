def get_html_from_website(url):
    from selenium import webdriver
    import time
    import os

    os.environ['MOZ_HEADLESS'] = '1'

    # start web browser
    browser=webdriver.Firefox()

    # get source code
    browser.get(url)
    html = browser.page_source
    time.sleep(2)
    #print(html)

    # close web browser
    browser.close()
    #print("browser geschlossen")
    return html

def get_value_from_website_by_id(url, html_element, id_of_element):
    """print(get_value_from_website_by_id("https://www.google.com/", "a", "gb_70"))"""
    from bs4 import BeautifulSoup
    import requests
    #r  = requests.get(url)
    #data = r.text
    
    #url = "https://www.facebook.com/groups/347805588637627/"
    #url = "https://www.google.com/"

    data = get_html_from_website(url)
    soup = BeautifulSoup(data, "html.parser")
    #print(soup.prettify())
    #span = soup.find("span", id="count_text")
    #input = soup.find("a", id="gb_70")
    input = soup.find(html_element, id=id_of_element)
    #print(input.text)
    return input.text
    #print(soup.prettify())

def get_value_from_website_by_class(url, html_element, class_of_element, count_of_element=0):
    """
    collection=get_value_from_website_by_class("https://www.ebay-kleinanzeigen.de/s-zu-verschenken/14797/c192l17124", "li", "ad-listitem",1)
    if len(collection) > 0:
        for entity in collection:
            print(entity)
    else:
        print("Anzahl war 0")
    """
    from bs4 import BeautifulSoup
    import requests

    #r  = requests.get(url)
    #data = r.text
    
    #url = "https://www.facebook.com/groups/347805588637627/"
    #url = "https://www.google.com/"
    
    data = get_html_from_website(url)
    soup = BeautifulSoup(data, "html.parser")
    #print(soup.prettify())
    #span = soup.find("span", id="count_text")
    elements = soup.find_all(html_element, class_=class_of_element)

    if count_of_element!=0:
        return elements[count_of_element]
    else:
        return elements
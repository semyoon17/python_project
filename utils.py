import urllib.request
from xml.dom import minidom

c = str(input('Введите код '))

def get_currency(c):

    URL = "http://www.cbr.ru/scripts/XML_daily.asp"
    Webfile = urllib.request.urlopen(URL)

    data = Webfile.read()
    dom = minidom.parseString(data)

    elements = dom.getElementsByTagName("Valute")
    currency_dict = {}

    for i in elements:
        for child in i.childNodes:
            if child.nodeType == 1:
                if child.tagName == "Value":
                    if child.firstChild.nodeType == 3:
                        value = float(child.firstChild.data.replace(',', '.'))
                if child.tagName == "CharCode":
                    if child.firstChild.nodeType == 3:
                        char_code = child.firstChild.data
        currency_dict[char_code] = value

    my_valute = currency_dict.get(c)
    print(my_valute)


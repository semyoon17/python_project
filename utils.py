def currency_rates(c= str(input('Введите код валюты: '))):
    from requests import get
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    rates = response.text
    m = rates.split('</Value></Valute>')
    index_d = rates.rfind('Date="') + 6
    date = rates[index_d:index_d+10]
    date_list = date.split('.')
    date_normal = '-'.join(date_list)
    for i, s in enumerate(m):
        crs = s[s.find('</CharCode>')-3:s.find('</CharCode>')]
        if crs == c:
            index_v = s.find('<Value>')
            s = (f'{s[index_v+7:]}')
            kurs = float(s.replace(',', '.'))
            print(f'{kurs}, {date_normal}')

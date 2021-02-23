import requests
from bs4 import BeautifulSoup

user = "VladBzS"
password = "rk#Kvkd32"
login_page = "https://www.usatrt.com/app/login.aspx?ReturnUrl=%2fapp%2fdefault.aspx"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0'}
login_data = {'Login1$txtName': user, 'Login1$txtPassword': password, "Login1$btnLogin": "Login" }
# A Session object will persist the login cookies.
with requests.Session() as s:
    page = s.get(login_page, headers=headers)
    soup = BeautifulSoup(page.content)
    login_data['__VIEWSTATE'] = soup.find('input', attrs={'id': '__VIEWSTATE'})['value']
    login_data['__VIEWSTATEGENERATOR'] = soup.find('input', attrs={'id': '__VIEWSTATEGENERATOR'})['value']
    login_data['__EVENTVALIDATION'] = soup.find('input', attrs={'id': '__EVENTVALIDATION'})['value']
    s.post(login_page, data=login_data, headers= headers)
    open_page = s.get("https://www.usatrt.com/app/Admin/Purchase.aspx#/purchases")

    #Check content
    if page.text == open_page.text:
        print("Same page")
    else:
        print(open_page.content)
        print("Different page!")


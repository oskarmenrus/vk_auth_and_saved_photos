import lxml.html
import requests
from bs4 import BeautifulSoup

#######################################################################################

login = 'logins'
password = 'password'

url = 'https://oauth.vk.com/authorize?client_id=id&display=page&redirect_uri=https://oauth.vk.com/blank.html&' \
      'scope=friends&response_type=token&v=5.92&state=123456'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 '
                  'Safari/537.36',
    'Content-Type': 'text/html'
}

######################################################################################

session = requests.session()

data = session.get(url, headers=headers)

page = lxml.html.fromstring(data.content)
form = page.forms[0]
form.fields['email'] = login
form.fields['pass'] = password

response = session.post(form.action, data=form.form_values())
print(response.url)

html = session.get('https://vk.com/audio', headers=headers)
print(html.url)
bsObj = BeautifulSoup(html.text, features="html.parser")
images = bsObj.findAll('span', {'class': 'audio_row__title_inner _audio_row__title_inner'})
for child in images:
    print(child.get_text())

# import vk_api
#
# vk_session = vk_api.VkApi('tel', '')
# vk_session.auth()
#
# vk = vk_session.get_api()
#
# print(vk.wall.post(message='Hello world!'))

# import lxml.html
# import requests
#
# login = 'tel'
# password = ''
# url = 'https://vk.com/'
#
# headers = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
#    (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#    'Accept-Language':'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
#    'Accept-Encoding':'gzip, deflate',
#    'Connection':'keep-alive',
#    'DNT':'1'
# }
#
# session = requests.session()
# data = session.get(url, headers=headers)
# page = lxml.html.fromstring(data.content)
#
# form = page.forms[0]
# form.fields['email'] = login
# form.fields['pass'] = password
#
# response = session.post(form.action, data=form.form_values())
# print(response.text)

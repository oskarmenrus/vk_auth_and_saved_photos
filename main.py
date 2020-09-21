import requests
# import json
import os

token = 'token
api_version = 5.101
my_id = 137576246
method_name = 'photos.get'
offset = 0
count = 0
url_list = []

url_ = f'https://api.vk.com/method/{method_name}?owner_id={my_id}&album_id=saved&' \
       f'count={count}&offset={offset}&access_token={token}&v={api_version}'
r = requests.get(url_)
count_img = r.json()["response"]["count"]

if count_img < 500:
    count_img += 500

for i in range(round(count_img / 1000)):
    url_ = f'https://api.vk.com/method/{method_name}?owner_id={my_id}&album_id=saved&' \
           f'count={1000}&offset={1000 * i}&access_token={token}&v={api_version}'
    r = requests.get(url_)
    for items in range(len(r.json()["response"]["items"])):
        url_list.append(r.json()["response"]["items"][items]["sizes"][-1]["url"])

if not os.path.exists('saved_photos'):
    os.mkdir('saved_photos')

for j in range(len(url_list)):
    r = requests.get(url_list[j]).content
    with open(f'saved_photos/saved_photo-{j}.jpg', 'wb') as photo:
        photo.write(r)

# with open('photos-{}.json'.format(i), 'w') as file:
#     json.dump(r.json(), file, indent=2, ensure_ascii=False)

# https://oauth.vk.com/authorize?client_id=6728883&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,messages,photos&response_type=token&v=5.52

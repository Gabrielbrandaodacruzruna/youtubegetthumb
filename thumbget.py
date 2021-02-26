import requests

video_id = input('enter with the youtube video code: ')


thumb = 'https://img.youtube.com/vi/' + video_id + '/maxresdefault.jpg'

r = requests.get(thumb)

with open(video_id + '.jpg', 'wb') as f:
    f.write(r.content)
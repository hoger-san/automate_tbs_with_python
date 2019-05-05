import urllib.request,urllib.error

url = 'https://scrapethissite.com/pages/simple/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}

request = urllib.request.Request(
    url=url,
    headers=headers
    )

try:
    response = urllib.request.urlopen(request)
except urllib.error.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib.error.URLError as e:
    print('URLError: {}'.format(e.reason))
else:
    print(response.read())
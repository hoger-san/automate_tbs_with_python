import urllib.request,urllib.error

url = 'https://scrapethissite.com/pages/simple/'
request = urllib.request.Request(url=url)

try:
    response = urllib.request.urlopen(request)
except urllib.error.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib.error.URLError as e:
    print('URLError: {}'.format(e.reason))
else:
    print(response.read())

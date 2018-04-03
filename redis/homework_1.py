import urllib.request
url = "https://api.nasa.gov/planetary/apod?api_key=3wqvhsbQ7ZvtvdDI2fNdDVvSNe5u22TiTQOsvgB9&date=2017-12-18"
contents = urllib.request.urlopen(url).read().decode("utf-8")
l = contents.split('\n')
for line in l:
    a = line.split(":", 1)
    if a[0].endswith('"url"'):
        print(a[1].strip()[1:-1])

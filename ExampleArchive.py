import webbrowser
import json
from urllib.request import urlopen
print("Lets find an old website")
site = input("Type a website URL    ")
era = input("Type year month and day example 20150613")
url = "http://archive.org/wayback/availble?url=%s&timestamp=%s" % (site, era)
responce = urlopen(url) 
contents = responce.read()
text = contents.decode("utf-8")
data = json.loads(text)
try:
    old_site = data["archived_snapshot"] ["closest"] ["url"]
    print("Found this copy", old_site)
    print("It should open now")
    webbrowser.open(old_site)
except:
    print("No site found!!")
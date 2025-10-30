import urllib.request
import json

contents = urllib.request.urlopen("https://api.massive.com/openapi").read()
parsed = json.loads(contents)
formatted = json.dumps(parsed, indent=2)
with open(".massive/rest.json", "w") as f:
    f.write(formatted)

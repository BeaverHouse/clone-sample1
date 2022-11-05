import json

a = {
    "inputDir": "/sample/input",
    "outputDir": "/sample/output",
    "nasPath": "D:/fake_nas"
}

parsed_str = json.dumps(a).replace('"', '\"\"')

print("'{}'".format(parsed_str))

# '{""inputDir"": ""/sample/input"", ""nasPath"": ""D:/fake_nas""}'
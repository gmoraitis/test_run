#!/usr/bin/python
import jinja2
import yaml

templateFilePath = jinja2.FileSystemLoader('./')

jinjaEnv = jinja2.Environment(loader=templateFilePath)

jTemplate = jinjaEnv.get_template("index.html")

with open("input.yml") as config:
    config = yaml.load(config)

#connecting template with yml    
output = jTemplate.render(config)

print(output)
outFileH = open('index.html', 'w')
outFileH.write(output)
outFileH.close()

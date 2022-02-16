#!/usr/bin/env python3

import yaml
from jinja2 import Environment, FileSystemLoader
from jinja_markdown import MarkdownExtension

DIVIDER = "#"*80
BASE_FOLDER = "./"

# init the jinja stuff
file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)
env.add_extension(MarkdownExtension)

# load the context from the metadata file
context = dict()
with open('metadata.yml') as f:
    context = yaml.load(f, Loader=yaml.FullLoader)

venues_by_name = dict()
for venue in context.get("venues", []):
    venues_by_name[venue.get("name")] = venue.get("url")
context["venues_by_name"] = venues_by_name

# MAIN PAGES
print(DIVIDER)
print("Generating main pages")
for page in ["index.html"]:
    with open(BASE_FOLDER + "/" + page, "w") as f:
        print("Writing out", page)
        template = env.get_template(page)
        f.write(template.render(page=page, **context))

print(DIVIDER)
print("Done")

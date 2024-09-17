#!/usr/bin/env python
import json
import re
import requests
import sys


class PyCode:
    comment_pattern = re.compile("\{Comment \d+\}")
    def __init__(self, pcs):
        if 'comments' in pcs:
            self.comments = [_['comment'] for _ in pcs['comments']]
        raw_code = pcs['code']
        self.code = PyCode.comment_pattern.sub('{}', raw_code).format(*self.comments) if 'comments' in pcs else raw_code

    def __str__(self):
        return "\n```python\n" + self.code + "\n```\n"

class Content:
    def __init__(self, cs):
        self.line = self.parse_content(cs)

    def parse_content(self, c):
        if "text" in c:
            return c['text']['content'].replace("$", "`").replace("**", "")
        elif "images" in c:
            return '\n'.join([f"![]({content_base_url + _['url']})" for _ in c['images']['image']])
        elif "python_code_stacks" in c:
            return ''.join([str(PyCode(_)) for _ in c['python_code_stacks']['python_code_stack']])
        elif "code_stacks" in c:
            return '\n'.join([f"![]({content_base_url + _['render']['url']})\n\n" for _ in c['code_stacks']['code_stack']])
        else:
            print("OUCH")
            return [None]
    def __str__(self):
        return self.line

class Page:
    def __init__(self, dx, level=1):
        self.level = level
        self.page_title = dx['page_title'].replace("$", "`")
        if 'sub_pages' in dx:
            self.sub_pages = [str(Page(x, self.level + 1)) for x in dx['sub_pages']]
        else:
            self.sub_pages = []
        self.content = [str(Content(_)) for _ in dx['content']]

    def __str__(self):
        return "\n" + "#"* self.level + ' ' +  self.page_title + '\n' +  ''.join(self.content) + ''.join(self.sub_pages)

if __name__ == "__main__":
    content_base_url =  "https://spike.legoeducation.com/content/"
    doc_link = content_base_url + "en-US/documents.json"
    cont = requests.get(doc_link)

    if cont.status_code != 200:
        print(f"There was an error fetching docs from Lego. Please verify if link {doc_link} is still valid")
        sys.exit()
    else:
        resp = cont.json()
        print("Here the documentation generation option available:")
        print("1. Python ALL")
        print("2. Python Intro")
        print("3. Python API reference")
        print("4. Word Blocks")
        print("5. Icon Blocks")

        selection = input("Enter your choice number: ")
        try:
            selection = int(selection)
            if selection not in {1,2,3,4,5}:
                print("Invalid Selection")
                sys.exit()
        except:
            print("Invalid Selection")
            sys.exit()
        
        options = [
            None,
            {'json_path': resp['en-us']["sub_pages"][0]["sub_pages"][2], "filename": "Spike All Python.md"},
            {'json_path': resp['en-us']["sub_pages"][0]["sub_pages"][2]["sub_pages"][0], "filename": "Spike Python Intro.md"},
            {'json_path': resp['en-us']["sub_pages"][0]["sub_pages"][2]["sub_pages"][1], "filename": "Spike Python API Ref.md"},
            {'json_path': resp['en-us']["sub_pages"][0]["sub_pages"][1], "filename": "Spike Word Blocks.md"},
            {'json_path': resp['en-us']["sub_pages"][0]["sub_pages"][0], "filename": "Spike Icon Blocks.md"},
        ]

        page = Page(options[selection]['json_path'])
        legal_docs = Page(resp['en-us']["sub_pages"][1])
        with open(options[selection]['filename'], 'w', encoding='utf8') as f:
            f.write(str(page))
            f.write(str(legal_docs))
            print(f"Generating {options[selection]['filename']} complete.")
        

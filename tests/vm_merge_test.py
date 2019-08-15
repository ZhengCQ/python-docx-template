#!/usr/bin/env python
import sys
import re
import os



import json

from docxtpl import DocxTemplate, RichText,InlineImage
from docx.shared import Mm, Inches, Pt

#injson=sys.argv[1]
#outdoc=sys.argv[2]
injson = 'templates/vm_merge_tpl.json'
outdoc = 'templates/vm_merge_test.docx'

tpl = './templates/vm_merge_tpl.docx'
tmp = DocxTemplate(tpl)


with open(injson, 'r') as fi:
    info_dict = json.load(fi)

tmp.render(info_dict)
tmp.save(outdoc)
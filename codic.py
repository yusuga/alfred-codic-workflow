#!/usr/bin/env python
# -*- coding=utf-8 -*-

import sys
from workflow import Workflow
from urllib import urlencode
from urllib2 import Request, urlopen
import json

url = 'https://codic.jp/-/engine/translate.json'
headers = {'X-Requested-With': 'XMLHttpRequest'}

def main(wf):
    query = wf.args[0]

    values = {'acronym_style': 'literal',
              'casing': 'lower underscore'.encode('utf-8'),
              'dictionary_id': '0',
              'data[0][id]': '0',
              'data[0][text]': query.encode('utf-8')}

    res = urlopen(Request(url, urlencode(values), headers))
    j = json.loads(res.read())
    #wf.logger.debug(j)
    text = j['data']['translation'][0]['translation']['translatedText']

    if not len(text):
        text = 'No Results'

    wf.add_item(title = text, icon='icon.png', arg = text, valid = True)
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))

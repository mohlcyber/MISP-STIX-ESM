#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import requests

from pymisp import PyMISP

requests.packages.urllib3.disable_warnings()

url = "https://misp-ip-address"
key = "api-key"

misp = PyMISP(url, key, False, 'json', debug=False)

headers = {'Authorization': key,
           'Accept': 'application/xml',
           'content-type': 'application/xml',
           'User-Agent': 'PyMISP'
          }

def search(tag):
    res = misp.search(tags=tag)
    return res

def getstix(eventid):
    weburl = '{0}/events/stix/download/{1}'.format(url, eventid)
    res = requests.get(weburl, headers=headers, verify=False, allow_redirects=True)

    #Define the path to a folder that should contain the STIX files
    with open('stix/misp_stix_%s.xml' % eventid, 'wb') as f:
        f.write(res.content)

def update_tag(uuid, ntag):
    res = misp.tag(uuid, ntag)
    return res


if __name__ == '__main__':

    tag = "indicator_found"

    misp_result = search(tag)

    try:
        if not misp_result['response']:
            pass
        for event in misp_result['response']:
            eventid = event['Event']['id']
            euuid = event['Event']['uuid']

            stix = getstix(eventid)
            print('Successfully exported the STIX file for event %s' % eventid)

            objects = event['Event']['Object']
            for fields in objects:
                for attributes in fields['Attribute']:
                    attuuid = attributes['uuid']
                    try:
                        for tags in attributes['Tag']:
                            atttag = tags['name']
                            if atttag == tag:
                                misp.untag(attuuid, tag)
                    except:
                        pass

            attributes = event['Event']['Attribute']
            for fields in attributes:
                attuuid = fields['uuid']
                try:
                    for tags in attributes['Tag']:
                        atttag = tags['name']
                        if atttag == tag:
                            misp.untag(attuuid, tag)
                except:
                    pass

            misp.untag(euuid, tag)

    except Exception as e:
        print("Something went wrong %s" % e)

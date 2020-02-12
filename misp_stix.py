#!/usr/bin/env python3
# Written by mohlcyber v.0.3 12/02/2020

import sys
import requests
import time

from pymisp import ExpandedPyMISP

requests.packages.urllib3.disable_warnings()

misp_url = 'https://1.1.1.1/'
misp_verify = False
misp_key = 'API Key'
misp_tag = 'McAfee: Export to ESM'
misp_path = 'stix/'


class MISP():
    def __init__(self):
        self.misp = ExpandedPyMISP(misp_url, misp_key, False)
        self.headers = {
            'Authorization': misp_key,
            'Accept': 'application/xml',
            'User-Agent': 'PyMISP'
        }

    def get_events(self, **kwargs):
        tags = kwargs.pop('tags', None)
        format = kwargs.pop('format', None)
        eid = kwargs.pop('eid', None)
        res = self.misp.search(eventid=eid, tags=tags, return_format=format)
        return res

    def get_stix(self, eventid, format):
        payload = {
            "returnFormat": format,
            "eventid": eventid
        }
        stix = requests.post(misp_url + 'events/restSearch', headers=self.headers, data=payload, verify=misp_verify)
        return stix.content

    def main(self):
        results = self.get_events(tags=misp_tag, format='json')
        try:
            if results:
                for result in results:
                    eventid = result['Event']['id']
                    euuid = result['Event']['uuid']

                    stix = self.get_stix(eventid, 'stix')
                    with open(misp_path + 'misp_stix_{0}.xml'.format(str(eventid)), 'w') as esm_stix:
                        esm_stix.write(stix.decode())
                        esm_stix.close()
                    print('SUCCESS: Successful exported the STIX file for event {0}.'.format(str(eventid)))

                    objects = result['Event']['Object']
                    for fields in objects:
                        for attributes in fields['Attribute']:
                            attuuid = attributes['uuid']

                            if 'Tag' in attributes:
                                for tags in attributes['Tag']:
                                    atttag = tags['name']
                                    if atttag == misp_tag:
                                        self.misp.untag(attuuid, misp_tag)

                    attributes = result['Event']['Attribute']
                    for fields in attributes:
                        attuuid = fields['uuid']

                        if 'Tag' in fields:
                            for tags in fields['Tag']:
                                atttag = tags['name']
                                if atttag == misp_tag:
                                    self.misp.untag(attuuid, misp_tag)

                    self.misp.untag(euuid, misp_tag)

            else:
                print('STATUS: Could not find Events that are tagged with {0}.'.format(str(misp_tag)))
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print("ERROR: Error in {location}.{funct_name}() - line {line_no} : {error}"
                  .format(location=__name__, funct_name=sys._getframe().f_code.co_name, line_no=exc_tb.tb_lineno,
                          error=str(e)))


if __name__ == '__main__':

    while True:
        misp = MISP()
        misp.main()
        time.sleep(60)
# MISP-STIX-ESM
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This Script will download MISP events in STIX format. McAfee ESM will be configured to poll STIX files from the folder location via SCP and run automated triage processes.

<img width="954" alt="screen shot 2018-06-26 at 16 31 48" src="https://user-images.githubusercontent.com/25227268/41919328-86c9e7ba-795e-11e8-80ef-7bfbe1468158.png">

## Component Description

**McAfee Enterprise Security Manager (ESM)**  is a security information and event management (SIEM) solution that delivers actionable intelligence and integrations to prioritize, investigate, and respond to threats.
https://www.mcafee.com/enterprise/en-us/products/enterprise-security-manager.html

**MISP** threat sharing platform is free and open source software helping information sharing of threat and cyber security indicators.
https://github.com/MISP/MISP

## Prerequisites

Download the [Latest Release](https://github.com/mohlcyber/MISP-STIX-ESM/releases)
   * Extract the release .zip file
   
MISP platform installation ([Link](https://github.com/MISP/MISP)) (tested with MISP 2.4.92)

Requests ([Link](http://docs.python-requests.org/en/master/user/install/#install))

PyMISP library installation ([Link](https://github.com/MISP/PyMISP))
```sh
git clone https://github.com/MISP/PyMISP.git
cd PyMISP/
python setup.py install
```

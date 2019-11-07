# MISP-STIX-ESM
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This Script will download MISP events in STIX format. McAfee ESM will be configured to pull STIX files from the folder location via SCP and run automated triage processes.

<img width="954" alt="screen shot 2018-06-26 at 16 31 48" src="https://user-images.githubusercontent.com/25227268/41919328-86c9e7ba-795e-11e8-80ef-7bfbe1468158.png">

## Component Description

**McAfee Enterprise Security Manager (ESM)**  is a security information and event management (SIEM) solution that delivers actionable intelligence and integrations to prioritize, investigate, and respond to threats.
https://www.mcafee.com/enterprise/en-us/products/enterprise-security-manager.html

**MISP** threat sharing platform is free and open source software helping information sharing of threat and cyber security indicators.
https://github.com/MISP/MISP

## Prerequisites

Download the [Latest Release](https://github.com/mohlcyber/MISP-STIX-ESM/releases)
   * Extract the release .zip file
   
MISP platform installation ([Link](https://github.com/MISP/MISP)) (tested with MISP 2.4.117)

Requests ([Link](http://docs.python-requests.org/en/master/user/install/#install))

PyMISP library installation ([Link](https://github.com/MISP/PyMISP))
```sh
git clone https://github.com/MISP/PyMISP.git
cd PyMISP/
python setup.py install
```
## Configuration
MISP receives intelligence feeds from multiple sources. The provided script will export tagged events as STIX files and McAfee ESM will pull these STIX files for automated investigations.

### misp_stix.py
The misp_stix.py script will export tagged events as STIX files to a given location.

Enter the MISP IP/URL, API key, MISP Tag to look for and the location where the STIX files should be stored (line 12 - 15).

<img width="359" alt="Screenshot 2019-11-07 at 11 48 33" src="https://user-images.githubusercontent.com/25227268/68382708-8fd1e680-0154-11ea-9854-850ba99aae41.png">

### ESM Configuration

Log into the McAfee ESM platform and open ESM properties.
Go to the Cyber Threat Feeds and add a new feed. In the source enter the IP, username, password and path to the folder that contains the STIX files that got previous downloaded through the misp_stix.py script.

<img width="762" alt="screen shot 2018-06-27 at 18 30 04" src="https://user-images.githubusercontent.com/25227268/41986979-26067152-7a38-11e8-9e01-369e0911733e.png">

Define the frequency, watchlist and backtrace options to automate triage steps.

McAfee ESM will pull new STIX file and check if any events have been seen in the past related to the artifacts.

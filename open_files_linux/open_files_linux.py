#!/usr/bin/python3

### Author: Vinoth Manoharan, Zoho Corp
### Language : Python
### Tested in Ubuntu

import sys,json

#if any impacting changes to this plugin kindly increment the plugin version here.
PLUGIN_VERSION = "1"

#Setting this to true will alert you when there is a communication problem while posting plugin data to server
HEARTBEAT="true"


PROC_FILE = "/proc/sys/fs/file-nr"

METRIC_UNITS = {'open_files': 'units', 'total_files': 'units'}

def metricCollector():
    data = {}
    try:
        open_nr, free_nr, max = open(PROC_FILE).readline().split("\t")
        open_files = int(open_nr) - int(free_nr)
        data["open_files"] = open_files
        data["total_files"] = int(max)
    except Exception as e:
        print ("status error ",e)
        data["error"] = str(e)
    data["units"] = METRIC_UNITS
    return data

if __name__ == "__main__":
    result = metricCollector()
    
    print(json.dumps(result, indent=4, sort_keys=True))
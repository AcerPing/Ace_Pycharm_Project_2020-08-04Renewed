
# This file was generated by 'versioneer.py' (0.15) from
# revision-control system data, or from the parent directory name of an
# unpacked source archive. Distribution tarballs contain a pre-generated copy
# of this file.

from warnings import catch_warnings
with catch_warnings(record=True):
    import json
import sys

version_json = '''
{
 "dirty": false,
 "error": null,
 "full-revisionid": "b687cd4d9e520666a956a60849568a98dd00c672",
 "version": "1.0.5"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)
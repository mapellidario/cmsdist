### RPM external py3-requests 2.25.1
## IMPORT build-with-pip3

Requires: py3-certifi py3-urllib3 py3-idna py3-chardet

%define PipPostBuild perl -p -i -e "s|^#!.*python|#!/usr/bin/env python|" %{i}/bin/*
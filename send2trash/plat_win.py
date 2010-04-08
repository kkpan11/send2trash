# Copyright 2010 Hardcoded Software (http://www.hardcoded.net)

# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

import os.path as op
import _send2trash_win

def send2trash(path):
    if not isinstance(path, unicode):
        path = unicode(path, 'mbcs')
    if not op.isabs(path):
        path = op.abspath(path)
    _send2trash_win.send(path)
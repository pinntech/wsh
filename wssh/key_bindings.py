#!/usr/bin/env python
"""
:copyright: (c) 2018 Pinn Technologies, Inc.
:license: All rights reserved
"""

__version__ = '0.1.0'

from prompt_toolkit.key_binding import KeyBindings


key_bindings = KeyBindings()

@key_bindings.add(u'c-c')
@key_bindings.add(u'c-q')
def _(event):
    " Pressing Ctrl-Q or Ctrl-C will exit the user interface. "
    event.app.exit()

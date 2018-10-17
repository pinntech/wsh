"""
:copyright: (c) 2018 Pinn Technologies, Inc.
:license: All rights reserved
"""

def test_import():
    import wssh
    from wssh import WSSH


def test_wssh():
    from wssh import WSSH
    wssh = WSSH(host='ws://127.0.0.1:7001/ws/connection')
    wssh.run()

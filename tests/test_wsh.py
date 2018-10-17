"""
:copyright: (c) 2018 Pinn Technologies, Inc.
:license: All rights reserved
"""

def test_import():
    import wsh
    from wsh import WSH


def test_wsh():
    from wsh import WSH
    wsh = WSH(host='ws://127.0.0.1:7001/ws/connection')
    wsh.run()

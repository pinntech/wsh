"""
:copyright: (c) 2018 Pinn Technologies, Inc.
:license: All rights reserved
"""


def test_import():
    import wsh
    from wsh import WSH


def test_wsh():
    from wsh import WSH

    def foo_command(argument):
        return "bar " + argument

    def receiver(message, connection):
        connection.info('Woohoo, received the important message.')
        connection.display('[-] Important Message:')
        connection.display(message.decode('utf-8'))
        connection.send(sender=None, data='hello world')

    wsh = WSH(host='ws://127.0.0.1:7001/ws/connection',
              senders={"foo": foo_command},
              receiver=receiver)
    wsh.run()

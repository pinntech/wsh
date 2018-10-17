.. |pypi| image:: https://img.shields.io/pypi/v/wssh.svg?style=flat-square
    :target: https://pypi.python.org/pypi/wssh
.. |license| image:: https://img.shields.io/pypi/l/wssh.svg?style=flat-square
    :target: https://pypi.python.org/pypi/wssh

****
WSSH
****
|pypi| |license| 

WSSH is a command line interface that launches a shell to send and recieve
messages from a WebSocket server. It was designed to be simplistic and allow
developers to easily connect/send/receive data over a WS with very little effort.

Quickstart
==========

Install via PyPi:

.. code-block:: shell

    pip install wssh


Then simply call the command line tool with your WebSocket server host, you should
also specify the WebSocket protocol ("ws" or "wss")

.. code-block:: shell

    wssh ws://127.0.0.1:7001/ws/connection


For more complex scenarios you can launch the shell manually via a simple python script.

.. code-block:: python

     from wssh import WSSH


     def main():
         # Custom Logic
         # ............
         wssh = WSSH(host='ws://127.0.0.1:7001/ws/connection')
         wssh.run()


     if __name__ == '__main__':
         main()

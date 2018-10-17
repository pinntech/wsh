`wsh` - WebSocket sHell
***********************

.. currentmodule:: wsh


Installation
------------

::

   pip install wsh

Quick start
-----------

Then simply call the command line tool with your WebSocket server host, you should
also specify the WebSocket protocol ("ws" or "wss")

.. code-block:: shell

    wsh ws://127.0.0.1:7001/ws/connection


For more complex scenarios you can launch the shell manually via a simple python script.

.. code-block:: python

     from wsh import WSH


     def main():
         # Custom Logic
         # ............
         wsh = WSH(host='ws://127.0.0.1:7001/ws/connection')
         wsh.run()


     if __name__ == '__main__':
         main()


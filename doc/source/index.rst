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


Senders
-------

If you would like to program in some of your own commands to send data you can register
a sender. These are roughly equivalent to macro expansions, your function will be registered
to a single command string with no spaces and should return a string - which is the data you
want to be sent over the wire. Your function may also accept the argument parameter which
passes all the data the user sends after the command and space.


.. code-block:: python

     from wsh import WSH


     if __name__ == '__main__':
        
         def foo(argument):
             """
             This command will translate out to the user typing:
             `send foo {argument}`
             """
             return "foo {}".format(argument)

         # Here we define the command name as 'foo' and pass in the function
         wsh = WSH(host='ws://127.0.0.1:7001/ws/connection',
                   senders={'foo': foo})
         wsh.run()

    # ...
    # At runtime used against an echo server
    # >>> foo bar baz
    # >>> sent
    # foo bar baz
    # <<< received
    # foo bar baz

    
Receiver
--------

You can also register a callback when a message is received, to insert your own custom logic
and also cat to wsh. The function you write should handle both a message and connection as
a parameter. This simple receiver shows you how to intercept the message and the do some 
custom output to the shell, and then send another message in reply to the incoming one.

You could for example decode JSON data in the receiver function and create a very custom
handler


.. code-block:: python

     from wsh import WSH


     if __name__ == '__main__':
        
         def receiver(message, connection):
             connection.info('Woohoo, received the important message.')
             connection.display('[-] Important Message:')
             connection.display(message.decode('utf-8'))
             # Send a message, sender is None since we are calling from a
             # classless function
             connection.send(sender=None, data='hello world')

         # Here we define the command name as 'foo' and pass in the function
         wsh = WSH(host='ws://127.0.0.1:7001/ws/connection',
                   receiver=receiver)
         wsh.run()

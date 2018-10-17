#!/usr/bin/env python
"""
:copyright: (c) 2018 Pinn Technologies, Inc.
:license: All rights reserved
"""

__version__ = '0.1.0'

from blinker import signal
from enum import Enum, unique
from prompt_toolkit.document import Document
from prompt_toolkit.application.current import get_app


@unique
class Command(Enum):
    EXIT = 'exit'
    NONE = ''
    SEND = 'send'
    OPEN = 'open'
    CLOSE = 'close'
    HELP = 'help'


class CommandProcessor:

    def __init__(self):
        self.wssh_send = signal('wssh-send')
        self.commands = dict()

    def process_command(self, command, argument, input_field, output_field):
        if command == Command.NONE:
            input_field.text = u""
        elif command == Command.EXIT:
            get_app().exit()
        elif command == Command.SEND:
            wssh_send = signal('wssh-send')
            wssh_send.send(self, data=argument)

    def accept_handler(self, buf, input_field, output_field):
        """Callback method invoked when <ENTER> is pressed."""
        try:
            tokens = input_field.text.split(' ')
            command = Command(tokens[0])
            cmd, sep, args = input_field.text.partition(' ')
            argument = tokens[1] if len(tokens) > 1 else None
            self.process_command(command, args, input_field, output_field)
        except ValueError:
            output = u'Command not found, type "help" to see available commands.'
            output = output_field.text + '\n' + output
            output_field.buffer.document = Document(text=output,
                                                    cursor_position=len(output))
        input_field.text = u""

    def register_command(self, name, command):
        """Register a new command as a callable function name in the shell."""
        self.commands[name] = command

#def write_repeat (message, n):
#    for i in range (n):
#        print (message)
#write_repeat ("Hello", 5)


def hof_write_repeat (message, n, action):
    for i in range (n):
        action (message)
hof_write_repeat ("Hello", 5, print)

# Import the logging library
import logging

# Log the output as an error instead
hof_write_repeat ("hello", 5, logging.error)
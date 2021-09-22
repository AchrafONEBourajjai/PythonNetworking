from pprint import pprint #for organise results
import socket
info = socket.getaddrinfo('fedoraproject.org','www')
pprint(info[0]) # display just tupel number 0
pprint(info[0:4]) #display results from tupel 0 to 4
#!/usr/bin/python

import optparse
from socket import *
from termcolor import colored as col

class Client:

    def make_conn(self, msg, ip, port):
        try:
            with socket(AF_INET, SOCK_STREAM) as s:
                if s.connect_ex((ip, port)):
                    pass
                else:
                    s.sendall(f"{msg}".encode())
                    print(f"{col('[*]', 'green')} Message sent")
                    return
        except:
            print(f"{col('[-]', 'red')} Error, message not sent")

def main():

        parser = optparse.OptionParser("python listener.py -m random_txt -d 127.0.0.1 -p 12345")
        parser.add_option('-p', '--prt', dest='port', type='int', help='To set port to connect to')
        parser.add_option('-d', '--dst', dest='dest', type='str', help='To set IP address to connect to')
        parser.add_option('-m', '--msg', dest='mesg', type='str', help='Message to send')

        (options, args) = parser.parse_args()

        if options.port == None:
            print(f'{parser.usage} port can be set with the -p or --prt flag')
            exit(0)

        if options.dest == None:
            print(f'{parser.usage} IP address can be set with the -d or --dst flag')
            exit(0)

        if options.mesg == None:
            print(f'{parser.usage} message can be set with the -m or --msg flag')
            exit(0)

        client = Client()
        client.make_conn(options.mesg, options.dest, options.port)

if __name__ == '__main__':
    main()

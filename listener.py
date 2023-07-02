from socket import *
from termcolor import colored as col
import optparse

class Server:

    def start_server(self, port):

        with socket(AF_INET, SOCK_STREAM) as s:
            s.bind(('', port))
            s.listen()
            print(f"{col('[*]', 'yellow')} Server listening on {port}")

            try:
                while True:
                    c, a = s.accept()
                    print(f"{col('[*]', 'green')} Connection from {a[0]}")
                    data = c.recv(1024).decode()
                    print(f"{col('[+]', 'green')} Data received")
                    with open('.logg.txt', 'w') as l:
                        l.write(data)

            except KeyboardInterrupt:
                print(f"\n{col('[-]', 'red')} Server shutting down")
                exit(0)

def main():

    parser = optparse.OptionParser("python listener.py -p 12345")
    parser.add_option('-p', '--prt', dest='port', type='int', help='To set port to listen on')
    (options, args) = parser.parse_args()

    if options.port == None:
        print(f'port can be set with the -p or --prt flag\nexample: {parser.usage}')
        exit(0)

    server = Server()
    server.start_server(options.port)

if __name__ == '__main__':
    main()

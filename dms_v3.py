#!/usr/bin/pyhon

import optparse
from datetime import datetime
from time import sleep

class FileMonitor(object):

    @staticmethod
    def get_time_ints():

        while True:
            ints = []
            res = datetime.now()
            res = str(res).split(' ')
            res = res[1].split(':')
            hour = int(res[0])
            minute = int(res[1])
            sec = res[2].split('.')
            sec = int(sec[0])

            ints.append(hour)
            ints.append(minute)
            ints.append(sec)

            return ints

    @staticmethod
    def start_check(passwd, file_to_del, timer='23:59'):

        in_t = timer.split(':')
        in_hr = int(in_t[0])
        in_mn = int(in_t[1])
        in_mn = in_mn - 1
        print(f"[*] Timer set for {timer}:00\n[*] Monitoring ...")

        try:
            while True:

                times = FileMonitor.get_time_ints()

                if times[0] == in_hr and times[1] == in_mn and times[2] == 58:

                    with open('.logg.txt', 'r') as l:
                        conts = l.read()

                    if conts != passwd:
                        print('[*] Deleting File')
                        with open(file_to_del, 'w') as sc:
                            sc.write('')
                            exit(0)
                    else:
                        print('[+] Correct passcode received')
                        with open('.logg.txt', 'w') as lg:
                            lg.write('')
                        sleep(10)
                else:
                    continue

        except KeyboardInterrupt:
            print("\n[!] User terminated process")

def main():

    parser = optparse.OptionParser("dms_v3.py -p passcode -f file.txt")
    parser.add_option('-p', '--pass', dest='pas', type='str', help='Passcode to authenticate against')
    parser.add_option('-f', '--file', dest='file', type='str', help='Absolute path of file to delete')
    (options, args) = parser.parse_args()
    f = ''
    p = ''

    if options.pas is None:
        print(f'[*] Enter passcode to auth against\n\nexample:\n{parser.usage}')
        exit(0)
    else:
        p = options.pas

    if options.file is None:
        print(f'{parser.usage}\n[*] Enter path of file to delete if passcode auth fails')
        exit(0)
    else:
        f = options.file

    FileMonitor.start_check(p, f)

if __name__ == '__main__':
    main()

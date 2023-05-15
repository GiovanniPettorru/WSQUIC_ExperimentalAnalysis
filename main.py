import os
import subprocess

if __name__ == '__main__':
    try:
        process = subprocess.Popen(['python', 'WSclientserver/serverWSQUIC.py', '--certificate',
                                    'WSclientserver/tests/ssl_cert.pem', '--private-key',
                                    'WSclientserver/tests/ssl_key.pem'])
        print('Starting the Server.\nPID: ' + str(process.pid))
    except:
        print('Server Error')
        exit()

    while True:
        try:
            inputmode = int(input('Choose 1 for 1-RTT mode client, 0 for 0-RTT mode client, 5 to close the '
                                  'client/server script.\n'))
            if inputmode == 1:
                try:
                    os.system('python WSclientserver/clientWSQUIC.py --ca-certs WSclientserver/tests/pycacert.pem '
                              'wss://localhost:4433/ws')
                except:
                    process.kill()

            elif inputmode == 0:
                try:
                    os.system('python WSclientserver/clientWSQUIC.py --ca-certs tests/pycacert.pem --session-ticket '
                              'WSclientserver/tests/ticket.bin wss://localhost:4433/ws')
                except:
                    process.kill()
            elif inputmode == 5:
                print('Goodbye')
                process.kill()
                break
            else:
                print('Not valid option')
                process.kill()
        except:
            process.kill()
            break

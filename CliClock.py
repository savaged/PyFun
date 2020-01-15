import time
import datetime


def getTimeStr():
    return datetime.datetime.now().strftime('%H:%M.%S')


def write(output):
    print(output, end='\r')


def writeSplash():
    print('Ctrl+C to quit')


def writeClose():
    print('\b\b\b\b\b\b\b\b' + getTimeStr())


def main():
    writeSplash()
    while True:
        write(getTimeStr())
        time.sleep(1)


try:
    main()
except (KeyboardInterrupt):
    writeClose()
    quit()
import time
import datetime


def getDeltaStr(lhs, rhs):
    return str(lhs - rhs)


def getDateTime():
    return datetime.datetime.now()


def write(output):
    print(output, end='\r')


def writeSplash():
    print('Ctrl+C to quit')


def writeClose():
    print()


def main():
    start = getDateTime()
    writeSplash()
    while True:
        now = getDateTime()
        write(getDeltaStr(now, start))
        time.sleep(1)


try:
    main()
except (KeyboardInterrupt):
    writeClose()
    quit()

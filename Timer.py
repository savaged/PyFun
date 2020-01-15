import time
import datetime


def getDeltaStr(lhs, rhs):
    delta = lhs - rhs
    return str(getHours(delta)) + ":" \
        + str(getMinutes(delta)) + \
        "." + str(getSeconds(delta))


def getHours(delta):
    return int(round(delta.seconds / 3600, 0))


def getMinutes(delta):
    return int(round((delta.seconds / 60) % 60, 0))


def getSeconds(delta):
    return round(delta.seconds, 0)


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
        write("   " + getDeltaStr(now, start))
        time.sleep(1)


try:
    main()
except (KeyboardInterrupt):
    writeClose()
    quit()

import time
import datetime


def getDeltaStr(lhs, rhs):
    delta = lhs - rhs
    return str(getHours(delta)).zfill(2) + ":" \
        + str(getMinutes(delta)).zfill(2) + \
        "." + str(getSeconds(delta)).zfill(2)


def getHours(delta):
    return delta.seconds // 3600


def getMinutes(delta):
    return (delta.seconds // 60) % 60


def getSeconds(delta):
    return delta.seconds % 60


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

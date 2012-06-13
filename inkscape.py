import subprocess

def run(*args):
    print "inkscape",
    for arg in args:
        print arg,
    print
    log = open("inkscape.log", "w")
    subprocess.call(["inkscape"] + list(args), stdout = log, stderr = log)
    log.close()

import popen2

def nkf(s, opt=None):
    cmd = "nkf"
    if opt:
        cmd = cmd + " " + opt
    p = popen2.Popen4(cmd)
    p.tochild.write(s)
    p.tochild.close()
    s = p.fromchild.read()
    r = p.wait()
    if r == 0:
        return s
    else:
        raise Exception((r, s))

if __name__ == '__main__':
    import sys
    s = sys.stdin.read()
    t = nkf(s, "-e")            # convert to EUC-JP
    sys.stdout.write(t)


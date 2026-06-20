# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ioctl.py
# case: IoctlTests_test_ioctl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ids = (os.getpgrp(), os.getsid(0))
    with open('/dev/tty', 'rb') as tty:
        r = fcntl.ioctl(tty, termios.TIOCGPGRP, '    ')
        rpgrp = struct.unpack('i', r)[0]
        self.assertIn(rpgrp, ids)

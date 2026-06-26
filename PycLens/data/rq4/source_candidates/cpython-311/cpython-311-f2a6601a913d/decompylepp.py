# Source Generated with Decompyle++
# File: cpython-311-f2a6601a913d.pyc (Python 3.11)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fp = open(os_helper.TESTFN)
    fd = posix.dup(fp.fileno())
    self.assertIsInstance(fd, int)
    os.close(fd)
    fp.close()
    return None
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    __pybcsec_seed__()
    return None

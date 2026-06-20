# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FileTests_test_closerange

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    first = os.open(os_helper.TESTFN, os.O_CREAT | os.O_RDWR)
    second = os.dup(first)
    try:
        retries = 0
        while second != first + 1:
            os.close(first)
            retries += 1
            if retries > 10:
                self.skipTest("couldn't allocate two consecutive fds")
            (first, second) = (second, os.dup(second))
    finally:
        os.close(second)
    os.closerange(first, first + 2)
    self.assertRaises(OSError, os.write, first, b'a')

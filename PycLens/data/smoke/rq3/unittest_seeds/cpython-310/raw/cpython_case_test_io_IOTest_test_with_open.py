# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_with_open

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for bufsize in (0, 100):
        f = None
        with self.open(os_helper.TESTFN, 'wb', bufsize) as f:
            f.write(b'xxx')
        self.assertEqual(f.closed, True)
        f = None
        try:
            with self.open(os_helper.TESTFN, 'wb', bufsize) as f:
                1 / 0
        except ZeroDivisionError:
            self.assertEqual(f.closed, True)
        else:
            self.fail("1/0 didn't raise an exception")

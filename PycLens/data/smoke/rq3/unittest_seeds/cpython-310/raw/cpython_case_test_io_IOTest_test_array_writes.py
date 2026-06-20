# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_array_writes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array('i', range(10))
    n = len(a.tobytes())

    def check(f):
        with f:
            self.assertEqual(f.write(a), n)
            f.writelines((a,))
    check(self.BytesIO())
    check(self.FileIO(os_helper.TESTFN, 'w'))
    check(self.BufferedWriter(self.MockRawIO()))
    check(self.BufferedRandom(self.MockRawIO()))
    check(self.BufferedRWPair(self.MockRawIO(), self.MockRawIO()))

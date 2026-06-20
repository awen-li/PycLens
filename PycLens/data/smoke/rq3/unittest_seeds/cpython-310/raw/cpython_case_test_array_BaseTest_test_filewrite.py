# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_filewrite

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, 2 * self.example)
    f = open(os_helper.TESTFN, 'wb')
    try:
        f.write(a)
        f.close()
        b = array.array(self.typecode)
        f = open(os_helper.TESTFN, 'rb')
        b.fromfile(f, len(self.example))
        self.assertEqual(b, array.array(self.typecode, self.example))
        self.assertNotEqual(a, b)
        b.fromfile(f, len(self.example))
        self.assertEqual(a, b)
        f.close()
    finally:
        if not f.closed:
            f.close()
        os_helper.unlink(os_helper.TESTFN)

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_tofromfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, 2 * self.example)
    self.assertRaises(TypeError, a.tofile)
    os_helper.unlink(os_helper.TESTFN)
    f = open(os_helper.TESTFN, 'wb')
    try:
        a.tofile(f)
        f.close()
        b = array.array(self.typecode)
        f = open(os_helper.TESTFN, 'rb')
        self.assertRaises(TypeError, b.fromfile)
        b.fromfile(f, len(self.example))
        self.assertEqual(b, array.array(self.typecode, self.example))
        self.assertNotEqual(a, b)
        self.assertRaises(EOFError, b.fromfile, f, len(self.example) + 1)
        self.assertEqual(a, b)
        f.close()
    finally:
        if not f.closed:
            f.close()
        os_helper.unlink(os_helper.TESTFN)

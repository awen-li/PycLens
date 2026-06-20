# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CTextIOWrapperTest_test_garbage_collection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings_helper.check_warnings(('', ResourceWarning)):
        rawio = io.FileIO(os_helper.TESTFN, 'wb')
        b = self.BufferedWriter(rawio)
        t = self.TextIOWrapper(b, encoding='ascii')
        t.write('456def')
        t.x = t
        wr = weakref.ref(t)
        del t
        support.gc_collect()
    self.assertIsNone(wr(), wr)
    with self.open(os_helper.TESTFN, 'rb') as f:
        self.assertEqual(f.read(), b'456def')

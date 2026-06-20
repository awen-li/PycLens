# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: MiscIOTest_test_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.open(os_helper.TESTFN, 'wb', buffering=0)
    self.assertEqual(f.mode, 'wb')
    f.close()
    with warnings_helper.check_warnings(('', DeprecationWarning)):
        f = self.open(os_helper.TESTFN, 'U', encoding='utf-8')
    self.assertEqual(f.name, os_helper.TESTFN)
    self.assertEqual(f.buffer.name, os_helper.TESTFN)
    self.assertEqual(f.buffer.raw.name, os_helper.TESTFN)
    self.assertEqual(f.mode, 'U')
    self.assertEqual(f.buffer.mode, 'rb')
    self.assertEqual(f.buffer.raw.mode, 'rb')
    f.close()
    f = self.open(os_helper.TESTFN, 'w+', encoding='utf-8')
    self.assertEqual(f.mode, 'w+')
    self.assertEqual(f.buffer.mode, 'rb+')
    self.assertEqual(f.buffer.raw.mode, 'rb+')
    g = self.open(f.fileno(), 'wb', closefd=False)
    self.assertEqual(g.mode, 'wb')
    self.assertEqual(g.raw.mode, 'wb')
    self.assertEqual(g.name, f.fileno())
    self.assertEqual(g.raw.name, f.fileno())
    f.close()
    g.close()

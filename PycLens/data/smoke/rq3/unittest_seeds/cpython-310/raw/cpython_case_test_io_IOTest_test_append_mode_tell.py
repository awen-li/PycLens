# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_append_mode_tell

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.open(os_helper.TESTFN, 'wb') as f:
        f.write(b'xxx')
    with self.open(os_helper.TESTFN, 'ab', buffering=0) as f:
        self.assertEqual(f.tell(), 3)
    with self.open(os_helper.TESTFN, 'ab') as f:
        self.assertEqual(f.tell(), 3)
    with self.open(os_helper.TESTFN, 'a', encoding='utf-8') as f:
        self.assertGreater(f.tell(), 0)

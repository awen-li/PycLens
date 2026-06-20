# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FileTests_test_replace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    TESTFN2 = os_helper.TESTFN + '.2'
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    self.addCleanup(os_helper.unlink, TESTFN2)
    create_file(os_helper.TESTFN, b'1')
    create_file(TESTFN2, b'2')
    os.replace(os_helper.TESTFN, TESTFN2)
    self.assertRaises(FileNotFoundError, os.stat, os_helper.TESTFN)
    with open(TESTFN2, 'r', encoding='utf-8') as f:
        self.assertEqual(f.read(), '1')

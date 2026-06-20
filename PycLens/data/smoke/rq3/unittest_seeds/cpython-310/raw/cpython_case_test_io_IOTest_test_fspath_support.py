# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_fspath_support

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check_path_succeeds(path):
        with self.open(path, 'w', encoding='utf-8') as f:
            f.write('egg\n')
        with self.open(path, 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), 'egg\n')
    check_path_succeeds(FakePath(os_helper.TESTFN))
    check_path_succeeds(FakePath(os.fsencode(os_helper.TESTFN)))
    with self.open(os_helper.TESTFN, 'w', encoding='utf-8') as f:
        bad_path = FakePath(f.fileno())
        with self.assertRaises(TypeError):
            self.open(bad_path, 'w', encoding='utf-8')
    bad_path = FakePath(None)
    with self.assertRaises(TypeError):
        self.open(bad_path, 'w', encoding='utf-8')
    bad_path = FakePath(FloatingPointError)
    with self.assertRaises(FloatingPointError):
        self.open(bad_path, 'w', encoding='utf-8')
    with self.assertRaisesRegex(ValueError, 'read/write/append mode'):
        self.open(FakePath(os_helper.TESTFN), 'rwxa', encoding='utf-8')

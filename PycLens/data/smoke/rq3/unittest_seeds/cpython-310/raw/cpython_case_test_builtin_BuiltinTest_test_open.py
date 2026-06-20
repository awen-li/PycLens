# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_open

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_testfile()
    fp = open(TESTFN, encoding='utf-8')
    with fp:
        self.assertEqual(fp.readline(4), '1+1\n')
        self.assertEqual(fp.readline(), 'The quick brown fox jumps over the lazy dog.\n')
        self.assertEqual(fp.readline(4), 'Dear')
        self.assertEqual(fp.readline(100), ' John\n')
        self.assertEqual(fp.read(300), 'XXX' * 100)
        self.assertEqual(fp.read(1000), 'YYY' * 100)
    self.assertRaises(ValueError, open, 'a\x00b')
    self.assertRaises(ValueError, open, b'a\x00b')

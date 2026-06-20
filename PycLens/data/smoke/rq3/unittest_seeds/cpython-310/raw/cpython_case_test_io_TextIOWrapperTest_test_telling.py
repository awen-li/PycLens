# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_telling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.open(os_helper.TESTFN, 'w+', encoding='utf-8')
    p0 = f.tell()
    f.write('ÿ\n')
    p1 = f.tell()
    f.write('ÿ\n')
    p2 = f.tell()
    f.seek(0)
    self.assertEqual(f.tell(), p0)
    self.assertEqual(f.readline(), 'ÿ\n')
    self.assertEqual(f.tell(), p1)
    self.assertEqual(f.readline(), 'ÿ\n')
    self.assertEqual(f.tell(), p2)
    f.seek(0)
    for line in f:
        self.assertEqual(line, 'ÿ\n')
        self.assertRaises(OSError, f.tell)
    self.assertEqual(f.tell(), p2)
    f.close()

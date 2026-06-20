# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_fileno

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t1 = self.writeTmp('A\nB')
    t2 = self.writeTmp('C\nD')
    fi = FileInput(files=(t1, t2), encoding='utf-8')
    self.assertEqual(fi.fileno(), -1)
    line = next(fi)
    self.assertNotEqual(fi.fileno(), -1)
    fi.nextfile()
    self.assertEqual(fi.fileno(), -1)
    line = list(fi)
    self.assertEqual(fi.fileno(), -1)

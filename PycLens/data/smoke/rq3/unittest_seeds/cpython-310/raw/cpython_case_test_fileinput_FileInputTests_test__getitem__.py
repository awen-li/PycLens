# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test__getitem__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = self.writeTmp('line1\nline2\n')
    with FileInput(files=[t], encoding='utf-8') as fi:
        retval1 = fi[0]
        self.assertEqual(retval1, 'line1\n')
        retval2 = fi[1]
        self.assertEqual(retval2, 'line2\n')

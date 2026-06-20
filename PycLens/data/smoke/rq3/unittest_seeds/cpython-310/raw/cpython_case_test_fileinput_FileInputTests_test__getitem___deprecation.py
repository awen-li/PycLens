# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test__getitem___deprecation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = self.writeTmp('line1\nline2\n')
    with self.assertWarnsRegex(DeprecationWarning, 'Use iterator protocol instead'):
        with FileInput(files=[t]) as fi:
            self.assertEqual(fi[0], 'line1\n')

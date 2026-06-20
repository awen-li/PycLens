# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: FormatTestCase_test_format_testfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(format_testfile, encoding='utf-8') as testfile:
        for line in testfile:
            if line.startswith('--'):
                continue
            line = line.strip()
            if not line:
                continue
            (lhs, rhs) = map(str.strip, line.split('->'))
            (fmt, arg) = lhs.split()
            self.assertEqual(fmt % float(arg), rhs)
            self.assertEqual(fmt % -float(arg), '-' + rhs)

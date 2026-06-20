# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_issue17998

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for reps in ('*', '+', '?', '{1}'):
        for mod in ('', '?'):
            pattern = '.' + reps + mod + 'yz'
            self.assertEqual(re.compile(pattern, re.S).findall('xyz'), ['xyz'], msg=pattern)
            pattern = pattern.encode()
            self.assertEqual(re.compile(pattern, re.S).findall(b'xyz'), [b'xyz'], msg=pattern)

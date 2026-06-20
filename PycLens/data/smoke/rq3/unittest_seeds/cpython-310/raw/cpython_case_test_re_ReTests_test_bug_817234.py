# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_bug_817234

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    iter = re.finditer('.*', 'asdf')
    self.assertEqual(next(iter).span(), (0, 4))
    self.assertEqual(next(iter).span(), (4, 4))
    self.assertRaises(StopIteration, next, iter)

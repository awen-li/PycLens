# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_anyall

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.match('a.b', 'a\nb', re.DOTALL).group(0), 'a\nb')
    self.assertEqual(re.match('a.*b', 'a\n\nb', re.DOTALL).group(0), 'a\n\nb')

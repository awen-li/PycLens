# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ExternalTests_test_re_benchmarks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from test.re_tests import benchmarks
    for (pattern, s) in benchmarks:
        with self.subTest(pattern=pattern, string=s):
            p = re.compile(pattern)
            self.assertTrue(p.search(s))
            self.assertTrue(p.match(s))
            self.assertTrue(p.fullmatch(s))
            s2 = ' ' * 10000 + s + ' ' * 10000
            self.assertTrue(p.search(s2))
            self.assertTrue(p.match(s2, 10000))
            self.assertTrue(p.match(s2, 10000, 10000 + len(s)))
            self.assertTrue(p.fullmatch(s2, 10000, 10000 + len(s)))

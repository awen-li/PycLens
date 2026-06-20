# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: TimeRETests_test_matching_with_escapes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    compiled_re = self.time_re.compile('\\w+ %m')
    found = compiled_re.match('\\w+ 10')
    self.assertTrue(found, "Escaping failed of format '\\w+ 10'")

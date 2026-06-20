# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_unicode_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = Template('$who likes $what')
    d = dict(who='tÿm', what='fþ\x0ced')
    self.assertEqual(s.substitute(d), 'tÿm likes fþ\x0ced')

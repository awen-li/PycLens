# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_SafeTemplate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    s = Template('$who likes ${what} for ${meal}')
    eq(s.safe_substitute(dict(who='tim')), 'tim likes ${what} for ${meal}')
    eq(s.safe_substitute(dict(what='ham')), '$who likes ham for ${meal}')
    eq(s.safe_substitute(dict(what='ham', meal='dinner')), '$who likes ham for dinner')
    eq(s.safe_substitute(dict(who='tim', what='ham')), 'tim likes ham for ${meal}')
    eq(s.safe_substitute(dict(who='tim', what='ham', meal='dinner')), 'tim likes ham for dinner')

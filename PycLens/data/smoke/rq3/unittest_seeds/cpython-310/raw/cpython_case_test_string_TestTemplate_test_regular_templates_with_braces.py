# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_regular_templates_with_braces

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = Template('$who likes ${what} for ${meal}')
    d = dict(who='tim', what='ham', meal='dinner')
    self.assertEqual(s.substitute(d), 'tim likes ham for dinner')
    self.assertRaises(KeyError, s.substitute, dict(who='tim', what='ham'))

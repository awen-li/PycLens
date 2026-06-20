# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_regular_templates_with_upper_case

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = Template('$WHO likes ${WHAT} for ${MEAL}')
    d = dict(WHO='tim', WHAT='ham', MEAL='dinner')
    self.assertEqual(s.substitute(d), 'tim likes ham for dinner')

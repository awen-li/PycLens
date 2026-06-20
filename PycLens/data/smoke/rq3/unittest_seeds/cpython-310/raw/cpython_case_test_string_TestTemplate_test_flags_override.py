# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_flags_override

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyPattern(Template):
        flags = 0
    s = MyPattern('$wHO likes ${WHAT} for ${meal}')
    d = dict(wHO='tim', WHAT='ham', meal='dinner', w='fred')
    self.assertRaises(ValueError, s.substitute, d)
    self.assertEqual(s.safe_substitute(d), 'fredHO likes ${WHAT} for dinner')

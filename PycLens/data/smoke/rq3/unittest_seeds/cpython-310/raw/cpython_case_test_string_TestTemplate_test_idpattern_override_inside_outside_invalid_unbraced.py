# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_idpattern_override_inside_outside_invalid_unbraced

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyPattern(Template):
        idpattern = '[a-z]+'
        braceidpattern = '[A-Z]+'
        flags = 0
    m = dict(foo='foo', BAR='BAR')
    s = MyPattern('$FOO')
    self.assertRaises(ValueError, s.substitute, m)
    s = MyPattern('${bar}')
    self.assertRaises(ValueError, s.substitute, m)

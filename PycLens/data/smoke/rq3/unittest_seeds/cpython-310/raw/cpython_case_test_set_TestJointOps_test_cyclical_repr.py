# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestJointOps_test_cyclical_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    w = ReprWrapper()
    s = self.thetype([w])
    w.value = s
    if self.thetype == set:
        self.assertEqual(repr(s), '{set(...)}')
    else:
        name = repr(s).partition('(')[0]
        self.assertEqual(repr(s), '%s({%s(...)})' % (name, name))

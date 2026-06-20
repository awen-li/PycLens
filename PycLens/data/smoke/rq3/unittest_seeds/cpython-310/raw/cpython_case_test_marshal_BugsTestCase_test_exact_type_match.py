# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: BugsTestCase_test_exact_type_match

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for typ in (int, float, complex, tuple, list, dict, set, frozenset):
        subtyp = type('subtyp', (typ,), {})
        self.assertRaises(ValueError, marshal.dumps, subtyp())

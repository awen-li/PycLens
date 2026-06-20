# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_simple_namespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = types.SimpleNamespace(the=0, quick=1, brown=2, fox=3, jumped=4, over=5, a=6, lazy=7, dog=8)
    formatted = pprint.pformat(ns, width=60, indent=4)
    self.assertEqual(formatted, 'namespace(the=0,\n          quick=1,\n          brown=2,\n          fox=3,\n          jumped=4,\n          over=5,\n          a=6,\n          lazy=7,\n          dog=8)')

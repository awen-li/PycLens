# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_recursive_dataclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dc = dataclass4(None)
    dc.a = dc
    formatted = pprint.pformat(dc, width=10)
    self.assertEqual(formatted, 'dataclass4(a=...,\n           b=1)')

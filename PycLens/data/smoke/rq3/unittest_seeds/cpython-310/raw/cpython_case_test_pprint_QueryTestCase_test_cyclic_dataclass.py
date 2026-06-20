# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_cyclic_dataclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dc5 = dataclass5(None)
    dc6 = dataclass6(None)
    dc5.a = dc6
    dc6.c = dc5
    formatted = pprint.pformat(dc5, width=10)
    self.assertEqual(formatted, 'dataclass5(a=dataclass6(c=...,\n                        d=1),\n           b=1)')

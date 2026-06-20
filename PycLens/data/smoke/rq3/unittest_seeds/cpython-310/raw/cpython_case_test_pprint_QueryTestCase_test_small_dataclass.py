# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_small_dataclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dc = dataclass1('text', 123)
    formatted = pprint.pformat(dc)
    self.assertEqual(formatted, "dataclass1(field1='text', field2=123, field3=False)")

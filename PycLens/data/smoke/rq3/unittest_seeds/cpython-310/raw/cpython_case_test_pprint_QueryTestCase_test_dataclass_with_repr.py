# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_dataclass_with_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dc = dataclass2()
    formatted = pprint.pformat(dc, width=20)
    self.assertEqual(formatted, "custom repr that doesn't fit within pprint width")

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_dataclass_no_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dc = dataclass3()
    formatted = pprint.pformat(dc, width=10)
    self.assertRegex(formatted, '<test.test_pprint.dataclass3 object at \\w+>')

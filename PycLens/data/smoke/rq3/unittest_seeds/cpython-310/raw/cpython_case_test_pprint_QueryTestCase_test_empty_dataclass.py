# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_empty_dataclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dc = dataclasses.make_dataclass('MyDataclass', ())()
    formatted = pprint.pformat(dc)
    self.assertEqual(formatted, 'MyDataclass()')

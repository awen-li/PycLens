# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_larger_dataclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dc = dataclass1('some fairly long text', int(10000000000.0), True)
    formatted = pprint.pformat([dc, dc], width=60, indent=4)
    self.assertEqual(formatted, "[   dataclass1(field1='some fairly long text',\n               field2=10000000000,\n               field3=True),\n    dataclass1(field1='some fairly long text',\n               field2=10000000000,\n               field3=True)]")

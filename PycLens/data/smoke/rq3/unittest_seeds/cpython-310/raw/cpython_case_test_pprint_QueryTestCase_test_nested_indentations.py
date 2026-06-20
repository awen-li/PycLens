# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_nested_indentations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o1 = list(range(10))
    o2 = dict(first=1, second=2, third=3)
    o = [o1, o2]
    expected = "[   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],\n    {'first': 1, 'second': 2, 'third': 3}]"
    self.assertEqual(pprint.pformat(o, indent=4, width=42), expected)
    expected = "[   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],\n    {   'first': 1,\n        'second': 2,\n        'third': 3}]"
    self.assertEqual(pprint.pformat(o, indent=4, width=41), expected)

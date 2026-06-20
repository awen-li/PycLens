# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_set_reprs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(pprint.pformat(set()), 'set()')
    self.assertEqual(pprint.pformat(set(range(3))), '{0, 1, 2}')
    self.assertEqual(pprint.pformat(set(range(7)), width=20), '{0,\n 1,\n 2,\n 3,\n 4,\n 5,\n 6}')
    self.assertEqual(pprint.pformat(set2(range(7)), width=20), 'set2({0,\n      1,\n      2,\n      3,\n      4,\n      5,\n      6})')
    self.assertEqual(pprint.pformat(set3(range(7)), width=20), 'set3({0, 1, 2, 3, 4, 5, 6})')
    self.assertEqual(pprint.pformat(frozenset()), 'frozenset()')
    self.assertEqual(pprint.pformat(frozenset(range(3))), 'frozenset({0, 1, 2})')
    self.assertEqual(pprint.pformat(frozenset(range(7)), width=20), 'frozenset({0,\n           1,\n           2,\n           3,\n           4,\n           5,\n           6})')
    self.assertEqual(pprint.pformat(frozenset2(range(7)), width=20), 'frozenset2({0,\n            1,\n            2,\n            3,\n            4,\n            5,\n            6})')
    self.assertEqual(pprint.pformat(frozenset3(range(7)), width=20), 'frozenset3({0, 1, 2, 3, 4, 5, 6})')

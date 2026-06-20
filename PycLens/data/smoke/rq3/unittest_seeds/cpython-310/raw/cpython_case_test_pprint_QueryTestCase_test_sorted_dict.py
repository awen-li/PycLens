# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_sorted_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {'a': 1, 'b': 1, 'c': 1}
    self.assertEqual(pprint.pformat(d), "{'a': 1, 'b': 1, 'c': 1}")
    self.assertEqual(pprint.pformat([d, d]), "[{'a': 1, 'b': 1, 'c': 1}, {'a': 1, 'b': 1, 'c': 1}]")
    self.assertEqual(pprint.pformat({'xy\tab\n': (3,), 5: [[]], (): {}}), "{5: [[]], 'xy\\tab\\n': (3,), (): {}}")

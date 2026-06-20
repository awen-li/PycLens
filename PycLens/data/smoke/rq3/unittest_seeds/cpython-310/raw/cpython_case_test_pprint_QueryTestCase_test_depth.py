# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_depth

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nested_tuple = (1, (2, (3, (4, (5, 6)))))
    nested_dict = {1: {2: {3: {4: {5: {6: 6}}}}}}
    nested_list = [1, [2, [3, [4, [5, [6, []]]]]]]
    self.assertEqual(pprint.pformat(nested_tuple), repr(nested_tuple))
    self.assertEqual(pprint.pformat(nested_dict), repr(nested_dict))
    self.assertEqual(pprint.pformat(nested_list), repr(nested_list))
    lv1_tuple = '(1, (...))'
    lv1_dict = '{1: {...}}'
    lv1_list = '[1, [...]]'
    self.assertEqual(pprint.pformat(nested_tuple, depth=1), lv1_tuple)
    self.assertEqual(pprint.pformat(nested_dict, depth=1), lv1_dict)
    self.assertEqual(pprint.pformat(nested_list, depth=1), lv1_list)

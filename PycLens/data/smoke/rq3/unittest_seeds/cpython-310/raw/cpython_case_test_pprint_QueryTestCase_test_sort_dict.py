# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_sort_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = dict.fromkeys('cba')
    self.assertEqual(pprint.pformat(d, sort_dicts=False), "{'c': None, 'b': None, 'a': None}")
    self.assertEqual(pprint.pformat([d, d], sort_dicts=False), "[{'c': None, 'b': None, 'a': None}, {'c': None, 'b': None, 'a': None}]")

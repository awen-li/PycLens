# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_dictview_mixed_set_operations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue({1: 1}.keys() == {1})
    self.assertTrue({1} == {1: 1}.keys())
    self.assertEqual({1: 1}.keys() | {2}, {1, 2})
    self.assertEqual({2} | {1: 1}.keys(), {1, 2})
    self.assertTrue({1: 1}.items() == {(1, 1)})
    self.assertTrue({(1, 1)} == {1: 1}.items())
    self.assertEqual({1: 1}.items() | {2}, {(1, 1), 2})
    self.assertEqual({2} | {1: 1}.items(), {(1, 1), 2})

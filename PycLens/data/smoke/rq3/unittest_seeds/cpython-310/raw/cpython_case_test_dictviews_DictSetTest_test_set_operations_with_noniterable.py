# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictviews.py
# case: DictSetTest_test_set_operations_with_noniterable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        {}.keys() & 1
    with self.assertRaises(TypeError):
        {}.keys() | 1
    with self.assertRaises(TypeError):
        {}.keys() ^ 1
    with self.assertRaises(TypeError):
        {}.keys() - 1
    with self.assertRaises(TypeError):
        {}.items() & 1
    with self.assertRaises(TypeError):
        {}.items() | 1
    with self.assertRaises(TypeError):
        {}.items() ^ 1
    with self.assertRaises(TypeError):
        {}.items() - 1

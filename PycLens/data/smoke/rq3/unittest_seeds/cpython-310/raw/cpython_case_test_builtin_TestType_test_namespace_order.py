# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: TestType_test_namespace_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    od = collections.OrderedDict([('a', 1), ('b', 2)])
    od.move_to_end('a')
    expected = list(od.items())
    C = type('C', (), od)
    self.assertEqual(list(C.__dict__.items())[:2], [('b', 2), ('a', 1)])

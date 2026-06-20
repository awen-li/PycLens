# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_iter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, iter)
    self.assertRaises(TypeError, iter, 42, 42)
    lists = [('1', '2'), ['1', '2'], '12']
    for l in lists:
        i = iter(l)
        self.assertEqual(next(i), '1')
        self.assertEqual(next(i), '2')
        self.assertRaises(StopIteration, next, i)

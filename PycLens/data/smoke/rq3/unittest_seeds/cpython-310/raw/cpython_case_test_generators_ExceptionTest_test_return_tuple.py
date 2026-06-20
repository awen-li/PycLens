# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: ExceptionTest_test_return_tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def g():
        return (yield 1)
    gen = g()
    self.assertEqual(next(gen), 1)
    with self.assertRaises(StopIteration) as cm:
        gen.send((2,))
    self.assertEqual(cm.exception.value, (2,))

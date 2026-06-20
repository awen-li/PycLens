# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_matmul

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    self.assertRaises(TypeError, operator.matmul)
    self.assertRaises(TypeError, operator.matmul, 42, 42)

    class M:

        def __matmul__(self, other):
            return other - 1
    self.assertEqual(M() @ 42, 41)

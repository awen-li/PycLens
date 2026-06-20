# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_concat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    self.assertRaises(TypeError, operator.concat)
    self.assertRaises(TypeError, operator.concat, None, None)
    self.assertEqual(operator.concat('py', 'thon'), 'python')
    self.assertEqual(operator.concat([1, 2], [3, 4]), [1, 2, 3, 4])
    self.assertEqual(operator.concat(Seq1([5, 6]), Seq1([7])), [5, 6, 7])
    self.assertEqual(operator.concat(Seq2([5, 6]), Seq2([7])), [5, 6, 7])
    self.assertRaises(TypeError, operator.concat, 13, 29)

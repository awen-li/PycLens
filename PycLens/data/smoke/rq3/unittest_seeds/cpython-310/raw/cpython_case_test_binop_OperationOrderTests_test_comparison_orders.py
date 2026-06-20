# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binop.py
# case: OperationOrderTests_test_comparison_orders

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(op_sequence(eq, A, A), ['A.__eq__', 'A.__eq__'])
    self.assertEqual(op_sequence(eq, A, B), ['A.__eq__', 'B.__eq__'])
    self.assertEqual(op_sequence(eq, B, A), ['B.__eq__', 'A.__eq__'])
    self.assertEqual(op_sequence(eq, B, C), ['C.__eq__', 'B.__eq__'])
    self.assertEqual(op_sequence(eq, C, B), ['C.__eq__', 'B.__eq__'])
    self.assertEqual(op_sequence(le, A, A), ['A.__le__', 'A.__ge__'])
    self.assertEqual(op_sequence(le, A, B), ['A.__le__', 'B.__ge__'])
    self.assertEqual(op_sequence(le, B, A), ['B.__le__', 'A.__ge__'])
    self.assertEqual(op_sequence(le, B, C), ['C.__ge__', 'B.__le__'])
    self.assertEqual(op_sequence(le, C, B), ['C.__le__', 'B.__ge__'])
    self.assertTrue(issubclass(V, B))
    self.assertEqual(op_sequence(eq, B, V), ['B.__eq__', 'V.__eq__'])
    self.assertEqual(op_sequence(le, B, V), ['B.__le__', 'V.__ge__'])

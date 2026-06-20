# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionAssignmentTest_test_named_expression_assignment_17

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = [1]
    element = a[(b := 0)]
    self.assertEqual(b, 0)
    self.assertEqual(element, a[0])

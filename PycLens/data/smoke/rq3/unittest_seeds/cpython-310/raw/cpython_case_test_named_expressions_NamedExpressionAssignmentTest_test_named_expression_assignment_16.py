# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionAssignmentTest_test_named_expression_assignment_16

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (a, b) = (1, 2)
    fib = {(c := a): (a := b) + (b := (a + c)) - b for __ in range(6)}
    self.assertEqual(fib, {1: 2, 2: 3, 3: 5, 5: 8, 8: 13, 13: 21})

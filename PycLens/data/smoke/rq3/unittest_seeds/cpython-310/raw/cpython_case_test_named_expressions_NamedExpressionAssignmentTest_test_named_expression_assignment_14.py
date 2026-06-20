# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionAssignmentTest_test_named_expression_assignment_14

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = 9
    n = 2
    x = 3
    while a > (d := (x // a ** (n - 1))):
        a = ((n - 1) * a + d) // n
    self.assertEqual(a, 1)

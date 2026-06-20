# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionAssignmentTest_test_named_expression_assignment_12

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def spam(a):
        return a
    res = [[(y := spam(x)), x / y] for x in range(1, 5)]
    self.assertEqual(res, [[1, 1.0], [2, 1.0], [3, 1.0], [4, 1.0]])

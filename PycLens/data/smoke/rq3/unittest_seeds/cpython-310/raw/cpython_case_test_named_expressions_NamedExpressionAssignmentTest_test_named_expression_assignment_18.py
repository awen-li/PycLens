# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionAssignmentTest_test_named_expression_assignment_18

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TwoDimensionalList:

        def __init__(self, two_dimensional_list):
            self.two_dimensional_list = two_dimensional_list

        def __getitem__(self, index):
            return self.two_dimensional_list[index[0]][index[1]]
    a = TwoDimensionalList([[1], [2]])
    element = a[(b := 0), (c := 0)]
    self.assertEqual(b, 0)
    self.assertEqual(c, 0)
    self.assertEqual(element, a.two_dimensional_list[b][c])

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionAssignmentTest_test_named_expression_assignment_09

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if True and (spam := True):
        self.assertTrue(spam)
    else:
        self.fail('variable was not assigned using named expression')

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionInvalidTest_test_named_expression_invalid_rebinding_set_comprehension_iteration_variable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cases = [('Local reuse', 'i', '{i := 0 for i in range(5)}'), ('Nested reuse', 'j', '{{(j := 0) for i in range(5)} for j in range(5)}'), ('Reuse inner loop target', 'j', '{(j := 0) for i in range(5) for j in range(5)}'), ('Unpacking reuse', 'i', '{i := 0 for i, j in {(0, 1)}}'), ('Reuse in loop condition', 'i', '{i+1 for i in range(5) if (i := 0)}'), ('Unreachable reuse', 'i', '{False or (i:=0) for i in range(5)}'), ('Unreachable nested reuse', 'i', '{(i, j) for i in range(5) for j in range(5) if True or (i:=10)}')]
    for (case, target, code) in cases:
        msg = f"assignment expression cannot rebind comprehension iteration variable '{target}'"
        with self.subTest(case=case):
            with self.assertRaisesRegex(SyntaxError, msg):
                exec(code, {}, {})

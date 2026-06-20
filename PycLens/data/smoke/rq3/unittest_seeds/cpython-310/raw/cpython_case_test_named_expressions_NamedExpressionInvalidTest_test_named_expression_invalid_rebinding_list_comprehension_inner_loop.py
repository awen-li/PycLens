# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionInvalidTest_test_named_expression_invalid_rebinding_list_comprehension_inner_loop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cases = [('Inner reuse', 'j', '[i for i in range(5) if (j := 0) for j in range(5)]'), ('Inner unpacking reuse', 'j', '[i for i in range(5) if (j := 0) for j, k in [(0, 1)]]')]
    for (case, target, code) in cases:
        msg = f"comprehension inner loop cannot rebind assignment expression target '{target}'"
        with self.subTest(case=case):
            with self.assertRaisesRegex(SyntaxError, msg):
                exec(code, {})
            with self.assertRaisesRegex(SyntaxError, msg):
                exec(code, {}, {})
            with self.assertRaisesRegex(SyntaxError, msg):
                exec(f'lambda: {code}', {})

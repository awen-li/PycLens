# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionInvalidTest_test_named_expression_invalid_set_comprehension_iterable_expression

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cases = [('Top level', '{i for i in (i := range(5))}'), ('Inside tuple', '{i for i in (2, 3, i := range(5))}'), ('Inside list', '{i for i in {2, 3, i := range(5)}}'), ('Different name', '{i for i in (j := range(5))}'), ('Lambda expression', '{i for i in (lambda:(j := range(5)))()}'), ('Inner loop', '{i for i in range(5) for j in (i := range(5))}'), ('Nested comprehension', '{i for i in {j for j in (k := range(5))}}'), ('Nested comprehension condition', '{i for i in {j for j in range(5) if (j := True)}}'), ('Nested comprehension body', '{i for i in {(j := True) for j in range(5)}}')]
    msg = 'assignment expression cannot be used in a comprehension iterable expression'
    for (case, code) in cases:
        with self.subTest(case=case):
            with self.assertRaisesRegex(SyntaxError, msg):
                exec(code, {})
            with self.assertRaisesRegex(SyntaxError, msg):
                exec(code, {}, {})
            with self.assertRaisesRegex(SyntaxError, msg):
                exec(f'lambda: {code}', {})

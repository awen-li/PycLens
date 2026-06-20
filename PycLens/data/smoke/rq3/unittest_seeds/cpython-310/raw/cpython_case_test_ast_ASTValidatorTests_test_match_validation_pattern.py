# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_match_validation_pattern

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name_x = ast.Name('x', ast.Load())
    for pattern in self._MATCH_PATTERNS:
        with self.subTest(ast.dump(pattern, indent=4)):
            node = ast.Match(subject=name_x, cases=[ast.match_case(pattern=pattern, body=[ast.Pass()])])
            node = ast.fix_missing_locations(node)
            module = ast.Module([node], [])
            with self.assertRaises(ValueError):
                compile(module, '<test>', 'exec')

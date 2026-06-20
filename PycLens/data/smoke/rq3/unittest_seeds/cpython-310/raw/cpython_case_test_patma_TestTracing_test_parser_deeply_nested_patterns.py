# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestTracing_test_parser_deeply_nested_patterns

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    levels = 100
    patterns = ['A' + '(' * levels + ')' * levels, '{1:' * levels + '1' + '}' * levels, '[' * levels + '1' + ']' * levels]
    for pattern in patterns:
        with self.subTest(pattern):
            code = inspect.cleandoc('\n                    match None:\n                        case {}:\n                            pass\n                '.format(pattern))
            compile(code, '<string>', 'exec')

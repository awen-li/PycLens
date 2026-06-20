# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syntax.py
# case: SyntaxTestCase_test_error_on_parser_stack_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = '-' * 100000 + '4'
    for mode in ['exec', 'eval', 'single']:
        with self.subTest(mode=mode):
            with self.assertRaises(MemoryError):
                compile(source, '<string>', mode)

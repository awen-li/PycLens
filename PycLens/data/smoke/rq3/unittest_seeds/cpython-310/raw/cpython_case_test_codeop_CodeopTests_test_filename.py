# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeop.py
# case: CodeopTests_test_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(compile_command('a = 1\n', 'abc').co_filename, compile('a = 1\n', 'abc', 'single').co_filename)
    self.assertNotEqual(compile_command('a = 1\n', 'abc').co_filename, compile('a = 1\n', 'def', 'single').co_filename)

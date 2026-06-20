# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: TokenTests_test_eof_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    samples = ('def foo(', '\ndef foo(', 'def foo(\n')
    for s in samples:
        with self.assertRaises(SyntaxError) as cm:
            compile(s, '<test>', 'exec')
        self.assertIn('was never closed', str(cm.exception))

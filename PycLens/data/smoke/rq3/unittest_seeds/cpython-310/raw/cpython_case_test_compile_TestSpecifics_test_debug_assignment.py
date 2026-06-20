# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_debug_assignment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(SyntaxError, compile, '__debug__ = 1', '?', 'single')
    import builtins
    prev = builtins.__debug__
    setattr(builtins, '__debug__', 'sure')
    self.assertEqual(__debug__, prev)
    setattr(builtins, '__debug__', prev)

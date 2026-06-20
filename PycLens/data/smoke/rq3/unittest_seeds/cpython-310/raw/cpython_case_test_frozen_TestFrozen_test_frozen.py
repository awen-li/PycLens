# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_frozen.py
# case: TestFrozen_test_frozen

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name = '__hello__'
    if name in sys.modules:
        del sys.modules[name]
    with captured_stdout() as out:
        import __hello__
    self.assertEqual(out.getvalue(), 'Hello world!\n')

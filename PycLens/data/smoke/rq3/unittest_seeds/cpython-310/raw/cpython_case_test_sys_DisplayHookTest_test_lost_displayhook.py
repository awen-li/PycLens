# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: DisplayHookTest_test_lost_displayhook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    displayhook = sys.displayhook
    try:
        del sys.displayhook
        code = compile('42', '<string>', 'single')
        self.assertRaises(RuntimeError, eval, code)
    finally:
        sys.displayhook = displayhook

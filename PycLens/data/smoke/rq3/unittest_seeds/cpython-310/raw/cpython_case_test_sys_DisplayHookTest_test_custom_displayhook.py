# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: DisplayHookTest_test_custom_displayhook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def baddisplayhook(obj):
        raise ValueError
    with support.swap_attr(sys, 'displayhook', baddisplayhook):
        code = compile('42', '<string>', 'single')
        self.assertRaises(ValueError, eval, code)

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winsound.py
# case: MessageBeepTest_test_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, winsound.MessageBeep, 'bad')
    self.assertRaises(TypeError, winsound.MessageBeep, 42, 42)
    safe_MessageBeep()

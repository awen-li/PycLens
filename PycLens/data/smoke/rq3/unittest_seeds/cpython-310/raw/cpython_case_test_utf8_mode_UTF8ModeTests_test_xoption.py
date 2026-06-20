# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_utf8_mode.py
# case: UTF8ModeTests_test_xoption

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import sys; print(sys.flags.utf8_mode)'
    out = self.get_output('-X', 'utf8', '-c', code)
    self.assertEqual(out, '1')
    out = self.get_output('-X', 'utf8=1', '-c', code)
    self.assertEqual(out, '1')
    out = self.get_output('-X', 'utf8=0', '-c', code)
    self.assertEqual(out, '0')
    if MS_WINDOWS:
        out = self.get_output('-X', 'utf8', '-c', code, PYTHONLEGACYWINDOWSFSENCODING='1')
        self.assertEqual(out, '0')

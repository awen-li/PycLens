# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_utf8_mode.py
# case: UTF8ModeTests_test_optim_level

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import sys; print(sys.flags.optimize)'
    out = self.get_output('-X', 'utf8', '-O', '-c', code)
    self.assertEqual(out, '1')
    out = self.get_output('-X', 'utf8', '-OO', '-c', code)
    self.assertEqual(out, '2')
    code = 'import sys; print(sys.flags.ignore_environment)'
    out = self.get_output('-X', 'utf8', '-E', '-c', code)
    self.assertEqual(out, '1')

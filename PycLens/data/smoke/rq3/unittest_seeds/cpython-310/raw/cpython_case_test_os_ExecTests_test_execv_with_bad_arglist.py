# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: ExecTests_test_execv_with_bad_arglist

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ValueError, os.execv, 'notepad', ())
    self.assertRaises(ValueError, os.execv, 'notepad', [])
    self.assertRaises(ValueError, os.execv, 'notepad', ('',))
    self.assertRaises(ValueError, os.execv, 'notepad', [''])

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: PidTests_test_waitstatus_to_exitcode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exitcode = 23
    code = f'import sys; sys.exit({exitcode})'
    self.check_waitpid(code, exitcode=exitcode)
    with self.assertRaises(TypeError):
        os.waitstatus_to_exitcode(0.0)

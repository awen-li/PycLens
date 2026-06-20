# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: Win32ProcessTestCase_test_issue31471

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BadEnv(dict):
        keys = None
    with self.assertRaises(TypeError):
        subprocess.Popen(ZERO_RETURN_CMD, env=BadEnv())

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_universal_newlines_communicate_input_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen(ZERO_RETURN_CMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    p.communicate()
    self.assertEqual(p.returncode, 0)

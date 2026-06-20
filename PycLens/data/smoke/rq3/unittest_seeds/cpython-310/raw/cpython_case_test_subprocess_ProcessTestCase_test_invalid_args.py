# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_invalid_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.captured_stderr() as s:
        self.assertRaises(TypeError, subprocess.Popen, invalid_arg_name=1)
        argcount = subprocess.Popen.__init__.__code__.co_argcount
        too_many_args = [0] * (argcount + 1)
        self.assertRaises(TypeError, subprocess.Popen, *too_many_args)
    self.assertEqual(s.getvalue(), '')

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_huntrleaks_fd_leak

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import os\n            import unittest\n\n            class FDLeakTest(unittest.TestCase):\n                def test_leak(self):\n                    fd = os.open(__file__, os.O_RDONLY)\n                    # bug: never close the file descriptor\n        ')
    self.check_leak(code, 'file descriptors')

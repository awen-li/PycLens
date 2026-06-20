# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_multiprocessing_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import time\n            import unittest\n            try:\n                import faulthandler\n            except ImportError:\n                faulthandler = None\n\n            class Tests(unittest.TestCase):\n                # test hangs and so should be stopped by the timeout\n                def test_sleep(self):\n                    # we want to test regrtest multiprocessing timeout,\n                    # not faulthandler timeout\n                    if faulthandler is not None:\n                        faulthandler.cancel_dump_traceback_later()\n\n                    time.sleep(60 * 5)\n        ')
    testname = self.create_test(code=code)
    output = self.run_tests('-j2', '--timeout=1.0', testname, exitcode=2)
    self.check_executed_tests(output, [testname], failed=testname)
    self.assertRegex(output, re.compile('%s timed out' % testname, re.MULTILINE))

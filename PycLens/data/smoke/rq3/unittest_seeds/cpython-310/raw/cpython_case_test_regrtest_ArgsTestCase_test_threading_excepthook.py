# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_threading_excepthook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import threading\n            import unittest\n            from test.support import captured_stderr\n\n            class MyObject:\n                pass\n\n            def func_bug():\n                raise Exception("bug in thread")\n\n            class Tests(unittest.TestCase):\n                def test_threading_excepthook(self):\n                    with captured_stderr() as stderr:\n                        thread = threading.Thread(target=func_bug)\n                        thread.start()\n                        thread.join()\n                    self.assertEqual(stderr.getvalue(), \'\')\n        ')
    testname = self.create_test(code=code)
    output = self.run_tests('--fail-env-changed', '-v', testname, exitcode=3)
    self.check_executed_tests(output, [testname], env_changed=[testname], fail_env_changed=True)
    self.assertIn('Warning -- Uncaught thread exception', output)
    self.assertIn('Exception: bug in thread', output)

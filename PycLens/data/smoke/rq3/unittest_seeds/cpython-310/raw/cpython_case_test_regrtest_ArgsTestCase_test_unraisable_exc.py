# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_unraisable_exc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import unittest\n            import weakref\n            from test.support import captured_stderr\n\n            class MyObject:\n                pass\n\n            def weakref_callback(obj):\n                raise Exception("weakref callback bug")\n\n            class Tests(unittest.TestCase):\n                def test_unraisable_exc(self):\n                    obj = MyObject()\n                    ref = weakref.ref(obj, weakref_callback)\n                    with captured_stderr() as stderr:\n                        # call weakref_callback() which logs\n                        # an unraisable exception\n                        obj = None\n                    self.assertEqual(stderr.getvalue(), \'\')\n        ')
    testname = self.create_test(code=code)
    output = self.run_tests('--fail-env-changed', '-v', testname, exitcode=3)
    self.check_executed_tests(output, [testname], env_changed=[testname], fail_env_changed=True)
    self.assertIn('Warning -- Unraisable exception', output)
    self.assertIn('Exception: weakref callback bug', output)

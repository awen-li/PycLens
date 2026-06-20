# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_atexit.py
# case: FunctionalTest_test_atexit_instances

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import sys\n            import atexit as atexit1\n            del sys.modules[\'atexit\']\n            import atexit as atexit2\n            del sys.modules[\'atexit\']\n\n            assert atexit2 is not atexit1\n\n            atexit1.register(print, "atexit1")\n            atexit2.register(print, "atexit2")\n        ')
    res = script_helper.assert_python_ok('-c', code)
    self.assertEqual(res.out.decode().splitlines(), ['atexit2', 'atexit1'])
    self.assertFalse(res.err)

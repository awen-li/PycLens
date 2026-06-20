# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_atexit.py
# case: FunctionalTest_test_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import atexit\n\n            def f(msg):\n                print(msg)\n\n            atexit.register(f, "one")\n            atexit.register(f, "two")\n        ')
    res = script_helper.assert_python_ok('-c', code)
    self.assertEqual(res.out.decode().splitlines(), ['two', 'one'])
    self.assertFalse(res.err)

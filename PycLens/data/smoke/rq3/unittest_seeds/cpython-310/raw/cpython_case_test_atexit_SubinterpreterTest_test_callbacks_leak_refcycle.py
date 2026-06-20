# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_atexit.py
# case: SubinterpreterTest_test_callbacks_leak_refcycle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    n = atexit._ncallbacks()
    code = textwrap.dedent('\n            import atexit\n            def f():\n                pass\n            atexit.register(f)\n            atexit.__atexit = atexit\n        ')
    ret = support.run_in_subinterp(code)
    self.assertEqual(ret, 0)
    self.assertEqual(atexit._ncallbacks(), n)

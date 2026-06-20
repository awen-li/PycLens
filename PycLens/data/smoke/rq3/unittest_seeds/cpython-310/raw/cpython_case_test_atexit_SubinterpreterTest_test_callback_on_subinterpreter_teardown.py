# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_atexit.py
# case: SubinterpreterTest_test_callback_on_subinterpreter_teardown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = b'The test has passed!'
    (r, w) = os.pipe()
    code = textwrap.dedent('\n            import os\n            import atexit\n            def callback():\n                os.write({:d}, b"The test has passed!")\n            atexit.register(callback)\n        '.format(w))
    ret = support.run_in_subinterp(code)
    os.close(w)
    self.assertEqual(os.read(r, len(expected)), expected)
    os.close(r)

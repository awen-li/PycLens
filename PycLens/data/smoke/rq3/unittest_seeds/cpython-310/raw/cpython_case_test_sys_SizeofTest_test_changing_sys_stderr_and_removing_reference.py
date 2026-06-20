# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SizeofTest_test_changing_sys_stderr_and_removing_reference

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import sys\n            class MyStderr:\n                def write(self, s):\n                    sys.stderr = None\n            sys.stderr = MyStderr()\n            1/0\n        ')
    (rc, out, err) = assert_python_failure('-c', code)
    self.assertEqual(out, b'')
    self.assertEqual(err, b'')

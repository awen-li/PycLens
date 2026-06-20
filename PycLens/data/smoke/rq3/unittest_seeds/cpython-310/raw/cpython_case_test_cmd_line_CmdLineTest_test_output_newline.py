# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_output_newline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n            import sys\n            print(1)\n            print(2)\n            print(3, file=sys.stderr)\n            print(4, file=sys.stderr)'
    (rc, out, err) = assert_python_ok('-c', code)
    if sys.platform == 'win32':
        self.assertEqual(b'1\r\n2\r\n', out)
        self.assertEqual(b'3\r\n4\r\n', err)
    else:
        self.assertEqual(b'1\n2\n', out)
        self.assertEqual(b'3\n4\n', err)

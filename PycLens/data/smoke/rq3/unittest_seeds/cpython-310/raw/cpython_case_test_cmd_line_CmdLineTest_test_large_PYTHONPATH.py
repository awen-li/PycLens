# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_large_PYTHONPATH

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path1 = 'ABCDE' * 100
    path2 = 'FGHIJ' * 100
    path = path1 + os.pathsep + path2
    code = 'if 1:\n            import sys\n            path = ":".join(sys.path)\n            path = path.encode("ascii", "backslashreplace")\n            sys.stdout.buffer.write(path)'
    (rc, out, err) = assert_python_ok('-S', '-c', code, PYTHONPATH=path)
    self.assertIn(path1.encode('ascii'), out)
    self.assertIn(path2.encode('ascii'), out)

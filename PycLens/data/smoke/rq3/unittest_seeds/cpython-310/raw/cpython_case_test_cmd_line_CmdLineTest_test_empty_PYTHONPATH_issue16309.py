# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_empty_PYTHONPATH_issue16309

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n            import sys\n            path = ":".join(sys.path)\n            path = path.encode("ascii", "backslashreplace")\n            sys.stdout.buffer.write(path)'
    (rc1, out1, err1) = assert_python_ok('-c', code, PYTHONPATH='')
    (rc2, out2, err2) = assert_python_ok('-c', code, __isolated=False)
    self.assertEqual(out1, out2)

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_unbuffered_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import sys; sys.stdout.write(sys.stdin.read(1))'
    p = spawn_python('-u', '-c', code)
    p.stdin.write(b'x')
    p.stdin.flush()
    (data, rc) = _kill_python_and_exit_code(p)
    self.assertEqual(rc, 0)
    self.assertTrue(data.startswith(b'x'), data)

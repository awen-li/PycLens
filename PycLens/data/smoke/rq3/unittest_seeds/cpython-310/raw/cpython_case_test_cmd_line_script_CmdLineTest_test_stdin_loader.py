# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_stdin_loader

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = spawn_python()
    try:
        p.stdin.write(b'print(__loader__)\n')
        p.stdin.flush()
    finally:
        out = kill_python(p)
    expected = repr(importlib.machinery.BuiltinImporter).encode('utf-8')
    self.assertIn(expected, out)

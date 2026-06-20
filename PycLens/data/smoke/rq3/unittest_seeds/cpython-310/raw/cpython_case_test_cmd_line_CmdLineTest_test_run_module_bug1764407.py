# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_run_module_bug1764407

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = spawn_python('-i', '-m', 'timeit', '-n', '1')
    p.stdin.write(b'Timer\n')
    p.stdin.write(b'exit()\n')
    data = kill_python(p)
    self.assertTrue(data.find(b'1 loop') != -1)
    self.assertTrue(data.find(b'__main__.Timer') != -1)

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_executable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(os.path.abspath(sys.executable), sys.executable)
    python_dir = os.path.dirname(os.path.realpath(sys.executable))
    p = subprocess.Popen(['nonexistent', '-c', 'import sys; print(sys.executable.encode("ascii", "backslashreplace"))'], executable=sys.executable, stdout=subprocess.PIPE, cwd=python_dir)
    stdout = p.communicate()[0]
    executable = stdout.strip().decode('ASCII')
    p.wait()
    self.assertIn(executable, ["b''", repr(sys.executable.encode('ascii', 'backslashreplace'))])

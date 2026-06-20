# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_argv0_normalization

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = (sys.executable, '-c', 'print(0)')
    (prefix, exe) = os.path.split(sys.executable)
    executable = prefix + '\\.\\.\\.\\' + exe
    proc = subprocess.run(args, stdout=subprocess.PIPE, executable=executable)
    self.assertEqual(proc.returncode, 0, proc)
    self.assertEqual(proc.stdout.strip(), b'0')

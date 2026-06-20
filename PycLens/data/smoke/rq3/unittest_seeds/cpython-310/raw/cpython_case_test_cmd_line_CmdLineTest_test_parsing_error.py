# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_parsing_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = [sys.executable, '-I', '--unknown-option']
    proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    err_msg = 'unknown option --unknown-option\nusage: '
    self.assertTrue(proc.stderr.startswith(err_msg), proc.stderr)
    self.assertNotEqual(proc.returncode, 0)

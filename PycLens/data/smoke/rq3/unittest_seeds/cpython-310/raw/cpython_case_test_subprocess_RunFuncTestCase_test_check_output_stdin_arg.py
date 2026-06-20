# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: RunFuncTestCase_test_check_output_stdin_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tf = tempfile.TemporaryFile()
    self.addCleanup(tf.close)
    tf.write(b'pear')
    tf.seek(0)
    cp = self.run_python('import sys; sys.stdout.write(sys.stdin.read().upper())', stdin=tf, stdout=subprocess.PIPE)
    self.assertIn(b'PEAR', cp.stdout)

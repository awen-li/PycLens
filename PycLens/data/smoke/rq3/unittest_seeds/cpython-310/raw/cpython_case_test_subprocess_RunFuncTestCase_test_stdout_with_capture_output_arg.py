# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: RunFuncTestCase_test_stdout_with_capture_output_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tf = tempfile.TemporaryFile()
    self.addCleanup(tf.close)
    with self.assertRaises(ValueError, msg='Expected ValueError when stdout and capture_output args supplied.') as c:
        output = self.run_python("print('will not be run')", capture_output=True, stdout=tf)
    self.assertIn('stdout', c.exception.args[0])
    self.assertIn('capture_output', c.exception.args[0])

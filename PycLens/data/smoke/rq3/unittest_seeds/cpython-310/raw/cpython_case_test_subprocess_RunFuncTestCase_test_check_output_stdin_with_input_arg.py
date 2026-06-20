# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: RunFuncTestCase_test_check_output_stdin_with_input_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tf = tempfile.TemporaryFile()
    self.addCleanup(tf.close)
    tf.write(b'pear')
    tf.seek(0)
    with self.assertRaises(ValueError, msg='Expected ValueError when stdin and input args supplied.') as c:
        output = self.run_python("print('will not be run')", stdin=tf, input=b'hare')
    self.assertIn('stdin', c.exception.args[0])
    self.assertIn('input', c.exception.args[0])

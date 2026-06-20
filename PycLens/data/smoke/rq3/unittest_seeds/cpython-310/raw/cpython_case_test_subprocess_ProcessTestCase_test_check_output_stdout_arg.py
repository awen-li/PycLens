# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_check_output_stdout_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError) as c:
        output = subprocess.check_output([sys.executable, '-c', "print('will not be run')"], stdout=sys.stdout)
        self.fail('Expected ValueError when stdout arg supplied.')
    self.assertIn('stdout', c.exception.args[0])

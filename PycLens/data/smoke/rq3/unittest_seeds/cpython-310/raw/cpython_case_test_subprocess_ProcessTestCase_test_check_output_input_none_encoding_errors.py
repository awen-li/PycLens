# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_check_output_input_none_encoding_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    output = subprocess.check_output([sys.executable, '-c', "print('foo')"], input=None, encoding='utf-8', errors='ignore')
    self.assertIn('foo', output)

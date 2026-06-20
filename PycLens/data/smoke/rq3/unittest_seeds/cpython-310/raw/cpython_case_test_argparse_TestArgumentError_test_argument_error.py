# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestArgumentError_test_argument_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = 'my error here'
    error = argparse.ArgumentError(None, msg)
    self.assertEqual(str(error), msg)

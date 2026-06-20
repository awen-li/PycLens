# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: PosixTests_test_interprocess_signal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dirname = os.path.dirname(__file__)
    script = os.path.join(dirname, 'signalinterproctester.py')
    assert_python_ok(script)

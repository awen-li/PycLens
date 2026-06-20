# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: IgnoreEnvironmentTest_test_ignore_PYTHONPATH

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = 'should_be_ignored'
    self.run_ignoring_vars("'{}' not in sys.path".format(path), PYTHONPATH=path)

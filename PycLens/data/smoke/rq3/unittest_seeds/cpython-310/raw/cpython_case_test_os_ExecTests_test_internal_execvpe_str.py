# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: ExecTests_test_internal_execvpe_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_internal_execvpe(str)
    if os.name != 'nt':
        self._test_internal_execvpe(bytes)

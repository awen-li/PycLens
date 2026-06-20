# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: AppendTest_test_trailing_garbage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = tarfile.TarInfo('foo').tobuf()
    self._test_error(data + b'\x00' * 13)

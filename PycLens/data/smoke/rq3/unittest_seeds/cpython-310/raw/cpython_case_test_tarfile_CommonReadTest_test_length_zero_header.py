# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CommonReadTest_test_length_zero_header

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(tarfile.ReadError, 'file could not be opened successfully'):
        with tarfile.open(support.findfile('recursion.tar')) as tar:
            pass

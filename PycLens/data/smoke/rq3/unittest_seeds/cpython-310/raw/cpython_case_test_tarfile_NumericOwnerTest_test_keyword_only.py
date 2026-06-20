# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: NumericOwnerTest_test_keyword_only

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self._setup_test(mock_geteuid) as (tarfl, filename_1, _, _):
        self.assertRaises(TypeError, tarfl.extract, filename_1, TEMPDIR, False, True)

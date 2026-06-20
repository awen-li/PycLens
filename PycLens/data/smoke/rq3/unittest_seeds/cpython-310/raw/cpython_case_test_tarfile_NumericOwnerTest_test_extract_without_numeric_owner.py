# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: NumericOwnerTest_test_extract_without_numeric_owner

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self._setup_test(mock_geteuid) as (tarfl, filename_1, _, _):
        tarfl.extract(filename_1, TEMPDIR, numeric_owner=False, filter='fully_trusted')
    f_filename_1 = os.path.join(TEMPDIR, filename_1)
    mock_chown.assert_called_with(f_filename_1, 0, 0)

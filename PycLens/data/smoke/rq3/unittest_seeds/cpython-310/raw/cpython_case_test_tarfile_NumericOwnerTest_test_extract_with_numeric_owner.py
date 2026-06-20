# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: NumericOwnerTest_test_extract_with_numeric_owner

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self._setup_test(mock_geteuid) as (tarfl, filename_1, _, filename_2):
        tarfl.extract(filename_1, TEMPDIR, numeric_owner=True, filter='fully_trusted')
        tarfl.extract(filename_2, TEMPDIR, numeric_owner=True, filter='fully_trusted')
    f_filename_1 = os.path.join(TEMPDIR, filename_1)
    f_filename_2 = os.path.join(TEMPDIR, filename_2)
    mock_chown.assert_has_calls([unittest.mock.call(f_filename_1, 99, 98), unittest.mock.call(f_filename_2, 88, 87)], any_order=True)

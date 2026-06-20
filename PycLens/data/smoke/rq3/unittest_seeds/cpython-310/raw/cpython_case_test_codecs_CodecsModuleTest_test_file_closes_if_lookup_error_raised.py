# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodecsModuleTest_test_file_closes_if_lookup_error_raised

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mock_open = mock.mock_open()
    with mock.patch('builtins.open', mock_open) as file:
        with self.assertRaises(LookupError):
            codecs.open(os_helper.TESTFN, 'wt', 'invalid-encoding')
        file().close.assert_called()

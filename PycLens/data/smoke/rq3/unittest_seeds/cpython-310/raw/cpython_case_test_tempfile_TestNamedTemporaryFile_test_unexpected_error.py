# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestNamedTemporaryFile_test_unexpected_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dir = tempfile.mkdtemp()
    self.addCleanup(os_helper.rmtree, dir)
    with mock.patch('tempfile._TemporaryFileWrapper') as mock_ntf, mock.patch('io.open', mock.mock_open()) as mock_open:
        mock_ntf.side_effect = KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):
            tempfile.NamedTemporaryFile(dir=dir)
    mock_open().close.assert_called()
    self.assertEqual(os.listdir(dir), [])

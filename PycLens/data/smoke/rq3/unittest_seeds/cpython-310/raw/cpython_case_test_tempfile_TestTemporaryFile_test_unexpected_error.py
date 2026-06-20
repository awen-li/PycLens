# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestTemporaryFile_test_unexpected_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dir = tempfile.mkdtemp()
    self.addCleanup(os_helper.rmtree, dir)
    with mock.patch('tempfile._O_TMPFILE_WORKS', False), mock.patch('os.unlink') as mock_unlink, mock.patch('os.open') as mock_open, mock.patch('os.close') as mock_close:
        mock_unlink.side_effect = KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):
            tempfile.TemporaryFile(dir=dir)
    mock_close.assert_called()
    self.assertEqual(os.listdir(dir), [])

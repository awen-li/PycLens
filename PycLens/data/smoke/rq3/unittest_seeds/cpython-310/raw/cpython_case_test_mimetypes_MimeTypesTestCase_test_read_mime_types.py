# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: MimeTypesTestCase_test_read_mime_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    self.assertIsNone(mimetypes.read_mime_types('non-existent'))
    with os_helper.temp_dir() as directory:
        data = 'x-application/x-unittest pyunit\n'
        file = pathlib.Path(directory, 'sample.mimetype')
        file.write_text(data, encoding='utf-8')
        mime_dict = mimetypes.read_mime_types(file)
        eq(mime_dict['.pyunit'], 'x-application/x-unittest')
    data = 'application/no-mans-land  Français'
    filename = 'filename'
    fp = io.StringIO(data)
    with unittest.mock.patch.object(mimetypes, 'open', return_value=fp) as mock_open:
        mime_dict = mimetypes.read_mime_types(filename)
        mock_open.assert_called_with(filename, encoding='utf-8')
    eq(mime_dict['.Français'], 'application/no-mans-land')

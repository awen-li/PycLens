# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: MimeTypesTestCase_test_path_like_ob

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = 'LICENSE.txt'
    filepath = pathlib.Path(filename)
    filepath_with_abs_dir = pathlib.Path('/dir/' + filename)
    filepath_relative = pathlib.Path('../dir/' + filename)
    path_dir = pathlib.Path('./')
    expected = self.db.guess_type(filename)
    self.assertEqual(self.db.guess_type(filepath), expected)
    self.assertEqual(self.db.guess_type(filepath_with_abs_dir), expected)
    self.assertEqual(self.db.guess_type(filepath_relative), expected)
    self.assertEqual(self.db.guess_type(path_dir), (None, None))

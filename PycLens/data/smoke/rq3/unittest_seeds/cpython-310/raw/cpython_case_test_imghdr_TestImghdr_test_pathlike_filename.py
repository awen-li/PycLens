# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imghdr.py
# case: TestImghdr_test_pathlike_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (filename, expected) in TEST_FILES:
        with self.subTest(filename=filename):
            filename = findfile(filename, subdir='imghdrdata')
            self.assertEqual(imghdr.what(pathlib.Path(filename)), expected)

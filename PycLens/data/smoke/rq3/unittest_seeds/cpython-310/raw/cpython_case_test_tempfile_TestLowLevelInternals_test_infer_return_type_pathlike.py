# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestLowLevelInternals_test_infer_return_type_pathlike

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Path:

        def __init__(self, path):
            self.path = path

        def __fspath__(self):
            return self.path
    self.assertIs(str, tempfile._infer_return_type(Path('/')))
    self.assertIs(bytes, tempfile._infer_return_type(Path(b'/')))
    self.assertIs(str, tempfile._infer_return_type('', Path('')))
    self.assertIs(bytes, tempfile._infer_return_type(b'', Path(b'')))
    self.assertIs(bytes, tempfile._infer_return_type(None, Path(b'')))
    self.assertIs(str, tempfile._infer_return_type(None, Path('')))
    with self.assertRaises(TypeError):
        tempfile._infer_return_type('', Path(b''))
    with self.assertRaises(TypeError):
        tempfile._infer_return_type(b'', Path(''))

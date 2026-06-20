# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imghdr.py
# case: TestImghdr_test_string_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', BytesWarning)
        for (filename, _) in TEST_FILES:
            filename = findfile(filename, subdir='imghdrdata')
            with open(filename, 'rb') as stream:
                data = stream.read().decode('latin1')
            with self.assertRaises(TypeError):
                imghdr.what(io.StringIO(data))
            with self.assertRaises(TypeError):
                imghdr.what(None, data)

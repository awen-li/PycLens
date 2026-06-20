# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imghdr.py
# case: TestImghdr_test_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (filename, expected) in TEST_FILES:
        filename = findfile(filename, subdir='imghdrdata')
        self.assertEqual(imghdr.what(filename), expected)
        with open(filename, 'rb') as stream:
            self.assertEqual(imghdr.what(stream), expected)
        with open(filename, 'rb') as stream:
            data = stream.read()
        self.assertEqual(imghdr.what(None, data), expected)
        self.assertEqual(imghdr.what(None, bytearray(data)), expected)

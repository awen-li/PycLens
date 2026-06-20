# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imghdr.py
# case: TestImghdr_test_unseekable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'wb') as stream:
        stream.write(self.testdata)
    with UnseekableIO(TESTFN, 'rb') as stream:
        with self.assertRaises(io.UnsupportedOperation):
            imghdr.what(stream)

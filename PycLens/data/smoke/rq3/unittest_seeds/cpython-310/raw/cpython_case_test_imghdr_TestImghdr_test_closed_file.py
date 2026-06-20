# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imghdr.py
# case: TestImghdr_test_closed_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stream = open(self.testfile, 'rb')
    stream.close()
    with self.assertRaises(ValueError) as cm:
        imghdr.what(stream)
    stream = io.BytesIO(self.testdata)
    stream.close()
    with self.assertRaises(ValueError) as cm:
        imghdr.what(stream)

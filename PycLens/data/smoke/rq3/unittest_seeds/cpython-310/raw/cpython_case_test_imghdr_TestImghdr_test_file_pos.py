# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imghdr.py
# case: TestImghdr_test_file_pos

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'wb') as stream:
        stream.write(b'ababagalamaga')
        pos = stream.tell()
        stream.write(self.testdata)
    with open(TESTFN, 'rb') as stream:
        stream.seek(pos)
        self.assertEqual(imghdr.what(stream), 'png')
        self.assertEqual(stream.tell(), pos)

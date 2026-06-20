# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imghdr.py
# case: TestImghdr_test_output_stream

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'wb') as stream:
        stream.write(self.testdata)
        stream.seek(0)
        with self.assertRaises(OSError) as cm:
            imghdr.what(stream)

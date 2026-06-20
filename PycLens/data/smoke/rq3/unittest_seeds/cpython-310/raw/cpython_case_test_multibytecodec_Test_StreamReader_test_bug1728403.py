# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_StreamReader_test_bug1728403

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        f = open(TESTFN, 'wb')
        try:
            f.write(b'\xa1')
        finally:
            f.close()
        f = codecs.open(TESTFN, encoding='cp949')
        try:
            self.assertRaises(UnicodeDecodeError, f.read, 2)
        finally:
            f.close()
    finally:
        os_helper.unlink(TESTFN)

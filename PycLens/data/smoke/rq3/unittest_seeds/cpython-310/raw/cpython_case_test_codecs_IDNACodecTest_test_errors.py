# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: IDNACodecTest_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    'python.org'.encode('idna', 'strict')
    b'python.org'.decode('idna', 'strict')
    for errors in ('ignore', 'replace', 'backslashreplace', 'surrogateescape'):
        self.assertRaises(Exception, 'python.org'.encode, 'idna', errors)
        self.assertRaises(Exception, b'python.org'.decode, 'idna', errors)

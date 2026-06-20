# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: LocaleCodecTest_test_encode_surrogatepass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        self.encode('', 'surrogatepass')
    except ValueError as exc:
        if str(exc) == 'unsupported error handler':
            self.skipTest(f"{self.ENCODING!r} encoder doesn't support surrogatepass error handler")
        else:
            raise
    self.check_encode_strings('surrogatepass')

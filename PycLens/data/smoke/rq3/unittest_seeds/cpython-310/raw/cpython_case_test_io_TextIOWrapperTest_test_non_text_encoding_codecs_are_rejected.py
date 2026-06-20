# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_non_text_encoding_codecs_are_rejected

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = self.BytesIO()
    b = self.BufferedWriter(r)
    with self.assertRaisesRegex(LookupError, 'is not a text encoding'):
        self.TextIOWrapper(b, encoding='hex')

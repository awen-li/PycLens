# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodePageTest_test_mbcs_alias

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with mock.patch('_winapi.GetACP', return_value=123):
        codec = codecs.lookup('cp123')
        self.assertEqual(codec.name, 'mbcs')

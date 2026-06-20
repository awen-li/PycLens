# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_xmlcharrefreplace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = 'スパモ änd eggs'
    self.assertEqual(s.encode('ascii', 'xmlcharrefreplace'), b'&#12473;&#12497;&#12514; &#228;nd eggs')
    self.assertEqual(s.encode('latin-1', 'xmlcharrefreplace'), b'&#12473;&#12497;&#12514; \xe4nd eggs')

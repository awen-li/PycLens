# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_IncrementalEncoder_test_subinterp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _testcapi
    encoding = 'cp932'
    text = 'Python の開発は、1990 年ごろから開始されています。'
    code = textwrap.dedent('\n            import codecs\n            encoding = %r\n            text = %r\n            encoder = codecs.getincrementalencoder(encoding)()\n            text2 = encoder.encode(text).decode(encoding)\n            if text2 != text:\n                raise ValueError(f"encoding issue: {text2!a} != {text!a}")\n        ') % (encoding, text)
    res = _testcapi.run_in_subinterp(code)
    self.assertEqual(res, 0)

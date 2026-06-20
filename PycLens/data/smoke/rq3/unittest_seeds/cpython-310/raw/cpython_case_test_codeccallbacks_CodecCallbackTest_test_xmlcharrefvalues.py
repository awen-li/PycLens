# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_xmlcharrefvalues

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    v = (1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000)
    s = ''.join([chr(x) for x in v])
    codecs.register_error('test.xmlcharrefreplace', codecs.xmlcharrefreplace_errors)
    for enc in ('ascii', 'iso-8859-15'):
        for err in ('xmlcharrefreplace', 'test.xmlcharrefreplace'):
            s.encode(enc, err)

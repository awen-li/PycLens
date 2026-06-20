# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_badhandlerresults

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    results = (42, 'foo', (1, 2, 3), ('foo', 1, 3), ('foo', None), ('foo',), ('foo', 1, 3), ('foo', None), ('foo',))
    encs = ('ascii', 'latin-1', 'iso-8859-1', 'iso-8859-15')
    for res in results:
        codecs.register_error('test.badhandler', lambda x: res)
        for enc in encs:
            self.assertRaises(TypeError, 'あ'.encode, enc, 'test.badhandler')
        for (enc, bytes) in (('ascii', b'\xff'), ('utf-8', b'\xff'), ('utf-7', b'+x-')):
            self.assertRaises(TypeError, bytes.decode, enc, 'test.badhandler')

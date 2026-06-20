# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_aifc.py
# case: AIFCLowLevelTest_test_write_header_comptype_raises

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for comptype in (b'ULAW', b'ulaw', b'ALAW', b'alaw', b'G722'):
        fout = aifc.open(io.BytesIO(), 'wb')
        fout.setsampwidth(1)
        fout.setcomptype(comptype, b'')
        self.assertRaises(aifc.Error, fout.close)
        fout.initfp(None)

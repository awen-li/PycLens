# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_aifc.py
# case: AIFCLowLevelTest_test_write_params_bunch

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fout = aifc.open(io.BytesIO(), 'wb')
    fout.aifc()
    p = (1, 2, 3, 4, b'NONE', b'name')
    fout.setparams(p)
    self.assertEqual(fout.getparams(), p)
    fout.initfp(None)

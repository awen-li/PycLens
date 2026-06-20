# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_is_char_device_true

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls('/dev/null')
    if not P.exists():
        self.skipTest('/dev/null required')
    self.assertTrue(P.is_char_device())
    self.assertFalse(P.is_block_device())
    self.assertFalse(P.is_file())
    self.assertIs(self.cls('/dev/null\udfff').is_char_device(), False)
    self.assertIs(self.cls('/dev/null\x00').is_char_device(), False)

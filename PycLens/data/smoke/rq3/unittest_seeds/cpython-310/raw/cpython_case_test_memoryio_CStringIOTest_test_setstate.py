# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: CStringIOTest_test_setstate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    memio = self.ioclass()
    memio.__setstate__(('no error', '\n', 0, None))
    memio.__setstate__(('no error', '', 0, {'spam': 3}))
    self.assertRaises(ValueError, memio.__setstate__, ('', 'f', 0, None))
    self.assertRaises(ValueError, memio.__setstate__, ('', '', -1, None))
    self.assertRaises(TypeError, memio.__setstate__, (b'', '', 0, None))
    self.assertRaises(TypeError, memio.__setstate__, ('', b'', 0, None))
    self.assertRaises(TypeError, memio.__setstate__, ('', '', 0.0, None))
    self.assertRaises(TypeError, memio.__setstate__, ('', '', 0, 0))
    self.assertRaises(TypeError, memio.__setstate__, ('len-test', 0))
    self.assertRaises(TypeError, memio.__setstate__)
    self.assertRaises(TypeError, memio.__setstate__, 0)
    memio.close()
    self.assertRaises(ValueError, memio.__setstate__, ('closed', '', 0, None))

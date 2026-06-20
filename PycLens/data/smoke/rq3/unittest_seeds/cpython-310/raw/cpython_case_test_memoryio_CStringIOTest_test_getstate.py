# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: CStringIOTest_test_getstate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    memio = self.ioclass()
    state = memio.__getstate__()
    self.assertEqual(len(state), 4)
    self.assertIsInstance(state[0], str)
    self.assertIsInstance(state[1], str)
    self.assertIsInstance(state[2], int)
    if state[3] is not None:
        self.assertIsInstance(state[3], dict)
    memio.close()
    self.assertRaises(ValueError, memio.__getstate__)

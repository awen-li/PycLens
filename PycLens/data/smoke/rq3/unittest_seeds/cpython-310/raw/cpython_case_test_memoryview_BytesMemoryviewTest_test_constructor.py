# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: BytesMemoryviewTest_test_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for tp in self._types:
        ob = tp(self._source)
        self.assertTrue(memoryview(ob))
        self.assertTrue(memoryview(object=ob))
        self.assertRaises(TypeError, memoryview)
        self.assertRaises(TypeError, memoryview, ob, ob)
        self.assertRaises(TypeError, memoryview, argument=ob)
        self.assertRaises(TypeError, memoryview, ob, argument=True)

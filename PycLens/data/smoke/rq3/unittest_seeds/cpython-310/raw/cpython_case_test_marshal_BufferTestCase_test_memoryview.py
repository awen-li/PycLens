# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: BufferTestCase_test_memoryview

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = memoryview(b'abc')
    self.helper(b)
    new = marshal.loads(marshal.dumps(b))
    self.assertEqual(type(new), bytes)

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: BufferTestCase_test_array

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array('B', b'abc')
    new = marshal.loads(marshal.dumps(a))
    self.assertEqual(new, b'abc')

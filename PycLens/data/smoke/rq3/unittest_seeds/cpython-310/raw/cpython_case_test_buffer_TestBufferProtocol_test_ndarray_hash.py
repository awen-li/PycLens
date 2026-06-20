# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array('L', [1, 2, 3])
    nd = ndarray(a)
    self.assertRaises(ValueError, hash, nd)
    b = bytes(list(range(12)))
    nd = ndarray(list(range(12)), shape=[12])
    self.assertEqual(hash(nd), hash(b))
    nd = ndarray(list(range(12)), shape=[3, 4])
    self.assertEqual(hash(nd), hash(b))
    nd = ndarray(list(range(12)), shape=[3, 2, 2])
    self.assertEqual(hash(nd), hash(b))
    b = bytes(transpose(list(range(12)), shape=[4, 3]))
    nd = ndarray(list(range(12)), shape=[3, 4], flags=ND_FORTRAN)
    self.assertEqual(hash(nd), hash(b))
    b = bytes(transpose(list(range(12)), shape=[2, 3, 2]))
    nd = ndarray(list(range(12)), shape=[2, 3, 2], flags=ND_FORTRAN)
    self.assertEqual(hash(nd), hash(b))
    b = bytes(list(range(12)))
    nd = ndarray(list(range(12)), shape=[2, 2, 3], flags=ND_PIL)
    self.assertEqual(hash(nd), hash(b))
    nd = ndarray(list(range(12)), shape=[2, 2, 3], format='L')
    self.assertEqual(hash(nd), hash(nd.tobytes()))

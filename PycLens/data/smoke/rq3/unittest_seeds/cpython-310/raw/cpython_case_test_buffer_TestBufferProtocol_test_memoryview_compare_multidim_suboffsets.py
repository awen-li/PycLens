# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_compare_multidim_suboffsets

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ex1 = ndarray(list(range(40)), shape=[5, 8], format='@I')
    nd1 = ex1[3:1:-1, ::-2]
    ex2 = ndarray(list(range(40)), shape=[5, 8], format='I', flags=ND_PIL)
    nd2 = ex2[1:3:1, ::-2]
    v = memoryview(nd1)
    w = memoryview(nd2)
    self.assertEqual(v, nd1)
    self.assertEqual(w, nd2)
    self.assertNotEqual(v, nd2)
    self.assertNotEqual(w, nd1)
    self.assertNotEqual(v, w)
    ex1 = ndarray([(2 ** 64 - 1, -1)] * 40, shape=[5, 8], format='=Qq', flags=ND_WRITABLE)
    ex1[2][7] = (1, -2)
    nd1 = ex1[3:1:-1, ::-2]
    ex2 = ndarray([(2 ** 64 - 1, -1)] * 40, shape=[5, 8], format='>Qq', flags=ND_PIL | ND_WRITABLE)
    ex2[2][7] = (1, -2)
    nd2 = ex2[1:3:1, ::-2]
    v = memoryview(nd1)
    w = memoryview(nd2)
    self.assertEqual(v, nd1)
    self.assertEqual(w, nd2)
    self.assertEqual(v, nd2)
    self.assertEqual(w, nd1)
    self.assertEqual(v, w)
    ex1 = ndarray(list(range(30)), shape=[2, 3, 5], format='b', flags=ND_PIL)
    nd1 = ex1[1:3, ::-2]
    nd2 = ndarray(list(range(30)), shape=[3, 2, 5], format='b')
    nd2 = ex2[1:3, ::-2]
    v = memoryview(nd1)
    w = memoryview(nd2)
    self.assertEqual(v, nd1)
    self.assertEqual(w, nd2)
    self.assertNotEqual(v, nd2)
    self.assertNotEqual(w, nd1)
    self.assertNotEqual(v, w)
    ex1 = ndarray([(2 ** 8 - 1, -1)] * 40, shape=[2, 3, 5], format='Bb', flags=ND_PIL | ND_WRITABLE)
    nd1 = ex1[1:2, ::-2]
    ex2 = ndarray([(2 ** 8 - 1, -1)] * 40, shape=[3, 2, 5], format='Bb')
    nd2 = ex2[1:2, ::-2]
    v = memoryview(nd1)
    w = memoryview(nd2)
    self.assertEqual(v, nd1)
    self.assertEqual(w, nd2)
    self.assertNotEqual(v, nd2)
    self.assertNotEqual(w, nd1)
    self.assertNotEqual(v, w)
    ex1 = ndarray(list(range(30)), shape=[5, 3, 2], format='i', flags=ND_PIL)
    nd1 = ex1[1:3, ::-2]
    ex2 = ndarray(list(range(30)), shape=[5, 3, 2], format='@I', flags=ND_PIL)
    nd2 = ex2[1:3, ::-2]
    v = memoryview(nd1)
    w = memoryview(nd2)
    self.assertEqual(v, nd1)
    self.assertEqual(w, nd2)
    self.assertEqual(v, nd2)
    self.assertEqual(w, nd1)
    self.assertEqual(v, w)
    ex1 = ndarray([(b'hello', b'', 1)] * 27, shape=[3, 3, 3], format='5s0sP', flags=ND_PIL | ND_WRITABLE)
    ex1[1][2][2] = (b'sushi', b'', 1)
    nd1 = ex1[1:3, ::-2]
    ex2 = ndarray([(b'hello', b'', 1)] * 27, shape=[3, 3, 3], format='5s0sP', flags=ND_PIL | ND_WRITABLE)
    ex1[1][2][2] = (b'sushi', b'', 1)
    nd2 = ex2[1:3, ::-2]
    v = memoryview(nd1)
    w = memoryview(nd2)
    self.assertEqual(v, nd1)
    self.assertEqual(w, nd2)
    self.assertNotEqual(v, nd2)
    self.assertNotEqual(w, nd1)
    self.assertNotEqual(v, w)
    lst1 = list(range(-15, 15))
    lst2 = transpose(lst1, [3, 2, 5])
    nd1 = ndarray(lst1, shape=[3, 2, 5], format='@l', flags=ND_PIL)
    nd2 = ndarray(lst2, shape=[3, 2, 5], format='l', flags=ND_FORTRAN | ND_PIL)
    v = memoryview(nd1)
    w = memoryview(nd2)
    self.assertEqual(v, nd1)
    self.assertEqual(w, nd2)
    self.assertEqual(v, w)
    lst1 = [(b'sashimi', b'sliced', 20.05)] * 30
    lst1[11] = (b'ramen', b'spicy', 9.45)
    lst2 = transpose(lst1, [3, 2, 5])
    nd1 = ndarray(lst1, shape=[3, 2, 5], format='< 10p 9p d', flags=ND_PIL)
    nd2 = ndarray(lst2, shape=[3, 2, 5], format='> 10p 9p d', flags=ND_FORTRAN | ND_PIL)
    v = memoryview(nd1)
    w = memoryview(nd2)
    self.assertEqual(v, nd1)
    self.assertEqual(w, nd2)
    self.assertEqual(v, w)

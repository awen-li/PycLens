# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_compare_multidim_mixed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lst1 = list(range(-15, 15))
    lst2 = transpose(lst1, [3, 2, 5])
    nd1 = ndarray(lst1, shape=[3, 2, 5], format='@l')
    nd2 = ndarray(lst2, shape=[3, 2, 5], format='l', flags=ND_FORTRAN)
    v = memoryview(nd1)
    w = memoryview(nd2)
    self.assertEqual(v, nd1)
    self.assertEqual(w, nd2)
    self.assertEqual(v, w)
    lst1 = [(-3.3, -22, b'x')] * 30
    lst1[5] = (-2.2, -22, b'x')
    lst2 = transpose(lst1, [3, 2, 5])
    nd1 = ndarray(lst1, shape=[3, 2, 5], format='d b c')
    nd2 = ndarray(lst2, shape=[3, 2, 5], format='d h c', flags=ND_FORTRAN)
    v = memoryview(nd1)
    w = memoryview(nd2)
    self.assertEqual(v, nd1)
    self.assertEqual(w, nd2)
    self.assertEqual(v, w)
    ex1 = ndarray(list(range(40)), shape=[5, 8], format='@I')
    nd1 = ex1[3:1:-1, ::-2]
    ex2 = ndarray(list(range(40)), shape=[5, 8], format='I')
    nd2 = ex2[1:3:1, ::-2]
    v = memoryview(nd1)
    w = memoryview(nd2)
    self.assertEqual(v, nd1)
    self.assertEqual(w, nd2)
    self.assertNotEqual(v, nd2)
    self.assertNotEqual(w, nd1)
    self.assertNotEqual(v, w)
    ex1 = ndarray([(2 ** 31 - 1, -2 ** 31)] * 22, shape=[11, 2], format='=ii')
    nd1 = ex1[3:1:-1, ::-2]
    ex2 = ndarray([(2 ** 31 - 1, -2 ** 31)] * 22, shape=[11, 2], format='>ii')
    nd2 = ex2[1:3:1, ::-2]
    v = memoryview(nd1)
    w = memoryview(nd2)
    self.assertEqual(v, nd1)
    self.assertEqual(w, nd2)
    self.assertEqual(v, nd2)
    self.assertEqual(w, nd1)
    self.assertEqual(v, w)
    ex1 = ndarray(list(range(30)), shape=[2, 3, 5], format='b')
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
    ex1 = ndarray(list(range(30)), shape=[2, 3, 5], format='B')
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
    ex1 = ndarray([(2, b'123')] * 30, shape=[5, 3, 2], format='b3s')
    nd1 = ex1[1:3, ::-2]
    nd2 = ndarray([(2, b'123')] * 30, shape=[5, 3, 2], format='i3s')
    nd2 = ex2[1:3, ::-2]
    v = memoryview(nd1)
    w = memoryview(nd2)
    self.assertEqual(v, nd1)
    self.assertEqual(w, nd2)
    self.assertNotEqual(v, nd2)
    self.assertNotEqual(w, nd1)
    self.assertNotEqual(v, w)

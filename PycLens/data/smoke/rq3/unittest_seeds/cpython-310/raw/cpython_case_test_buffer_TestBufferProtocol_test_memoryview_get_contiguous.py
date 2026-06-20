# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_get_contiguous

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, get_contiguous, {}, PyBUF_READ, 'F')
    self.assertRaises(BufferError, get_contiguous, b'x', PyBUF_WRITE, 'C')
    nd = ndarray([1, 2, 3], shape=[2], strides=[2])
    self.assertRaises(BufferError, get_contiguous, nd, PyBUF_WRITE, 'A')
    nd = ndarray(9, shape=(), format='L')
    for order in ['C', 'F', 'A']:
        m = get_contiguous(nd, PyBUF_READ, order)
        self.assertEqual(m, nd)
        self.assertEqual(m[()], 9)
    nd = ndarray(9, shape=(), format='L', flags=ND_WRITABLE)
    for order in ['C', 'F', 'A']:
        m = get_contiguous(nd, PyBUF_READ, order)
        self.assertEqual(m, nd)
        self.assertEqual(m[()], 9)
    for order in ['C', 'F', 'A']:
        nd[()] = 9
        m = get_contiguous(nd, PyBUF_WRITE, order)
        self.assertEqual(m, nd)
        self.assertEqual(m[()], 9)
        m[()] = 10
        self.assertEqual(m[()], 10)
        self.assertEqual(nd[()], 10)
    nd = ndarray([1], shape=[0], format='L', flags=ND_WRITABLE)
    for order in ['C', 'F', 'A']:
        m = get_contiguous(nd, PyBUF_READ, order)
        self.assertRaises(IndexError, m.__getitem__, 0)
        self.assertEqual(m, nd)
        self.assertEqual(m.tolist(), [])
    nd = ndarray(list(range(8)), shape=[2, 0, 7], format='L', flags=ND_WRITABLE)
    for order in ['C', 'F', 'A']:
        m = get_contiguous(nd, PyBUF_READ, order)
        self.assertEqual(ndarray(m).tolist(), [[], []])
    nd = ndarray([1], shape=[1], format='h', flags=ND_WRITABLE)
    for order in ['C', 'F', 'A']:
        m = get_contiguous(nd, PyBUF_WRITE, order)
        self.assertEqual(m, nd)
        self.assertEqual(m.tolist(), nd.tolist())
    nd = ndarray([1, 2, 3], shape=[3], format='b', flags=ND_WRITABLE)
    for order in ['C', 'F', 'A']:
        m = get_contiguous(nd, PyBUF_WRITE, order)
        self.assertEqual(m, nd)
        self.assertEqual(m.tolist(), nd.tolist())
    nd = ndarray([1, 2, 3], shape=[2], strides=[2], flags=ND_WRITABLE)
    for order in ['C', 'F', 'A']:
        m = get_contiguous(nd, PyBUF_READ, order)
        self.assertEqual(m, nd)
        self.assertEqual(m.tolist(), nd.tolist())
        self.assertRaises(TypeError, m.__setitem__, 1, 20)
        self.assertEqual(m[1], 3)
        self.assertEqual(nd[1], 3)
    nd = nd[::-1]
    for order in ['C', 'F', 'A']:
        m = get_contiguous(nd, PyBUF_READ, order)
        self.assertEqual(m, nd)
        self.assertEqual(m.tolist(), nd.tolist())
        self.assertRaises(TypeError, m.__setitem__, 1, 20)
        self.assertEqual(m[1], 1)
        self.assertEqual(nd[1], 1)
    nd = ndarray(list(range(12)), shape=[3, 4], flags=ND_WRITABLE)
    for order in ['C', 'A']:
        m = get_contiguous(nd, PyBUF_WRITE, order)
        self.assertEqual(ndarray(m).tolist(), nd.tolist())
    self.assertRaises(BufferError, get_contiguous, nd, PyBUF_WRITE, 'F')
    m = get_contiguous(nd, PyBUF_READ, order)
    self.assertEqual(ndarray(m).tolist(), nd.tolist())
    nd = ndarray(list(range(12)), shape=[3, 4], flags=ND_WRITABLE | ND_FORTRAN)
    for order in ['F', 'A']:
        m = get_contiguous(nd, PyBUF_WRITE, order)
        self.assertEqual(ndarray(m).tolist(), nd.tolist())
    self.assertRaises(BufferError, get_contiguous, nd, PyBUF_WRITE, 'C')
    m = get_contiguous(nd, PyBUF_READ, order)
    self.assertEqual(ndarray(m).tolist(), nd.tolist())
    nd = ndarray(list(range(12)), shape=[3, 4], flags=ND_WRITABLE | ND_PIL)
    for order in ['C', 'F', 'A']:
        self.assertRaises(BufferError, get_contiguous, nd, PyBUF_WRITE, order)
        m = get_contiguous(nd, PyBUF_READ, order)
        self.assertEqual(ndarray(m).tolist(), nd.tolist())
    nd = ndarray([1, 2, 3, 4, 5], shape=[3], strides=[2])
    m = get_contiguous(nd, PyBUF_READ, 'C')
    self.assertTrue(m.c_contiguous)

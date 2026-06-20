# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_py_buffer_to_contiguous

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    requests = (PyBUF_INDIRECT, PyBUF_STRIDES, PyBUF_ND, PyBUF_SIMPLE, PyBUF_FULL, PyBUF_FULL_RO, PyBUF_RECORDS, PyBUF_RECORDS_RO, PyBUF_STRIDED, PyBUF_STRIDED_RO, PyBUF_CONTIG, PyBUF_CONTIG_RO)
    self.assertRaises(TypeError, py_buffer_to_contiguous, {}, 'F', PyBUF_FULL_RO)
    nd = ndarray(9, shape=(), format='L', flags=ND_WRITABLE)
    for order in ['C', 'F', 'A']:
        for request in requests:
            b = py_buffer_to_contiguous(nd, order, request)
            self.assertEqual(b, nd.tobytes())
    nd = ndarray([1], shape=[0], format='L', flags=ND_WRITABLE)
    for order in ['C', 'F', 'A']:
        for request in requests:
            b = py_buffer_to_contiguous(nd, order, request)
            self.assertEqual(b, b'')
    nd = ndarray(list(range(8)), shape=[2, 0, 7], format='L', flags=ND_WRITABLE)
    for order in ['C', 'F', 'A']:
        for request in requests:
            b = py_buffer_to_contiguous(nd, order, request)
            self.assertEqual(b, b'')
    for f in [0, ND_FORTRAN]:
        nd = ndarray([1], shape=[1], format='h', flags=f | ND_WRITABLE)
        ndbytes = nd.tobytes()
        for order in ['C', 'F', 'A']:
            for request in requests:
                b = py_buffer_to_contiguous(nd, order, request)
                self.assertEqual(b, ndbytes)
        nd = ndarray([1, 2, 3], shape=[3], format='b', flags=f | ND_WRITABLE)
        ndbytes = nd.tobytes()
        for order in ['C', 'F', 'A']:
            for request in requests:
                b = py_buffer_to_contiguous(nd, order, request)
                self.assertEqual(b, ndbytes)
    nd = ndarray([1, 2, 3], shape=[2], strides=[2], flags=ND_WRITABLE)
    ndbytes = nd.tobytes()
    for order in ['C', 'F', 'A']:
        for request in [PyBUF_STRIDES, PyBUF_FULL]:
            b = py_buffer_to_contiguous(nd, order, request)
            self.assertEqual(b, ndbytes)
    nd = nd[::-1]
    ndbytes = nd.tobytes()
    for order in ['C', 'F', 'A']:
        for request in requests:
            try:
                b = py_buffer_to_contiguous(nd, order, request)
            except BufferError:
                continue
            self.assertEqual(b, ndbytes)
    lst = list(range(12))
    for f in [0, ND_FORTRAN]:
        nd = ndarray(lst, shape=[3, 4], flags=f | ND_WRITABLE)
        if numpy_array:
            na = numpy_array(buffer=bytearray(lst), shape=[3, 4], dtype='B', order='C' if f == 0 else 'F')
        if f == ND_FORTRAN:
            x = ndarray(transpose(lst, [4, 3]), shape=[3, 4], flags=ND_WRITABLE)
            expected = x.tobytes()
        else:
            expected = nd.tobytes()
        for request in requests:
            try:
                b = py_buffer_to_contiguous(nd, 'C', request)
            except BufferError:
                continue
            self.assertEqual(b, expected)
            y = ndarray([v for v in b], shape=[3, 4], flags=ND_WRITABLE)
            self.assertEqual(memoryview(y), memoryview(nd))
            if numpy_array:
                self.assertEqual(b, na.tostring(order='C'))
        if f == 0:
            x = ndarray(transpose(lst, [3, 4]), shape=[4, 3], flags=ND_WRITABLE)
        else:
            x = ndarray(lst, shape=[3, 4], flags=ND_WRITABLE)
        expected = x.tobytes()
        for request in [PyBUF_FULL, PyBUF_FULL_RO, PyBUF_INDIRECT, PyBUF_STRIDES, PyBUF_ND]:
            try:
                b = py_buffer_to_contiguous(nd, 'F', request)
            except BufferError:
                continue
            self.assertEqual(b, expected)
            y = ndarray([v for v in b], shape=[3, 4], flags=ND_FORTRAN | ND_WRITABLE)
            self.assertEqual(memoryview(y), memoryview(nd))
            if numpy_array:
                self.assertEqual(b, na.tostring(order='F'))
        if f == ND_FORTRAN:
            x = ndarray(lst, shape=[3, 4], flags=ND_WRITABLE)
            expected = x.tobytes()
        else:
            expected = nd.tobytes()
        for request in [PyBUF_FULL, PyBUF_FULL_RO, PyBUF_INDIRECT, PyBUF_STRIDES, PyBUF_ND]:
            try:
                b = py_buffer_to_contiguous(nd, 'A', request)
            except BufferError:
                continue
            self.assertEqual(b, expected)
            y = ndarray([v for v in b], shape=[3, 4], flags=f | ND_WRITABLE)
            self.assertEqual(memoryview(y), memoryview(nd))
            if numpy_array:
                self.assertEqual(b, na.tostring(order='A'))
    nd = ndarray(list(range(12)), shape=[3, 4], flags=ND_WRITABLE | ND_PIL)
    b = py_buffer_to_contiguous(nd, 'C', PyBUF_FULL_RO)
    self.assertEqual(b, nd.tobytes())
    y = ndarray([v for v in b], shape=[3, 4], flags=ND_WRITABLE)
    self.assertEqual(memoryview(y), memoryview(nd))
    b = py_buffer_to_contiguous(nd, 'F', PyBUF_FULL_RO)
    x = ndarray(transpose(lst, [3, 4]), shape=[4, 3], flags=ND_WRITABLE)
    self.assertEqual(b, x.tobytes())
    y = ndarray([v for v in b], shape=[3, 4], flags=ND_FORTRAN | ND_WRITABLE)
    self.assertEqual(memoryview(y), memoryview(nd))
    b = py_buffer_to_contiguous(nd, 'A', PyBUF_FULL_RO)
    self.assertEqual(b, nd.tobytes())
    y = ndarray([v for v in b], shape=[3, 4], flags=ND_WRITABLE)
    self.assertEqual(memoryview(y), memoryview(nd))

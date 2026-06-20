# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_compare_special_cases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array('L', [1, 2, 3])
    b = array.array('L', [1, 2, 7])
    v = memoryview(a)
    w = memoryview(b)
    for attr in ('__lt__', '__le__', '__gt__', '__ge__'):
        self.assertIs(getattr(v, attr)(w), NotImplemented)
        self.assertIs(getattr(a, attr)(v), NotImplemented)
    v = memoryview(a)
    v.release()
    self.assertEqual(v, v)
    self.assertNotEqual(v, a)
    self.assertNotEqual(a, v)
    v = memoryview(a)
    w = memoryview(a)
    w.release()
    self.assertNotEqual(v, w)
    self.assertNotEqual(w, v)
    v = memoryview(a)
    self.assertNotEqual(v, [1, 2, 3])
    nd = ndarray([(0, 0)], shape=[1], format='l x d x', flags=ND_WRITABLE)
    nd[0] = (-1, float('nan'))
    self.assertNotEqual(memoryview(nd), nd)
    a = array.array('u', 'xyz')
    v = memoryview(a)
    self.assertNotEqual(a, v)
    self.assertNotEqual(v, a)
    if ctypes:

        class BEPoint(ctypes.BigEndianStructure):
            _fields_ = [('x', ctypes.c_long), ('y', ctypes.c_long)]
        point = BEPoint(100, 200)
        a = memoryview(point)
        b = memoryview(point)
        self.assertNotEqual(a, b)
        self.assertNotEqual(a, point)
        self.assertNotEqual(point, a)
        self.assertRaises(NotImplementedError, a.tolist)

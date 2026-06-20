# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_buffer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, self.example)
    m = memoryview(a)
    expected = m.tobytes()
    self.assertEqual(a.tobytes(), expected)
    self.assertEqual(a.tobytes()[0], expected[0])
    self.assertRaises(BufferError, a.append, a[0])
    self.assertEqual(m.tobytes(), expected)
    self.assertRaises(BufferError, a.extend, a[0:1])
    self.assertEqual(m.tobytes(), expected)
    self.assertRaises(BufferError, a.remove, a[0])
    self.assertEqual(m.tobytes(), expected)
    self.assertRaises(BufferError, a.pop, 0)
    self.assertEqual(m.tobytes(), expected)
    self.assertRaises(BufferError, a.fromlist, a.tolist())
    self.assertEqual(m.tobytes(), expected)
    self.assertRaises(BufferError, a.frombytes, a.tobytes())
    self.assertEqual(m.tobytes(), expected)
    if self.typecode == 'u':
        self.assertRaises(BufferError, a.fromunicode, a.tounicode())
        self.assertEqual(m.tobytes(), expected)
    self.assertRaises(BufferError, operator.imul, a, 2)
    self.assertEqual(m.tobytes(), expected)
    self.assertRaises(BufferError, operator.imul, a, 0)
    self.assertEqual(m.tobytes(), expected)
    self.assertRaises(BufferError, operator.setitem, a, slice(0, 0), a)
    self.assertEqual(m.tobytes(), expected)
    self.assertRaises(BufferError, operator.delitem, a, 0)
    self.assertEqual(m.tobytes(), expected)
    self.assertRaises(BufferError, operator.delitem, a, slice(0, 1))
    self.assertEqual(m.tobytes(), expected)

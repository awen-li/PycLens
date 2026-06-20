# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: OtherTest_test_use_released_memory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    size = 128

    def release():
        m.release()
        nonlocal ba
        ba = bytearray(size)

    class MyIndex:

        def __index__(self):
            release()
            return 4

    class MyFloat:

        def __float__(self):
            release()
            return 4.25

    class MyBool:

        def __bool__(self):
            release()
            return True
    ba = None
    m = memoryview(bytearray(b'\xff' * size))
    with self.assertRaises(ValueError):
        m[MyIndex()]
    ba = None
    m = memoryview(bytearray(b'\xff' * size))
    self.assertEqual(list(m[:MyIndex()]), [255] * 4)
    ba = None
    m = memoryview(bytearray(b'\xff' * size))
    self.assertEqual(list(m[MyIndex():8]), [255] * 4)
    ba = None
    m = memoryview(bytearray(b'\xff' * size)).cast('B', (64, 2))
    with self.assertRaisesRegex(ValueError, 'operation forbidden'):
        m[MyIndex(), 0]
    ba = None
    m = memoryview(bytearray(b'\xff' * size)).cast('B', (2, 64))
    with self.assertRaisesRegex(ValueError, 'operation forbidden'):
        m[0, MyIndex()]
    ba = None
    m = memoryview(bytearray(b'\xff' * size))
    with self.assertRaisesRegex(ValueError, 'operation forbidden'):
        m[MyIndex()] = 42
    self.assertEqual(ba[:8], b'\x00' * 8)
    ba = None
    m = memoryview(bytearray(b'\xff' * size))
    with self.assertRaisesRegex(ValueError, 'operation forbidden'):
        m[:MyIndex()] = b'spam'
    self.assertEqual(ba[:8], b'\x00' * 8)
    ba = None
    m = memoryview(bytearray(b'\xff' * size))
    with self.assertRaisesRegex(ValueError, 'operation forbidden'):
        m[MyIndex():8] = b'spam'
    self.assertEqual(ba[:8], b'\x00' * 8)
    ba = None
    m = memoryview(bytearray(b'\xff' * size)).cast('B', (64, 2))
    with self.assertRaisesRegex(ValueError, 'operation forbidden'):
        m[MyIndex(), 0] = 42
    self.assertEqual(ba[8:16], b'\x00' * 8)
    ba = None
    m = memoryview(bytearray(b'\xff' * size)).cast('B', (2, 64))
    with self.assertRaisesRegex(ValueError, 'operation forbidden'):
        m[0, MyIndex()] = 42
    self.assertEqual(ba[:8], b'\x00' * 8)
    ba = None
    m = memoryview(bytearray(b'\xff' * size))
    with self.assertRaisesRegex(ValueError, 'operation forbidden'):
        m[0] = MyIndex()
    self.assertEqual(ba[:8], b'\x00' * 8)
    for fmt in 'bhilqnBHILQN':
        with self.subTest(fmt=fmt):
            ba = None
            m = memoryview(bytearray(b'\xff' * size)).cast(fmt)
            with self.assertRaisesRegex(ValueError, 'operation forbidden'):
                m[0] = MyIndex()
            self.assertEqual(ba[:8], b'\x00' * 8)
    for fmt in 'fd':
        with self.subTest(fmt=fmt):
            ba = None
            m = memoryview(bytearray(b'\xff' * size)).cast(fmt)
            with self.assertRaisesRegex(ValueError, 'operation forbidden'):
                m[0] = MyFloat()
            self.assertEqual(ba[:8], b'\x00' * 8)
    ba = None
    m = memoryview(bytearray(b'\xff' * size)).cast('?')
    with self.assertRaisesRegex(ValueError, 'operation forbidden'):
        m[0] = MyBool()
    self.assertEqual(ba[:8], b'\x00' * 8)

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_struct_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class INT(object):

        def __init__(self, val):
            self.val = val

        def __int__(self):
            return self.val

    class IDX(object):

        def __init__(self, val):
            self.val = val

        def __index__(self):
            return self.val

    def f():
        return 7
    values = [INT(9), IDX(9), 2.2 + 3j, Decimal('-21.1'), 12.2, Fraction(5, 2), [1, 2, 3], {4, 5, 6}, {7: 8}, (), (9,), True, False, None, Ellipsis, b'a', b'abc', bytearray(b'a'), bytearray(b'abc'), 'a', 'abc', 'a', 'abc', f, lambda x: x]
    for (fmt, items, item) in iter_format(10, 'memoryview'):
        ex = ndarray(items, shape=[10], format=fmt, flags=ND_WRITABLE)
        nd = ndarray(items, shape=[10], format=fmt, flags=ND_WRITABLE)
        m = memoryview(ex)
        struct.pack_into(fmt, nd, 0, item)
        m[0] = item
        self.assertEqual(m[0], nd[0])
        itemsize = struct.calcsize(fmt)
        if 'P' in fmt:
            continue
        for v in values:
            struct_err = None
            try:
                struct.pack_into(fmt, nd, itemsize, v)
            except struct.error:
                struct_err = struct.error
            mv_err = None
            try:
                m[1] = v
            except (TypeError, ValueError) as e:
                mv_err = e.__class__
            if struct_err or mv_err:
                self.assertIsNot(struct_err, None)
                self.assertIsNot(mv_err, None)
            else:
                self.assertEqual(m[1], nd[1])

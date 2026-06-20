# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: MemoryTestMixin_test_pickling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = self.buftype('1234567890')
    memio = self.ioclass(buf)
    memio.foo = 42
    memio.seek(2)

    class PickleTestMemIO(self.ioclass):

        def __init__(me, initvalue, foo):
            self.ioclass.__init__(me, initvalue)
            me.foo = foo
    import __main__
    PickleTestMemIO.__module__ = '__main__'
    PickleTestMemIO.__qualname__ = PickleTestMemIO.__name__
    __main__.PickleTestMemIO = PickleTestMemIO
    submemio = PickleTestMemIO(buf, 80)
    submemio.seek(2)
    for proto in range(2, pickle.HIGHEST_PROTOCOL + 1):
        for obj in (memio, submemio):
            obj2 = pickle.loads(pickle.dumps(obj, protocol=proto))
            self.assertEqual(obj.getvalue(), obj2.getvalue())
            self.assertEqual(obj.__class__, obj2.__class__)
            self.assertEqual(obj.foo, obj2.foo)
            self.assertEqual(obj.tell(), obj2.tell())
            obj2.close()
            self.assertRaises(ValueError, pickle.dumps, obj2, proto)
    del __main__.PickleTestMemIO

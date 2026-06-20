# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: MemoryTestMixin_test_subclassing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = self.buftype('1234567890')

    def test1():

        class MemIO(self.ioclass):
            pass
        m = MemIO(buf)
        return m.getvalue()

    def test2():

        class MemIO(self.ioclass):

            def __init__(me, a, b):
                self.ioclass.__init__(me, a)
        m = MemIO(buf, None)
        return m.getvalue()
    self.assertEqual(test1(), buf)
    self.assertEqual(test2(), buf)

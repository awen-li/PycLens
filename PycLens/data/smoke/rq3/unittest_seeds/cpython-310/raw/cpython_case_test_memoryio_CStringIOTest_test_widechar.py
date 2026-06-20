# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: CStringIOTest_test_widechar

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = self.buftype('𠌊𠍇')
    memio = self.ioclass(buf)
    self.assertEqual(memio.getvalue(), buf)
    self.assertEqual(memio.write(buf), len(buf))
    self.assertEqual(memio.tell(), len(buf))
    self.assertEqual(memio.getvalue(), buf)
    self.assertEqual(memio.write(buf), len(buf))
    self.assertEqual(memio.tell(), len(buf) * 2)
    self.assertEqual(memio.getvalue(), buf + buf)

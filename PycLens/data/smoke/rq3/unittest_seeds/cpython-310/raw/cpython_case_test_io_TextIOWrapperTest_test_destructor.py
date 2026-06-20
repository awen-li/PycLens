# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_destructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = []
    base = self.BytesIO

    class MyBytesIO(base):

        def close(self):
            l.append(self.getvalue())
            base.close(self)
    b = MyBytesIO()
    t = self.TextIOWrapper(b, encoding='ascii')
    t.write('abc')
    del t
    support.gc_collect()
    self.assertEqual([b'abc'], l)

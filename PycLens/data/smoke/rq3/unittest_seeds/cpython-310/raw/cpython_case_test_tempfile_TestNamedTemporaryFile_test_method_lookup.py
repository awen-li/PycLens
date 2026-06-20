# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestNamedTemporaryFile_test_method_lookup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.do_create()
    wr = weakref.ref(f)
    write = f.write
    write2 = f.write
    del f
    write(b'foo')
    del write
    write2(b'bar')
    del write2
    if support.check_impl_detail(cpython=True):
        self.assertIsNone(wr())

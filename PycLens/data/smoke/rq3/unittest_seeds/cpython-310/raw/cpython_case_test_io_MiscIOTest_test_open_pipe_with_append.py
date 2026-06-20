# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: MiscIOTest_test_open_pipe_with_append

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (r, w) = os.pipe()
    self.addCleanup(os.close, r)
    f = self.open(w, 'a', encoding='utf-8')
    self.addCleanup(f.close)
    if sys.platform != 'win32':
        self.assertFalse(f.seekable())

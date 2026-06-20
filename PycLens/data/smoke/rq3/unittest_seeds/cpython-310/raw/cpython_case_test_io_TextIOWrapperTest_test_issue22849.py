# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_issue22849

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class F(object):

        def readable(self):
            return True

        def writable(self):
            return True

        def seekable(self):
            return True
    for i in range(10):
        try:
            self.TextIOWrapper(F(), encoding='utf-8')
        except Exception:
            pass
    F.tell = lambda x: 0
    t = self.TextIOWrapper(F(), encoding='utf-8')

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_unreadable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class UnReadable(self.BytesIO):

        def readable(self):
            return False
    txt = self.TextIOWrapper(UnReadable(), encoding='utf-8')
    self.assertRaises(OSError, txt.read)

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRWPairTest_test_isatty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class SelectableIsAtty(MockRawIO):

        def __init__(self, isatty):
            MockRawIO.__init__(self)
            self._isatty = isatty

        def isatty(self):
            return self._isatty
    pair = self.tp(SelectableIsAtty(False), SelectableIsAtty(False))
    self.assertFalse(pair.isatty())
    pair = self.tp(SelectableIsAtty(True), SelectableIsAtty(False))
    self.assertTrue(pair.isatty())
    pair = self.tp(SelectableIsAtty(False), SelectableIsAtty(True))
    self.assertTrue(pair.isatty())
    pair = self.tp(SelectableIsAtty(True), SelectableIsAtty(True))
    self.assertTrue(pair.isatty())

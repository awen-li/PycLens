# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_stripid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stripid = pydoc.stripid
    self.assertEqual(stripid('<function stripid at 0x88dcee4>'), '<function stripid>')
    self.assertEqual(stripid('<function stripid at 0x01F65390>'), '<function stripid>')
    self.assertEqual(stripid('42'), '42')
    self.assertEqual(stripid("<type 'exceptions.Exception'>"), "<type 'exceptions.Exception'>")

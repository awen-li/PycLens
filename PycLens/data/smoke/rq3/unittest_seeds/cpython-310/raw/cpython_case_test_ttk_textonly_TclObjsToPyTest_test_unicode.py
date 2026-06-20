# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ttk_textonly.py
# case: TclObjsToPyTest_test_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    adict = {'opt': 'välúè'}
    self.assertEqual(ttk.tclobjs_to_py(adict), {'opt': 'välúè'})
    adict['opt'] = MockTclObj(adict['opt'])
    self.assertEqual(ttk.tclobjs_to_py(adict), {'opt': 'välúè'})

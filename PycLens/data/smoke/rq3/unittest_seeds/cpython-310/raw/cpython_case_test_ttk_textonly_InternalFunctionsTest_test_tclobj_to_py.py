# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ttk_textonly.py
# case: InternalFunctionsTest_test_tclobj_to_py

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(ttk._tclobj_to_py((MockStateSpec('a', 'b'), 'val')), [('a', 'b', 'val')])
    self.assertEqual(ttk._tclobj_to_py([MockTclObj('1'), 2, MockTclObj('3m')]), [1, 2, '3m'])

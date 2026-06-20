# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ttk_textonly.py
# case: TclObjsToPyTest_test_multivalues

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    adict = {'opt': [1, 2, 3, 4]}
    self.assertEqual(ttk.tclobjs_to_py(adict), {'opt': [1, 2, 3, 4]})
    adict['opt'] = [1, 'xm', 3]
    self.assertEqual(ttk.tclobjs_to_py(adict), {'opt': [1, 'xm', 3]})
    adict['opt'] = (MockStateSpec('a', 'b'), 'válũè')
    self.assertEqual(ttk.tclobjs_to_py(adict), {'opt': [('a', 'b', 'válũè')]})
    self.assertEqual(ttk.tclobjs_to_py({'x': ['y z']}), {'x': ['y z']})

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tcl.py
# case: TclTest_test_new_tcl_obj

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    support.check_disallow_instantiation(self, _tkinter.Tcl_Obj)
    support.check_disallow_instantiation(self, _tkinter.TkttType)
    support.check_disallow_instantiation(self, _tkinter.TkappType)

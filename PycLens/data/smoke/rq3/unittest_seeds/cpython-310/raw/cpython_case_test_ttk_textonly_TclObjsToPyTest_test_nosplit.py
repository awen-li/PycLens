# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ttk_textonly.py
# case: TclObjsToPyTest_test_nosplit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(ttk.tclobjs_to_py({'text': 'some text'}), {'text': 'some text'})

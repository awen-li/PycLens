# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_var_annot_in_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ann_module3 = import_helper.import_fresh_module('test.ann_module3')
    with self.assertRaises(NameError):
        ann_module3.f_bad_ann()
    with self.assertRaises(NameError):
        ann_module3.g_bad_ann()
    with self.assertRaises(NameError):
        ann_module3.D_bad_ann(5)

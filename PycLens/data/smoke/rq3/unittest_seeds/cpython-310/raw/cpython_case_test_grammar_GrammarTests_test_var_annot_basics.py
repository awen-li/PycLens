# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_var_annot_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    var1: int = 5
    var2: [int, str]
    my_lst = [42]

    def one():
        return 1
    int.new_attr: int
    [list][0]: type
    my_lst[one() - 1]: int = 5
    self.assertEqual(my_lst, [5])

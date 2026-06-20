# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_annotations_constant_fold

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def g():

        def f(x: not int is int, /):
            ...
    codes = [(i.opname, i.argval) for i in dis.get_instructions(g)]
    self.assertNotIn(('UNARY_NOT', None), codes)
    self.assertIn(('IS_OP', 1), codes)

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_reprlib.py
# case: ReprTests_test_nesting

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(r([[[[[[[]]]]]]]), '[[[[[[[]]]]]]]')
    eq(r([[[[[[[[]]]]]]]]), '[[[[[[[...]]]]]]]')
    eq(r(nestedTuple(6)), '(((((((),),),),),),)')
    eq(r(nestedTuple(7)), '(((((((...),),),),),),)')
    eq(r({nestedTuple(5): nestedTuple(5)}), '{((((((),),),),),): ((((((),),),),),)}')
    eq(r({nestedTuple(6): nestedTuple(6)}), '{((((((...),),),),),): ((((((...),),),),),)}')
    eq(r([[[[[[{}]]]]]]), '[[[[[[{}]]]]]]')
    eq(r([[[[[[[{}]]]]]]]), '[[[[[[[...]]]]]]]')

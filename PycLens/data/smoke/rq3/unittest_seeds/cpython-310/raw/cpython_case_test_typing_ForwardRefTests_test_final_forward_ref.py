# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ForwardRefTests_test_final_forward_ref

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(gth(Loop, globals())['attr'], Final[Loop])
    self.assertNotEqual(gth(Loop, globals())['attr'], Final[int])
    self.assertNotEqual(gth(Loop, globals())['attr'], Final)

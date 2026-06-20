# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ForwardRefTests_test_forward_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fr = typing.ForwardRef('int')
    self.assertEqual(fr, typing.ForwardRef('int'))
    self.assertNotEqual(List['int'], List[int])
    self.assertNotEqual(fr, typing.ForwardRef('int', module=__name__))
    frm = typing.ForwardRef('int', module=__name__)
    self.assertEqual(frm, typing.ForwardRef('int', module=__name__))
    self.assertNotEqual(frm, typing.ForwardRef('int', module='__other_name__'))

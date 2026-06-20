# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: NamedTupleTests_test_annotation_usage_with_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(XMeth(1).double(), 2)
    self.assertEqual(XMeth(42).x, XMeth(42)[0])
    self.assertEqual(str(XRepr(42)), '42 -> 1')
    self.assertEqual(XRepr(1, 2) + XRepr(3), 0)
    with self.assertRaises(AttributeError):

        class XMethBad(NamedTuple):
            x: int

            def _fields(self):
                return 'no chance for this'
    with self.assertRaises(AttributeError):

        class XMethBad2(NamedTuple):
            x: int

            def _source(self):
                return 'no chance for this as well'

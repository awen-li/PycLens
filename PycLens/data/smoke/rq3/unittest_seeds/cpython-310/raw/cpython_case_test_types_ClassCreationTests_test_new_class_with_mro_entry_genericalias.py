# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: ClassCreationTests_test_new_class_with_mro_entry_genericalias

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    L1 = types.new_class('L1', (typing.List[int],), {})
    self.assertEqual(L1.__bases__, (list, typing.Generic))
    self.assertEqual(L1.__orig_bases__, (typing.List[int],))
    self.assertEqual(L1.__mro__, (L1, list, typing.Generic, object))
    L2 = types.new_class('L2', (list[int],), {})
    self.assertEqual(L2.__bases__, (list,))
    self.assertEqual(L2.__orig_bases__, (list[int],))
    self.assertEqual(L2.__mro__, (L2, list, object))

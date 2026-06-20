# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: ClassCreationTests_test_resolve_bases_with_mro_entry

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(types.resolve_bases((typing.List[int],)), (list, typing.Generic))
    self.assertEqual(types.resolve_bases((list[int],)), (list,))

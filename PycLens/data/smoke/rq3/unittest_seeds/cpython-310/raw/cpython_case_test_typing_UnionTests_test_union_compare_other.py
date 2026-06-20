# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: UnionTests_test_union_compare_other

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertNotEqual(Union, object)
    self.assertNotEqual(Union, Any)
    self.assertNotEqual(ClassVar, Union)
    self.assertNotEqual(Optional, Union)
    self.assertNotEqual([None], Optional)
    self.assertNotEqual(Optional, typing.Mapping)
    self.assertNotEqual(Optional[typing.MutableMapping], Union)

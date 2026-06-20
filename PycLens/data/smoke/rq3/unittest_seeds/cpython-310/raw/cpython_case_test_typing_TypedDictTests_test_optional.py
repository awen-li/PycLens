# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypedDictTests_test_optional

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    EmpD = TypedDict('EmpD', name=str, id=int)
    self.assertEqual(typing.Optional[EmpD], typing.Union[None, EmpD])
    self.assertNotEqual(typing.List[EmpD], typing.Tuple[EmpD])

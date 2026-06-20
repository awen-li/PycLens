# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestDocString_test_docstring_one_field_with_default_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: Union[int, type(None)] = None
    self.assertDocStrEqual(C.__doc__, 'C(x:Optional[int]=None)')

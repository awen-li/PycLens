# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_class_nested_enum_and_pickle_protocol_four

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NestedEnum(Enum):
        twigs = 'common'
        shiny = 'rare'
    self.__class__.NestedEnum = NestedEnum
    self.NestedEnum.__qualname__ = '%s.NestedEnum' % self.__class__.__name__
    test_pickle_dump_load(self.assertIs, self.NestedEnum.twigs)

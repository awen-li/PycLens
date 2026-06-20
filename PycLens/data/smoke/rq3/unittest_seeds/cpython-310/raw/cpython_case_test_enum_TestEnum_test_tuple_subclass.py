# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_tuple_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class SomeTuple(tuple, Enum):
        __qualname__ = 'SomeTuple'
        first = (1, 'for the money')
        second = (2, 'for the show')
        third = (3, 'for the music')
    self.assertIs(type(SomeTuple.first), SomeTuple)
    self.assertIsInstance(SomeTuple.second, tuple)
    self.assertEqual(SomeTuple.third, (3, 'for the music'))
    globals()['SomeTuple'] = SomeTuple
    test_pickle_dump_load(self.assertIs, SomeTuple.first)

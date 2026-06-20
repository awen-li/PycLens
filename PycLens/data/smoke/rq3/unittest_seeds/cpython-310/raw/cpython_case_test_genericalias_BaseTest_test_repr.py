# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyList(list):
        pass
    self.assertEqual(repr(list[str]), 'list[str]')
    self.assertEqual(repr(list[()]), 'list[()]')
    self.assertEqual(repr(tuple[int, ...]), 'tuple[int, ...]')
    self.assertTrue(repr(MyList[int]).endswith('.BaseTest.test_repr.<locals>.MyList[int]'))
    self.assertEqual(repr(list[str]()), '[]')

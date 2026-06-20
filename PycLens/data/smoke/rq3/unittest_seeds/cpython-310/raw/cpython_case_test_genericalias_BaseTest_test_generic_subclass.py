# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_generic_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyList(list):
        pass
    t = MyList[int]
    self.assertIs(t.__origin__, MyList)
    self.assertEqual(t.__args__, (int,))
    self.assertEqual(t.__parameters__, ())

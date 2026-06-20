# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_subclassing_types_genericalias

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class SubClass(GenericAlias):
        ...
    alias = SubClass(list, int)

    class Bad(GenericAlias):

        def __new__(cls, *args, **kwargs):
            super().__new__(cls, *args, **kwargs)
    self.assertEqual(alias, list[int])
    with self.assertRaises(TypeError):
        Bad(list, int, bad=int)

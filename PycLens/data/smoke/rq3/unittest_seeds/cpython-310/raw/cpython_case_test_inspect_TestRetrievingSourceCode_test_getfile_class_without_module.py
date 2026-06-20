# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestRetrievingSourceCode_test_getfile_class_without_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class CM(type):

        @property
        def __module__(cls):
            raise AttributeError

    class C(metaclass=CM):
        pass
    with self.assertRaises(TypeError):
        inspect.getfile(C)

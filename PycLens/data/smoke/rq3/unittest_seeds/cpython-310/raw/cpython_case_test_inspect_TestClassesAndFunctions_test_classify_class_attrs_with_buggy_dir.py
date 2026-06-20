# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_classify_class_attrs_with_buggy_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class M(type):

        def __dir__(cls):
            return ['__class__', '__name__', 'missing']

    class C(metaclass=M):
        pass
    attrs = [a[0] for a in inspect.classify_class_attrs(C)]
    self.assertNotIn('missing', attrs)

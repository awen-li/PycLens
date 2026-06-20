# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_type_annotations.py
# case: TypeAnnotationTests_test_annotations_getset_raises

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(AttributeError):
        print(float.__annotations__)
    with self.assertRaises(TypeError):
        float.__annotations__ = {}
    with self.assertRaises(TypeError):
        del float.__annotations__
    foo = type('Foo', (), {})
    foo.__annotations__ = {}
    del foo.__annotations__
    with self.assertRaises(AttributeError):
        del foo.__annotations__

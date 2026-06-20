# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_type_annotations.py
# case: TypeAnnotationTests_test_setting_annotations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    foo = type('Foo', (), {})
    for i in range(3):
        self.assertFalse('__annotations__' in foo.__dict__)
        d = {'a': int}
        foo.__annotations__ = d
        self.assertTrue('__annotations__' in foo.__dict__)
        self.assertEqual(foo.__annotations__, d)
        self.assertEqual(foo.__dict__['__annotations__'], d)
        del foo.__annotations__

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_type_annotations.py
# case: TypeAnnotationTests_test_annotations_are_created_correctly

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:
        a: int = 3
        b: str = 4
    self.assertTrue('__annotations__' in C.__dict__)
    del C.__annotations__
    self.assertFalse('__annotations__' in C.__dict__)

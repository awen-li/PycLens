# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_future.py
# case: AnnotationsFutureTestCase_test_annotation_with_complex_target

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(SyntaxError):
        exec('from __future__ import annotations\nobject.__debug__: int')

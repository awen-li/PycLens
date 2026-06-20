# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_future.py
# case: AnnotationsFutureTestCase_test_fstring_debug_annotations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertAnnotationEqual("f'{x=!r}'", expected="f'x={x!r}'")
    self.assertAnnotationEqual("f'{x=:}'", expected="f'x={x:}'")
    self.assertAnnotationEqual("f'{x=:.2f}'", expected="f'x={x:.2f}'")
    self.assertAnnotationEqual("f'{x=!r}'", expected="f'x={x!r}'")
    self.assertAnnotationEqual("f'{x=!a}'", expected="f'x={x!a}'")
    self.assertAnnotationEqual("f'{x=!s:*^20}'", expected="f'x={x!s:*^20}'")

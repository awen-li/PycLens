# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_future.py
# case: AnnotationsFutureTestCase_test_annotations_symbol_table_pass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    namespace = self._exec_future(dedent('\n        from __future__ import annotations\n\n        def foo():\n            outer = 1\n            def bar():\n                inner: outer = 1\n            return bar\n        '))
    foo = namespace.pop('foo')
    self.assertIsNone(foo().__closure__)
    self.assertEqual(foo.__code__.co_cellvars, ())
    self.assertEqual(foo().__code__.co_freevars, ())

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_future.py
# case: AnnotationsFutureTestCase_test_annotations_forbidden

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(SyntaxError):
        self._exec_future('test: (yield)')
    with self.assertRaises(SyntaxError):
        self._exec_future('test.test: (yield a + b)')
    with self.assertRaises(SyntaxError):
        self._exec_future('test[something]: (yield from x)')
    with self.assertRaises(SyntaxError):
        self._exec_future('def func(test: (yield from outside_of_generator)): pass')
    with self.assertRaises(SyntaxError):
        self._exec_future('def test() -> (await y): pass')
    with self.assertRaises(SyntaxError):
        self._exec_future('async def test() -> something((a := b)): pass')
    with self.assertRaises(SyntaxError):
        self._exec_future('test: await some.complicated[0].call(with_args=True or 1 is not 1)')
    with self.assertRaises(SyntaxError):
        self._exec_future("test: f'{(x := 10):=10}'")
    with self.assertRaises(SyntaxError):
        self._exec_future(dedent('            def foo():\n                def bar(arg: (yield)): pass\n            '))

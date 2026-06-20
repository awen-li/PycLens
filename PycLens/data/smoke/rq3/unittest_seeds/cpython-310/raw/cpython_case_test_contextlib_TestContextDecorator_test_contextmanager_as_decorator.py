# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestContextDecorator_test_contextmanager_as_decorator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @contextmanager
    def woohoo(y):
        state.append(y)
        yield
        state.append(999)
    state = []

    @woohoo(1)
    def test(x):
        self.assertEqual(state, [1])
        state.append(x)
    test('something')
    self.assertEqual(state, [1, 'something', 999])
    state = []
    test('something else')
    self.assertEqual(state, [1, 'something else', 999])

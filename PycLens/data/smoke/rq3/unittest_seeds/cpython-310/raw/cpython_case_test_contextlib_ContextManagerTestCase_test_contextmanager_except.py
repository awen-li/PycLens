# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: ContextManagerTestCase_test_contextmanager_except

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    state = []

    @contextmanager
    def woohoo():
        state.append(1)
        try:
            yield 42
        except ZeroDivisionError as e:
            state.append(e.args[0])
            self.assertEqual(state, [1, 42, 999])
    with woohoo() as x:
        self.assertEqual(state, [1])
        self.assertEqual(x, 42)
        state.append(x)
        raise ZeroDivisionError(999)
    self.assertEqual(state, [1, 42, 999])

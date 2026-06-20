# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: ContextManagerTestCase_test_recursive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    depth = 0

    @contextmanager
    def woohoo():
        nonlocal depth
        before = depth
        depth += 1
        yield
        depth -= 1
        self.assertEqual(depth, before)

    @woohoo()
    def recursive():
        if depth < 10:
            recursive()
    recursive()
    self.assertEqual(depth, 0)

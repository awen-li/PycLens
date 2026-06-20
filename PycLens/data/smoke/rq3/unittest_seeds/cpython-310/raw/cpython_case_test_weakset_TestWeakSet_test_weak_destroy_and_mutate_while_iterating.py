# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_weak_destroy_and_mutate_while_iterating

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    items = [ustr(c) for c in string.ascii_letters]
    s = WeakSet(items)

    @contextlib.contextmanager
    def testcontext():
        try:
            it = iter(s)
            yielded = ustr(str(next(it)))
            u = ustr(str(items.pop()))
            if yielded == u:
                next(it)
            gc.collect()
            yield u
        finally:
            it = None
    with testcontext() as u:
        self.assertNotIn(u, s)
    with testcontext() as u:
        self.assertRaises(KeyError, s.remove, u)
    self.assertNotIn(u, s)
    with testcontext() as u:
        s.add(u)
    self.assertIn(u, s)
    t = s.copy()
    with testcontext() as u:
        s.update(t)
    self.assertEqual(len(s), len(t))
    with testcontext() as u:
        s.clear()
    self.assertEqual(len(s), 0)

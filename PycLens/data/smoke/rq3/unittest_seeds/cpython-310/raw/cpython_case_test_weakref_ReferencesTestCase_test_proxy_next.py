# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_proxy_next

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    arr = [4, 5, 6]

    def iterator_func():
        yield from arr
    it = iterator_func()

    class IteratesWeakly:

        def __iter__(self):
            return weakref.proxy(it)
    weak_it = IteratesWeakly()
    self.assertEqual(list(weak_it), [4, 5, 6])

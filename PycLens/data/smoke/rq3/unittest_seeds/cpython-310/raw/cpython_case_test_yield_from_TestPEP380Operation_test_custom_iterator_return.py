# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_custom_iterator_return

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyIter:

        def __iter__(self):
            return self

        def __next__(self):
            raise StopIteration(42)

    def gen():
        nonlocal ret
        ret = (yield from MyIter())
    ret = None
    list(gen())
    self.assertEqual(ret, 42)

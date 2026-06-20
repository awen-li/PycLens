# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest__check_async_iterator_anext_test_send

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = ait_class()
    obj = anext(p, 'completed')
    with self.assertRaises(StopIteration):
        with contextlib.closing(obj.__await__()) as g:
            g.send(None)

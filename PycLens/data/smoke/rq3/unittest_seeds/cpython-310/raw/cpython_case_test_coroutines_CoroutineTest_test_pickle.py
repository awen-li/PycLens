# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def func():
        pass
    coro = func()
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        with self.assertRaises((TypeError, pickle.PicklingError)):
            pickle.dumps(coro, proto)
    aw = coro.__await__()
    try:
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            with self.assertRaises((TypeError, pickle.PicklingError)):
                pickle.dumps(aw, proto)
    finally:
        aw.close()

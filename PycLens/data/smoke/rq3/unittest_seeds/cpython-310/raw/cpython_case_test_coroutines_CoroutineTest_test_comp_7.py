# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_comp_7

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def f():
        yield 1
        yield 2
        raise Exception('aaa')

    async def run_list():
        return [i async for i in f()]
    with self.assertRaisesRegex(Exception, 'aaa'):
        run_async(run_list())

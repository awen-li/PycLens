# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_anext_return_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class WithGenAnext:

        def __aiter__(self):
            return self

        def __anext__(self):
            yield
    result = self.loop.run_until_complete(self.check_anext_returning_iterator(WithGenAnext))
    self.assertEqual(result, 'completed')

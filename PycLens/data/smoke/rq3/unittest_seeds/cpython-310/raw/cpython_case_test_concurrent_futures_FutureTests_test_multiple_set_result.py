# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: FutureTests_test_multiple_set_result

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = create_future(state=PENDING)
    f.set_result(1)
    with self.assertRaisesRegex(futures.InvalidStateError, 'FINISHED: <Future at 0x[0-9a-f]+ state=finished returned int>'):
        f.set_result(2)
    self.assertTrue(f.done())
    self.assertEqual(f.result(), 1)

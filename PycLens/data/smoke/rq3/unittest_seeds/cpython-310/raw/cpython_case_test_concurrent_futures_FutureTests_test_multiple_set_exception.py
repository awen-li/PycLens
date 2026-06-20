# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: FutureTests_test_multiple_set_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = create_future(state=PENDING)
    e = ValueError()
    f.set_exception(e)
    with self.assertRaisesRegex(futures.InvalidStateError, 'FINISHED: <Future at 0x[0-9a-f]+ state=finished raised ValueError>'):
        f.set_exception(Exception())
    self.assertEqual(f.exception(), e)

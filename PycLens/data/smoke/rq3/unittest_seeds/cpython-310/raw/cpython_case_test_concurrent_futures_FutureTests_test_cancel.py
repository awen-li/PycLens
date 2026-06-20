# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: FutureTests_test_cancel

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f1 = create_future(state=PENDING)
    f2 = create_future(state=RUNNING)
    f3 = create_future(state=CANCELLED)
    f4 = create_future(state=CANCELLED_AND_NOTIFIED)
    f5 = create_future(state=FINISHED, exception=OSError())
    f6 = create_future(state=FINISHED, result=5)
    self.assertTrue(f1.cancel())
    self.assertEqual(f1._state, CANCELLED)
    self.assertFalse(f2.cancel())
    self.assertEqual(f2._state, RUNNING)
    self.assertTrue(f3.cancel())
    self.assertEqual(f3._state, CANCELLED)
    self.assertTrue(f4.cancel())
    self.assertEqual(f4._state, CANCELLED_AND_NOTIFIED)
    self.assertFalse(f5.cancel())
    self.assertEqual(f5._state, FINISHED)
    self.assertFalse(f6.cancel())
    self.assertEqual(f6._state, FINISHED)

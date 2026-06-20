# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: HelperFunctionTests_test_readwriteexc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tr1 = exitingdummy()
    self.assertRaises(asyncore.ExitNow, asyncore.read, tr1)
    self.assertRaises(asyncore.ExitNow, asyncore.write, tr1)
    self.assertRaises(asyncore.ExitNow, asyncore._exception, tr1)
    tr2 = crashingdummy()
    asyncore.read(tr2)
    self.assertEqual(tr2.error_handled, True)
    tr2 = crashingdummy()
    asyncore.write(tr2)
    self.assertEqual(tr2.error_handled, True)
    tr2 = crashingdummy()
    asyncore._exception(tr2)
    self.assertEqual(tr2.error_handled, True)

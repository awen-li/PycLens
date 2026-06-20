# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: GetCurrentTests_test_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    main = interpreters.get_main()
    cur = interpreters.get_current()
    self.assertEqual(cur, main)
    self.assertIsInstance(cur, interpreters.InterpreterID)

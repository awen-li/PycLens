# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: GetMainTests_test_from_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    [expected] = interpreters.list_all()
    main = interpreters.get_main()
    self.assertEqual(main, expected)
    self.assertIsInstance(main, interpreters.InterpreterID)

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestInterpreterClose_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    main = interpreters.get_main()
    interp1 = interpreters.create()
    interp2 = interpreters.create()
    interp3 = interpreters.create()
    self.assertEqual(set(interpreters.list_all()), {main, interp1, interp2, interp3})
    interp2.close()
    self.assertEqual(set(interpreters.list_all()), {main, interp1, interp3})

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestInterpreterAttrs_test_id_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    main = interpreters.get_main()
    current = interpreters.get_current()
    interp = interpreters.create()
    self.assertIsInstance(main.id, _interpreters.InterpreterID)
    self.assertIsInstance(current.id, _interpreters.InterpreterID)
    self.assertIsInstance(interp.id, _interpreters.InterpreterID)

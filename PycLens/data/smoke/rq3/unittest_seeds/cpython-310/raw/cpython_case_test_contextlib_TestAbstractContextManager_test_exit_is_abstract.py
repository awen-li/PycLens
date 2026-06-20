# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestAbstractContextManager_test_exit_is_abstract

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MissingExit(AbstractContextManager):
        pass
    with self.assertRaises(TypeError):
        MissingExit()

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: GenericTests_test_functions_module_attr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for name in dir(signal):
        value = getattr(signal, name)
        if inspect.isroutine(value) and (not inspect.isbuiltin(value)):
            self.assertEqual(value.__module__, 'signal')

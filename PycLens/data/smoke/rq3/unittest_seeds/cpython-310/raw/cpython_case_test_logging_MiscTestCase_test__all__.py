# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: MiscTestCase_test__all__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    not_exported = {'logThreads', 'logMultiprocessing', 'logProcesses', 'currentframe', 'PercentStyle', 'StrFormatStyle', 'StringTemplateStyle', 'Filterer', 'PlaceHolder', 'Manager', 'RootLogger', 'root', 'threading'}
    support.check__all__(self, logging, not_exported=not_exported)

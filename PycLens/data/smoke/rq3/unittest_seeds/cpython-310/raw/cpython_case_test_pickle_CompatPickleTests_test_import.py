# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pickle.py
# case: CompatPickleTests_test_import

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    modules = set(IMPORT_MAPPING.values())
    modules |= set(REVERSE_IMPORT_MAPPING)
    modules |= {module for (module, name) in REVERSE_NAME_MAPPING}
    modules |= {module for (module, name) in NAME_MAPPING.values()}
    for module in modules:
        try:
            getmodule(module)
        except ImportError:
            pass

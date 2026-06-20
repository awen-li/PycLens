# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: test_pickle_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    for protocol in range(HIGHEST_PROTOCOL + 1):
        with assertion(exception):
            dumps(obj, protocol=protocol)

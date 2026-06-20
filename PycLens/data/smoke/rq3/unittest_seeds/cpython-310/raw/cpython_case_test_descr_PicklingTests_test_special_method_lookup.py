# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: PicklingTests_test_special_method_lookup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    protocols = range(pickle.HIGHEST_PROTOCOL + 1)

    class Picky:

        def __getstate__(self):
            return {}

        def __getattr__(self, attr):
            if attr in ('__getnewargs__', '__getnewargs_ex__'):
                raise AssertionError(attr)
            return None
    for protocol in protocols:
        state = {} if protocol >= 2 else None
        self._check_reduce(protocol, Picky(), state=state)

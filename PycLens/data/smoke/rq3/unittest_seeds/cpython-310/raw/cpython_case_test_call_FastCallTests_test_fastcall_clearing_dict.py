# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: FastCallTests_test_fastcall_clearing_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class IntWithDict:
        __slots__ = ['kwargs']

        def __init__(self, **kwargs):
            self.kwargs = kwargs

        def __index__(self):
            self.kwargs.clear()
            gc.collect()
            return 0
    x = IntWithDict(optimize=IntWithDict())
    compile('pass', '', 'exec', x, **x.kwargs)

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_weakref

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        p = proxy(s)
        self.assertEqual(p.fileno(), s.fileno())
    s = None
    support.gc_collect()
    try:
        p.fileno()
    except ReferenceError:
        pass
    else:
        self.fail('Socket proxy still exists')

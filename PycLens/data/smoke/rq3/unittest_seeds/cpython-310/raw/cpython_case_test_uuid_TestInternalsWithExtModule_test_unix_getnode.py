# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uuid.py
# case: TestInternalsWithExtModule_test_unix_getnode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not importable('_uuid') and (not importable('ctypes')):
        self.skipTest('neither _uuid extension nor ctypes available')
    try:
        node = self.uuid._unix_getnode()
    except TypeError:
        self.skipTest('requires uuid_generate_time')
    self.check_node(node, 'unix')

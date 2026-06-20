# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winreg.py
# case: LocalWinregTests_test_connect_registry_to_local_machine_works

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    self.assertNotEqual(h.handle, 0)
    h.Close()
    self.assertEqual(h.handle, 0)

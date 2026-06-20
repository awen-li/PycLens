# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winreg.py
# case: LocalWinregTests_test_context_manager

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        with ConnectRegistry(None, HKEY_LOCAL_MACHINE) as h:
            self.assertNotEqual(h.handle, 0)
            raise OSError
    except OSError:
        self.assertEqual(h.handle, 0)

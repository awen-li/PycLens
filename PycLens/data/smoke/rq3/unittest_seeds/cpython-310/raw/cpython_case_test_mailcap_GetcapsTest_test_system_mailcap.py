# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailcap.py
# case: GetcapsTest_test_system_mailcap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    caps = mailcap.getcaps()
    self.assertIsInstance(caps, dict)
    mailcapfiles = mailcap.listmailcapfiles()
    existingmcfiles = [mcf for mcf in mailcapfiles if os.path.exists(mcf)]
    if existingmcfiles:
        for (k, v) in caps.items():
            self.assertIsInstance(k, str)
            self.assertIsInstance(v, list)
            for e in v:
                self.assertIsInstance(e, dict)
    else:
        self.assertEqual({}, caps)

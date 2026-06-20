# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_nt_helpers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    executable = nt._getfinalpathname(sys.executable)
    for path in (executable, os.fsencode(executable)):
        volume_path = nt._getvolumepathname(path)
        path_drive = ntpath.splitdrive(path)[0]
        volume_path_drive = ntpath.splitdrive(volume_path)[0]
        self.assertEqualCI(path_drive, volume_path_drive)
    (cap, free) = nt._getdiskusage(sys.exec_prefix)
    self.assertGreater(cap, 0)
    self.assertGreater(free, 0)
    (b_cap, b_free) = nt._getdiskusage(sys.exec_prefix.encode())
    self.assertEqual(b_cap, cap)
    self.assertGreater(b_free, 0)
    for path in [sys.prefix, sys.executable]:
        final_path = nt._getfinalpathname(path)
        self.assertIsInstance(final_path, str)
        self.assertGreater(len(final_path), 0)
        b_final_path = nt._getfinalpathname(path.encode())
        self.assertIsInstance(b_final_path, bytes)
        self.assertGreater(len(b_final_path), 0)

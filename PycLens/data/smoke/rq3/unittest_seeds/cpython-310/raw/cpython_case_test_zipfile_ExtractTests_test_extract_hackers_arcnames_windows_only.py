# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: ExtractTests_test_extract_hackers_arcnames_windows_only

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    windows_hacknames = [('..\\foo\\bar', 'foo/bar'), ('..\\/foo\\/bar', 'foo/bar'), ('foo/\\..\\/bar', 'foo/bar'), ('foo\\/../\\bar', 'foo/bar'), ('C:foo/bar', 'foo/bar'), ('C:/foo/bar', 'foo/bar'), ('C://foo/bar', 'foo/bar'), ('C:\\foo\\bar', 'foo/bar'), ('//conky/mountpoint/foo/bar', 'foo/bar'), ('\\\\conky\\mountpoint\\foo\\bar', 'foo/bar'), ('///conky/mountpoint/foo/bar', 'conky/mountpoint/foo/bar'), ('\\\\\\conky\\mountpoint\\foo\\bar', 'conky/mountpoint/foo/bar'), ('//conky//mountpoint/foo/bar', 'conky/mountpoint/foo/bar'), ('\\\\conky\\\\mountpoint\\foo\\bar', 'conky/mountpoint/foo/bar'), ('//?/C:/foo/bar', 'foo/bar'), ('\\\\?\\C:\\foo\\bar', 'foo/bar'), ('C:/../C:/foo/bar', 'C_/foo/bar'), ('a:b\\c<d>e|f"g?h*i', 'b/c_d_e_f_g_h_i'), ('../../foo../../ba..r', 'foo/ba..r')]
    self._test_extract_hackers_arcnames(windows_hacknames)

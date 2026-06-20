# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: ExtractTests_test_sanitize_windows_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    san = zipfile.ZipFile._sanitize_windows_name
    self.assertEqual(san(',,?,C:,foo,bar/z', ','), '_,C_,foo,bar/z')
    self.assertEqual(san('a\\b,c<d>e|f"g?h*i', ','), 'a\\b,c_d_e_f_g_h_i')
    self.assertEqual(san('../../foo../../ba..r', '/'), 'foo/ba..r')

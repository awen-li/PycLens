# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: HelperFunctionsTests_test_addpackage_import_bad_pth_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (pth_dir, pth_fn) = self.make_pth('abc\x00def\n')
    with captured_stderr() as err_out:
        self.assertFalse(site.addpackage(pth_dir, pth_fn, set()))
    self.maxDiff = None
    self.assertEqual(err_out.getvalue(), '')
    for path in sys.path:
        if isinstance(path, str):
            self.assertNotIn('abc\x00def', path)

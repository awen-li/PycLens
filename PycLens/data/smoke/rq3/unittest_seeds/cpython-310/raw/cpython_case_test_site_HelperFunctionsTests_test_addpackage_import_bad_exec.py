# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: HelperFunctionsTests_test_addpackage_import_bad_exec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (pth_dir, pth_fn) = self.make_pth('randompath\nimport nosuchmodule\n')
    with captured_stderr() as err_out:
        site.addpackage(pth_dir, pth_fn, set())
    self.assertRegex(err_out.getvalue(), 'line 2')
    self.assertRegex(err_out.getvalue(), re.escape(os.path.join(pth_dir, pth_fn)))
    self.assertRegex(err_out.getvalue(), 'Traceback')
    self.assertRegex(err_out.getvalue(), 'ModuleNotFoundError')

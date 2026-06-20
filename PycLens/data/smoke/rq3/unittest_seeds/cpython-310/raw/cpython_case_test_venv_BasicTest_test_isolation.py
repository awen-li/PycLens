# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_venv.py
# case: BasicTest_test_isolation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (ssp, s) in ((True, 'true'), (False, 'false')):
        builder = venv.EnvBuilder(clear=True, system_site_packages=ssp)
        builder.create(self.env_dir)
        data = self.get_text_file_contents('pyvenv.cfg')
        self.assertIn('include-system-site-packages = %s\n' % s, data)

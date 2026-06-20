# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_home

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.EnvironmentVarGuard() as env:
        self._test_home(self.cls.home())
        env.clear()
        env['USERPROFILE'] = os.path.join(BASE, 'userprofile')
        self._test_home(self.cls.home())
        env['HOME'] = os.path.join(BASE, 'home')
        self._test_home(self.cls.home())

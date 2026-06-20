# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_webbrowser.py
# case: ImportTest_test_environment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    webbrowser = import_helper.import_fresh_module('webbrowser')
    try:
        browser = webbrowser.get().name
    except (webbrowser.Error, AttributeError) as err:
        self.skipTest(str(err))
    with os_helper.EnvironmentVarGuard() as env:
        env['BROWSER'] = browser
        webbrowser = import_helper.import_fresh_module('webbrowser')
        webbrowser.get()

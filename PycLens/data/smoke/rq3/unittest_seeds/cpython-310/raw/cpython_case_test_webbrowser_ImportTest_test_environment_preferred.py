# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_webbrowser.py
# case: ImportTest_test_environment_preferred

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    webbrowser = import_helper.import_fresh_module('webbrowser')
    try:
        webbrowser.get()
        least_preferred_browser = webbrowser.get(webbrowser._tryorder[-1]).name
    except (webbrowser.Error, AttributeError, IndexError) as err:
        self.skipTest(str(err))
    with os_helper.EnvironmentVarGuard() as env:
        env['BROWSER'] = least_preferred_browser
        webbrowser = import_helper.import_fresh_module('webbrowser')
        self.assertEqual(webbrowser.get().name, least_preferred_browser)
    with os_helper.EnvironmentVarGuard() as env:
        env['BROWSER'] = sys.executable
        webbrowser = import_helper.import_fresh_module('webbrowser')
        self.assertEqual(webbrowser.get().name, sys.executable)

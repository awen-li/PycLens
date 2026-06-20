# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_webbrowser.py
# case: ImportTest_test_get

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    webbrowser = import_helper.import_fresh_module('webbrowser')
    self.assertIsNone(webbrowser._tryorder)
    self.assertFalse(webbrowser._browsers)
    with self.assertRaises(webbrowser.Error):
        webbrowser.get('fakebrowser')
    self.assertIsNotNone(webbrowser._tryorder)

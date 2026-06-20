# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_webbrowser.py
# case: ImportTest_test_synthesize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    webbrowser = import_helper.import_fresh_module('webbrowser')
    name = os.path.basename(sys.executable).lower()
    webbrowser.register(name, None, webbrowser.GenericBrowser(name))
    webbrowser.get(sys.executable)

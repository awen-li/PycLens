# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_modulefinder.py
# case: ModuleFinderTest_test_load_module_api

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class CheckLoadModuleApi(modulefinder.ModuleFinder):

        def __init__(self, *args, **kwds):
            super().__init__(*args, **kwds)

        def load_module(self, fqname, fp, pathname, file_info):
            (suffix, mode, type) = file_info
            return super().load_module(fqname, fp, pathname, file_info)
    self._do_test(absolute_import_test, modulefinder_class=CheckLoadModuleApi)

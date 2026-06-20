# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestReload_test_getsource_reload

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with _ready_to_import('reload_bug', self.src_before) as (name, path):
        module = importlib.import_module(name)
        self.assertInspectEqual(path, module)
        with open(path, 'w', encoding='utf-8') as src:
            src.write(self.src_after)
        self.assertInspectEqual(path, module)

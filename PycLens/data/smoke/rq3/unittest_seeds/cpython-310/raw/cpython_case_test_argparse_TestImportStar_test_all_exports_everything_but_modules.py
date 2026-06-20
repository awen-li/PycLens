# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestImportStar_test_all_exports_everything_but_modules

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    items = [name for (name, value) in vars(argparse).items() if not (name.startswith('_') or name == 'ngettext') if not inspect.ismodule(value)]
    self.assertEqual(sorted(items), sorted(argparse.__all__))

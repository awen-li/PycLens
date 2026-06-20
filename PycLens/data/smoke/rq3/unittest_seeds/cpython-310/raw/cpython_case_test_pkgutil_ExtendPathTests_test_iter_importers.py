# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkgutil.py
# case: ExtendPathTests_test_iter_importers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    iter_importers = pkgutil.iter_importers
    get_importer = pkgutil.get_importer
    pkgname = 'spam'
    modname = 'eggs'
    dirname = self.create_init(pkgname)
    pathitem = os.path.join(dirname, pkgname)
    fullname = '{}.{}'.format(pkgname, modname)
    sys.modules.pop(fullname, None)
    sys.modules.pop(pkgname, None)
    try:
        self.create_submodule(dirname, pkgname, modname, 0)
        importlib.import_module(fullname)
        importers = list(iter_importers(fullname))
        expected_importer = get_importer(pathitem)
        for finder in importers:
            spec = pkgutil._get_spec(finder, fullname)
            loader = spec.loader
            try:
                loader = loader.loader
            except AttributeError:
                pass
            self.assertIsInstance(finder, importlib.machinery.FileFinder)
            self.assertEqual(finder, expected_importer)
            self.assertIsInstance(loader, importlib.machinery.SourceFileLoader)
            self.assertIsNone(pkgutil._get_spec(finder, pkgname))
        with self.assertRaises(ImportError):
            list(iter_importers('invalid.module'))
        with self.assertRaises(ImportError):
            list(iter_importers('.spam'))
    finally:
        shutil.rmtree(dirname)
        del sys.path[0]
        try:
            del sys.modules['spam']
            del sys.modules['spam.eggs']
        except KeyError:
            pass

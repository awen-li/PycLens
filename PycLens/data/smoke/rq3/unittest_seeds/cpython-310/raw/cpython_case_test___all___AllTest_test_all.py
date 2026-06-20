# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test___all__.py
# case: AllTest_test_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    denylist = set(['__future__'])
    if not sys.platform.startswith('java'):
        import _socket
    ignored = []
    failed_imports = []
    lib_dir = os.path.dirname(os.path.dirname(__file__))
    for (path, modname) in self.walk_modules(lib_dir, ''):
        m = modname
        denied = False
        while m:
            if m in denylist:
                denied = True
                break
            m = m.rpartition('.')[0]
        if denied:
            continue
        if support.verbose:
            print(modname)
        try:
            with open(path, 'rb') as f:
                if b'__all__' not in f.read():
                    raise NoAll(modname)
                self.check_all(modname)
        except NoAll:
            ignored.append(modname)
        except FailedImport:
            failed_imports.append(modname)
    if support.verbose:
        print('Following modules have no __all__ and have been ignored:', ignored)
        print('Following modules failed to be imported:', failed_imports)

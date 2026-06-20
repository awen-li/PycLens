# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CompileallTestsBase_test_ignore_symlink_destination

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    allowed_path = os.path.join(self.directory, 'test', 'dir', 'allowed')
    symlinks_path = os.path.join(self.directory, 'test', 'dir', 'symlinks')
    prohibited_path = os.path.join(self.directory, 'test', 'dir', 'prohibited')
    os.makedirs(allowed_path)
    os.makedirs(symlinks_path)
    os.makedirs(prohibited_path)
    allowed_script = script_helper.make_script(allowed_path, 'test_allowed', 'a = 0')
    prohibited_script = script_helper.make_script(prohibited_path, 'test_prohibited', 'a = 0')
    allowed_symlink = os.path.join(symlinks_path, 'test_allowed.py')
    prohibited_symlink = os.path.join(symlinks_path, 'test_prohibited.py')
    os.symlink(allowed_script, allowed_symlink)
    os.symlink(prohibited_script, prohibited_symlink)
    allowed_bc = importlib.util.cache_from_source(allowed_symlink)
    prohibited_bc = importlib.util.cache_from_source(prohibited_symlink)
    compileall.compile_dir(symlinks_path, quiet=True, limit_sl_dest=allowed_path)
    self.assertTrue(os.path.isfile(allowed_bc))
    self.assertFalse(os.path.isfile(prohibited_bc))

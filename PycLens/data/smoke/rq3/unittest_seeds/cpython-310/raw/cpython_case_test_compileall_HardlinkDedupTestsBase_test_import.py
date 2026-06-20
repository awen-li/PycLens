# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: HardlinkDedupTestsBase_test_import

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.temporary_directory():
        script = self.make_script(self.create_code(), name='module')
        self.compile_dir()
        self.check_hardlinks(script)
        pycs = get_pycs(script)
        inode = os.stat(pycs[0]).st_ino
        script = self.make_script('print(0)', name='module')
        script_helper.assert_python_ok('-O', '-c', 'import module', __isolated=False, PYTHONPATH=self.path)
        self.assertEqual(inode, os.stat(pycs[0]).st_ino)
        self.assertEqual(inode, os.stat(pycs[2]).st_ino)
        self.assertFalse(is_hardlink(pycs[1], pycs[2]))
        self.assertFalse(filecmp.cmp(pycs[1], pycs[2], shallow=True))

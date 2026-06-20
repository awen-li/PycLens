# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: HardlinkDedupTestsBase_test_recompilation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.temporary_directory():
        script = self.make_script('a = 0')
        self.compile_dir()
        self.check_hardlinks(script)
        pycs = get_pycs(script)
        inode = os.stat(pycs[0]).st_ino
        script = self.make_script('print(0)')
        self.compile_dir(optimize=[0, 2], force=True)
        self.assertEqual(inode, os.stat(pycs[1]).st_ino)
        self.assertTrue(is_hardlink(pycs[0], pycs[2]))
        self.assertNotEqual(inode, os.stat(pycs[2]).st_ino)
        self.assertFalse(filecmp.cmp(pycs[1], pycs[2], shallow=True))

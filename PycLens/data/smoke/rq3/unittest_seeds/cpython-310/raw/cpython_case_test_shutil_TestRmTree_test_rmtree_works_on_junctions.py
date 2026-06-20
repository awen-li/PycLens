# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestRmTree_test_rmtree_works_on_junctions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmp = self.mkdtemp()
    dir1 = os.path.join(tmp, 'dir1')
    dir2 = os.path.join(dir1, 'dir2')
    dir3 = os.path.join(tmp, 'dir3')
    for d in (dir1, dir2, dir3):
        os.mkdir(d)
    file1 = os.path.join(tmp, 'file1')
    write_file(file1, 'foo')
    link1 = os.path.join(dir1, 'link1')
    _winapi.CreateJunction(dir2, link1)
    link2 = os.path.join(dir1, 'link2')
    _winapi.CreateJunction(dir3, link2)
    link3 = os.path.join(dir1, 'link3')
    _winapi.CreateJunction(file1, link3)
    shutil.rmtree(dir1)
    self.assertFalse(os.path.exists(dir1))
    self.assertTrue(os.path.exists(dir3))
    self.assertTrue(os.path.exists(file1))

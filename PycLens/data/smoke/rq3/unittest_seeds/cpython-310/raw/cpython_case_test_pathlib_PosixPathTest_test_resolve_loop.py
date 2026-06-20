# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PosixPathTest_test_resolve_loop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.symlink('linkX/inside', join('linkX'))
    self._check_symlink_loop(BASE, 'linkX')
    os.symlink('linkY', join('linkY'))
    self._check_symlink_loop(BASE, 'linkY')
    os.symlink('linkZ/../linkZ', join('linkZ'))
    self._check_symlink_loop(BASE, 'linkZ')
    self._check_symlink_loop(BASE, 'linkZ', 'foo', strict=False)
    os.symlink(join('linkU/inside'), join('linkU'))
    self._check_symlink_loop(BASE, 'linkU')
    os.symlink(join('linkV'), join('linkV'))
    self._check_symlink_loop(BASE, 'linkV')
    os.symlink(join('linkW/../linkW'), join('linkW'))
    self._check_symlink_loop(BASE, 'linkW')
    self._check_symlink_loop(BASE, 'linkW', 'foo', strict=False)

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: NonLocalSymlinkTests_test_directory_link_nonlocal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src = os.path.join('base', 'some_link')
    os.symlink('some_dir', src)
    assert os.path.isdir(src)

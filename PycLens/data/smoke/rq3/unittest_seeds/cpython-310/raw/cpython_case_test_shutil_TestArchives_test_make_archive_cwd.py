# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestArchives_test_make_archive_cwd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    current_dir = os.getcwd()
    root_dir = self.mkdtemp()

    def _breaks(*args, **kw):
        raise RuntimeError()
    dirs = []

    def _chdir(path):
        dirs.append(path)
        orig_chdir(path)
    register_archive_format('xxx', _breaks, [], 'xxx file')
    try:
        with support.swap_attr(os, 'chdir', _chdir) as orig_chdir:
            try:
                make_archive('xxx', 'xxx', root_dir=root_dir)
            except Exception:
                pass
        self.assertEqual(os.getcwd(), current_dir)
        self.assertEqual(dirs, [root_dir, current_dir])
    finally:
        unregister_archive_format('xxx')

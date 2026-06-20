# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: MiscTests_test_getcwd_long_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    min_len = 2000
    if sys.platform == 'vxworks':
        min_len = 1000
    dirlen = 200
    dirname = 'python_test_dir_'
    dirname = dirname + 'a' * (dirlen - len(dirname))
    with tempfile.TemporaryDirectory() as tmpdir:
        with os_helper.change_cwd(tmpdir) as path:
            expected = path
            while True:
                cwd = os.getcwd()
                self.assertEqual(cwd, expected)
                need = min_len - (len(cwd) + len(os.path.sep))
                if need <= 0:
                    break
                if len(dirname) > need and need > 0:
                    dirname = dirname[:need]
                path = os.path.join(path, dirname)
                try:
                    os.mkdir(path)
                    os.chdir(path)
                except FileNotFoundError:
                    break
                except OSError as exc:
                    if exc.errno == errno.ENAMETOOLONG:
                        break
                    else:
                        raise
                expected = path
            if support.verbose:
                print(f'Tested current directory length: {len(cwd)}')

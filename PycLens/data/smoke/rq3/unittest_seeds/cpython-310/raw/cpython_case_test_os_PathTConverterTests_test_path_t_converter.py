# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: PathTConverterTests_test_path_t_converter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    str_filename = os_helper.TESTFN
    if os.name == 'nt':
        bytes_fspath = bytes_filename = None
    else:
        bytes_filename = os.fsencode(os_helper.TESTFN)
        bytes_fspath = FakePath(bytes_filename)
    fd = os.open(FakePath(str_filename), os.O_WRONLY | os.O_CREAT)
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    self.addCleanup(os.close, fd)
    int_fspath = FakePath(fd)
    str_fspath = FakePath(str_filename)
    for (name, allow_fd, extra_args, cleanup_fn) in self.functions:
        with self.subTest(name=name):
            try:
                fn = getattr(os, name)
            except AttributeError:
                continue
            for path in (str_filename, bytes_filename, str_fspath, bytes_fspath):
                if path is None:
                    continue
                with self.subTest(name=name, path=path):
                    result = fn(path, *extra_args)
                    if cleanup_fn is not None:
                        cleanup_fn(result)
            with self.assertRaisesRegex(TypeError, 'to return str or bytes'):
                fn(int_fspath, *extra_args)
            if allow_fd:
                result = fn(fd, *extra_args)
                if cleanup_fn is not None:
                    cleanup_fn(result)
            else:
                with self.assertRaisesRegex(TypeError, 'os.PathLike'):
                    fn(fd, *extra_args)

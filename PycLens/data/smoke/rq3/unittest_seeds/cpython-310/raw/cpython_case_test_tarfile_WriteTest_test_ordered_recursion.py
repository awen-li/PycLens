# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: WriteTest_test_ordered_recursion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = os.path.join(TEMPDIR, 'directory')
    os.mkdir(path)
    open(os.path.join(path, '1'), 'a').close()
    open(os.path.join(path, '2'), 'a').close()
    try:
        tar = tarfile.open(tmpname, self.mode)
        try:
            with unittest.mock.patch('os.listdir') as mock_listdir:
                mock_listdir.return_value = ['2', '1']
                tar.add(path)
            paths = []
            for m in tar.getmembers():
                paths.append(os.path.split(m.name)[-1])
            self.assertEqual(paths, ['directory', '1', '2'])
        finally:
            tar.close()
    finally:
        os_helper.unlink(os.path.join(path, '1'))
        os_helper.unlink(os.path.join(path, '2'))
        os_helper.rmdir(path)

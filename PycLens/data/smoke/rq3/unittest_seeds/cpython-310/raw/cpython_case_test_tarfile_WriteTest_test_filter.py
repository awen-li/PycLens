# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: WriteTest_test_filter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tempdir = os.path.join(TEMPDIR, 'filter')
    os.mkdir(tempdir)
    try:
        for name in ('foo', 'bar', 'baz'):
            name = os.path.join(tempdir, name)
            os_helper.create_empty_file(name)

        def filter(tarinfo):
            if os.path.basename(tarinfo.name) == 'bar':
                return
            tarinfo.uid = 123
            tarinfo.uname = 'foo'
            return tarinfo
        tar = tarfile.open(tmpname, self.mode, encoding='iso8859-1')
        try:
            tar.add(tempdir, arcname='empty_dir', filter=filter)
        finally:
            tar.close()
        with self.assertRaises(TypeError):
            tar.add(tempdir, 'empty_dir', True, None, filter)
        tar = tarfile.open(tmpname, 'r')
        try:
            for tarinfo in tar:
                self.assertEqual(tarinfo.uid, 123)
                self.assertEqual(tarinfo.uname, 'foo')
            self.assertEqual(len(tar.getmembers()), 3)
        finally:
            tar.close()
    finally:
        os_helper.rmtree(tempdir)

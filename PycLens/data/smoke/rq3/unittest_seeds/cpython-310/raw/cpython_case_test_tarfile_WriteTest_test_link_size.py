# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: WriteTest_test_link_size

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    link = os.path.join(TEMPDIR, 'link')
    target = os.path.join(TEMPDIR, 'link_target')
    with open(target, 'wb') as fobj:
        fobj.write(b'aaa')
    try:
        os.link(target, link)
    except PermissionError as e:
        self.skipTest('os.link(): %s' % e)
    try:
        tar = tarfile.open(tmpname, self.mode)
        try:
            tar.gettarinfo(target)
            tarinfo = tar.gettarinfo(link)
            self.assertEqual(tarinfo.size, 0)
        finally:
            tar.close()
    finally:
        os_helper.unlink(target)
        os_helper.unlink(link)

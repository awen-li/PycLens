# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: TestExtractionFilters_test_special_files

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for special_type in (tarfile.FIFOTYPE, tarfile.CHRTYPE, tarfile.BLKTYPE):
        tarinfo = tarfile.TarInfo('foo')
        tarinfo.type = special_type
        trusted = tarfile.fully_trusted_filter(tarinfo, '')
        self.assertIs(trusted, tarinfo)
        tar = tarfile.tar_filter(tarinfo, '')
        self.assertEqual(tar.type, special_type)
        with self.assertRaises(tarfile.SpecialFileError) as cm:
            tarfile.data_filter(tarinfo, '')
        self.assertIsInstance(cm.exception.tarinfo, tarfile.TarInfo)
        self.assertEqual(cm.exception.tarinfo.name, 'foo')

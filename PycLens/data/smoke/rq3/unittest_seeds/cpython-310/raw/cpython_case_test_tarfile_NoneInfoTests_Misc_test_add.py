# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: NoneInfoTests_Misc_test_add

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bio = io.BytesIO()
    for tarformat in (tarfile.USTAR_FORMAT, tarfile.GNU_FORMAT, tarfile.PAX_FORMAT):
        with self.subTest(tarformat=tarformat):
            tar = tarfile.open(fileobj=bio, mode='w', format=tarformat)
            tarinfo = tar.gettarinfo(tarname)
            try:
                tar.addfile(tarinfo)
            except Exception:
                if tarformat == tarfile.USTAR_FORMAT:
                    pass
                else:
                    raise
            else:
                for attr_name in ('mtime', 'mode', 'uid', 'gid', 'uname', 'gname'):
                    with self.subTest(attr_name=attr_name):
                        replaced = tarinfo.replace(**{attr_name: None})
                        with self.assertRaisesRegex(ValueError, f'{attr_name}'):
                            tar.addfile(replaced)

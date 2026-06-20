# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_open_via_zip_info

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN2, 'w', zipfile.ZIP_STORED) as zipfp:
        zipfp.writestr('name', 'foo')
        with self.assertWarns(UserWarning):
            zipfp.writestr('name', 'bar')
        self.assertEqual(zipfp.namelist(), ['name'] * 2)
    with zipfile.ZipFile(TESTFN2, 'r') as zipfp:
        infos = zipfp.infolist()
        data = b''
        for info in infos:
            with zipfp.open(info) as zipopen:
                data += zipopen.read()
        self.assertIn(data, {b'foobar', b'barfoo'})
        data = b''
        for info in infos:
            data += zipfp.read(info)
        self.assertIn(data, {b'foobar', b'barfoo'})

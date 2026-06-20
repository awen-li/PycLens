# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: RawConfigParserTestSambaConf_test_reading

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    smbconf = support.findfile('cfgparser.2')
    cf = self.newconfig()
    parsed_files = cf.read([smbconf, 'nonexistent-file'], encoding='utf-8')
    self.assertEqual(parsed_files, [smbconf])
    sections = ['global', 'homes', 'printers', 'print$', 'pdf-generator', 'tmp', 'Agustin']
    self.assertEqual(cf.sections(), sections)
    self.assertEqual(cf.get('global', 'workgroup'), 'MDKGROUP')
    self.assertEqual(cf.getint('global', 'max log size'), 50)
    self.assertEqual(cf.get('global', 'hosts allow'), '127.')
    self.assertEqual(cf.get('tmp', 'echo command'), 'cat %s; rm %s')

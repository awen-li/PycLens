# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__osx_support.py
# case: Test_OSXSupport_test__read_output

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if self.env['PATH']:
        self.env['PATH'] = self.env['PATH'] + ':'
    self.env['PATH'] = self.env['PATH'] + os.path.abspath(self.temp_path_dir)
    os_helper.unlink(self.prog_name)
    self.addCleanup(os_helper.unlink, self.prog_name)
    with open(self.prog_name, 'w') as f:
        f.write('#!/bin/sh\n/bin/echo ExpectedOutput\n')
    os.chmod(self.prog_name, stat.S_IRWXU)
    self.assertEqual('ExpectedOutput', _osx_support._read_output(self.prog_name))

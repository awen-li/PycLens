# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sundry.py
# case: TestUntestedModules_test_untested_modules_can_be_imported

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    untested = ('encodings',)
    with warnings_helper.check_warnings(quiet=True):
        for name in untested:
            try:
                import_helper.import_module('test.test_{}'.format(name))
            except unittest.SkipTest:
                importlib.import_module(name)
            else:
                self.fail('{} has tests even though test_sundry claims otherwise'.format(name))
        import distutils.bcppcompiler
        import distutils.ccompiler
        import distutils.cygwinccompiler
        import distutils.filelist
        import distutils.text_file
        import distutils.unixccompiler
        import distutils.command.bdist_dumb
        if sys.platform.startswith('win') and (not platform.win32_is_iot()):
            import distutils.command.bdist_msi
        import distutils.command.bdist
        import distutils.command.bdist_rpm
        import distutils.command.build_clib
        import distutils.command.build_ext
        import distutils.command.build
        import distutils.command.clean
        import distutils.command.config
        import distutils.command.install_data
        import distutils.command.install_egg_info
        import distutils.command.install_headers
        import distutils.command.install_lib
        import distutils.command.register
        import distutils.command.sdist
        import distutils.command.upload
        import html.entities
        try:
            import tty
        except ImportError:
            if support.verbose:
                print('skipping tty')

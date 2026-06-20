# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_init_warnoptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    warnoptions = ['ignore:::PyConfig_Insert0', 'default', 'ignore:::env1', 'ignore:::env2', 'ignore:::cmdline1', 'ignore:::cmdline2', 'default::BytesWarning', 'ignore:::PySys_AddWarnOption1', 'ignore:::PySys_AddWarnOption2', 'ignore:::PyConfig_BeforeRead', 'ignore:::PyConfig_AfterRead']
    preconfig = dict(allocator=PYMEM_ALLOCATOR_DEBUG)
    config = {'dev_mode': 1, 'faulthandler': 1, 'bytes_warning': 1, 'warnoptions': warnoptions, 'orig_argv': ['python3', '-Wignore:::cmdline1', '-Wignore:::cmdline2']}
    self.check_all_configs('test_init_warnoptions', config, preconfig, api=API_PYTHON)

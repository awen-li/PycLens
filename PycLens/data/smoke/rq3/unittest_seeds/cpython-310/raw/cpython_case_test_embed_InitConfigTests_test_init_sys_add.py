# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_init_sys_add

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config = {'faulthandler': 1, 'xoptions': ['config_xoption', 'cmdline_xoption', 'sysadd_xoption', 'faulthandler'], 'warnoptions': ['ignore:::cmdline_warnoption', 'ignore:::sysadd_warnoption', 'ignore:::config_warnoption'], 'orig_argv': ['python3', '-W', 'ignore:::cmdline_warnoption', '-X', 'cmdline_xoption']}
    self.check_all_configs('test_init_sys_add', config, api=API_PYTHON)

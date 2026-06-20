# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multiprocessing_main_handling.py
# case: MultiProcessingCmdLineMixin_test_ipython_workaround

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = test_source_main_skipped_in_children
    with os_helper.temp_dir() as script_dir:
        script_name = _make_test_script(script_dir, 'ipython', source=source)
        self._check_script(script_name)
        script_no_suffix = _make_test_script(script_dir, 'ipython', source=source, omit_suffix=True)
        self._check_script(script_no_suffix)

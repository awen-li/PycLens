# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multiprocessing_main_handling.py
# case: MultiProcessingCmdLineMixin_test_package

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = self.main_in_children_source
    with os_helper.temp_dir() as script_dir:
        pkg_dir = os.path.join(script_dir, 'test_pkg')
        make_pkg(pkg_dir)
        script_name = _make_test_script(pkg_dir, '__main__', source=source)
        launch_name = _make_launch_script(script_dir, 'launch', 'test_pkg')
        self._check_script(launch_name)

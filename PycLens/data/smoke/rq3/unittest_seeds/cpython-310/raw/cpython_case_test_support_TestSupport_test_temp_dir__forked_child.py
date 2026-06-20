# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_temp_dir__forked_child

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script_helper.assert_python_ok('-c', textwrap.dedent('\n            import os\n            from test import support\n            from test.support import os_helper\n            with os_helper.temp_cwd() as temp_path:\n                pid = os.fork()\n                if pid != 0:\n                    # parent process\n\n                    # wait for the child to terminate\n                    support.wait_process(pid, exitcode=0)\n\n                    # Make sure that temp_path is still present. When the child\n                    # process leaves the \'temp_cwd\'-context, the __exit__()-\n                    # method of the context must not remove the temporary\n                    # directory.\n                    if not os.path.isdir(temp_path):\n                        raise AssertionError("Child removed temp_path.")\n        '))

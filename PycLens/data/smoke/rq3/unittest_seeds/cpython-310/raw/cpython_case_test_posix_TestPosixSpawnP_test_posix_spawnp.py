# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixSpawnP_test_posix_spawnp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    temp_dir = tempfile.mkdtemp()
    self.addCleanup(os_helper.rmtree, temp_dir)
    program = 'posix_spawnp_test_program.exe'
    program_fullpath = os.path.join(temp_dir, program)
    os.symlink(sys.executable, program_fullpath)
    try:
        path = os.pathsep.join((temp_dir, os.environ['PATH']))
    except KeyError:
        path = temp_dir
    spawn_args = (program, '-I', '-S', '-c', 'pass')
    code = textwrap.dedent('\n            import os\n            from test import support\n\n            args = %a\n            pid = os.posix_spawnp(args[0], args, os.environ)\n\n            support.wait_process(pid, exitcode=0)\n        ' % (spawn_args,))
    args = ('-c', code)
    assert_python_ok(*args, PATH=path)

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fork1.py
# case: ForkTest_test_threaded_import_lock_fork

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import_started = threading.Event()
    fake_module_name = 'fake test module'
    partial_module = 'partial'
    complete_module = 'complete'

    def importer():
        imp.acquire_lock()
        sys.modules[fake_module_name] = partial_module
        import_started.set()
        time.sleep(0.01)
        sys.modules[fake_module_name] = complete_module
        imp.release_lock()
    t = threading.Thread(target=importer)
    t.start()
    import_started.wait()
    exitcode = 42
    pid = os.fork()
    try:
        if not pid:
            m = __import__(fake_module_name)
            if m == complete_module:
                os._exit(exitcode)
            else:
                if support.verbose > 1:
                    print('Child encountered partial module')
                os._exit(1)
        else:
            t.join()
            self.wait_impl(pid, exitcode=exitcode)
    finally:
        try:
            os.kill(pid, signal.SIGKILL)
        except OSError:
            pass

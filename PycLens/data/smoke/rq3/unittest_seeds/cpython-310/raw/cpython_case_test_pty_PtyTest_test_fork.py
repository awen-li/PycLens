# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pty.py
# case: PtyTest_test_fork

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    debug('calling pty.fork()')
    (pid, master_fd) = pty.fork()
    self.addCleanup(os.close, master_fd)
    if pid == pty.CHILD:
        if not os.isatty(1):
            debug("Child's fd 1 is not a tty?!")
            os._exit(3)
        debug('In child, calling os.setsid()')
        try:
            os.setsid()
        except OSError:
            debug('Good: OSError was raised.')
            pass
        except AttributeError:
            debug('No setsid() available?')
            pass
        except:
            debug('An unexpected error was raised.')
            os._exit(1)
        else:
            debug('os.setsid() succeeded! (bad!)')
            os._exit(2)
        os._exit(4)
    else:
        debug('Waiting for child (%d) to finish.' % pid)
        while True:
            try:
                data = os.read(master_fd, 80)
            except OSError:
                break
            if not data:
                break
            sys.stdout.write(str(data.replace(b'\r\n', b'\n'), encoding='ascii'))
        (pid, status) = os.waitpid(pid, 0)
        res = os.waitstatus_to_exitcode(status)
        debug('Child (%d) exited with code %d (status %d).' % (pid, res, status))
        if res == 1:
            self.fail('Child raised an unexpected exception in os.setsid()')
        elif res == 2:
            self.fail('pty.fork() failed to make child a session leader.')
        elif res == 3:
            self.fail('Child spawned by pty.fork() did not have a tty as stdout')
        elif res != 4:
            self.fail('pty.fork() failed for unknown reasons.')

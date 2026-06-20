# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ThreadPoolExecutorTest_test_executor_map_current_future_cancel

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stop_event = threading.Event()
    log = []

    def log_n_wait(ident):
        log.append(f'ident={ident!r} started')
        try:
            stop_event.wait()
        finally:
            log.append(f'ident={ident!r} stopped')
    with self.executor_type(max_workers=1) as pool:
        fut = pool.submit(log_n_wait, ident='first')
        try:
            with contextlib.closing(pool.map(log_n_wait, ['second', 'third'], timeout=0)) as gen:
                with self.assertRaises(futures.TimeoutError):
                    next(gen)
        finally:
            stop_event.set()
        fut.result()
    self.assertListEqual(log, ["ident='first' started", "ident='first' stopped"])

# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_threaded_hashing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hasher = hashlib.sha1()
    num_threads = 5
    smallest_data = b'swineflu'
    data = smallest_data * 200000
    expected_hash = hashlib.sha1(data * num_threads).hexdigest()

    def hash_in_chunks(chunk_size):
        index = 0
        while index < len(data):
            hasher.update(data[index:index + chunk_size])
            index += chunk_size
    threads = []
    for threadnum in range(num_threads):
        chunk_size = len(data) // 10 ** threadnum
        self.assertGreater(chunk_size, 0)
        self.assertEqual(chunk_size % len(smallest_data), 0)
        thread = threading.Thread(target=hash_in_chunks, args=(chunk_size,))
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    self.assertEqual(expected_hash, hasher.hexdigest())

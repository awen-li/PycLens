# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_init_read_set

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config = {'program_name': './init_read_set', 'executable': 'my_executable'}

    def modify_path(path):
        path.insert(1, 'test_path_insert1')
        path.append('test_path_append')
    self.check_all_configs('test_init_read_set', config, api=API_PYTHON, modify_path_cb=modify_path)

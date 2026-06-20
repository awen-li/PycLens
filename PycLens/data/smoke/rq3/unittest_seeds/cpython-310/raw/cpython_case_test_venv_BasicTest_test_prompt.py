# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_venv.py
# case: BasicTest_test_prompt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    env_name = os.path.split(self.env_dir)[1]
    rmtree(self.env_dir)
    builder = venv.EnvBuilder()
    self.run_with_capture(builder.create, self.env_dir)
    context = builder.ensure_directories(self.env_dir)
    data = self.get_text_file_contents('pyvenv.cfg')
    self.assertEqual(context.prompt, '(%s) ' % env_name)
    self.assertNotIn('prompt = ', data)
    rmtree(self.env_dir)
    builder = venv.EnvBuilder(prompt='My prompt')
    self.run_with_capture(builder.create, self.env_dir)
    context = builder.ensure_directories(self.env_dir)
    data = self.get_text_file_contents('pyvenv.cfg')
    self.assertEqual(context.prompt, '(My prompt) ')
    self.assertIn("prompt = 'My prompt'\n", data)
    rmtree(self.env_dir)
    builder = venv.EnvBuilder(prompt='.')
    cwd = os.path.basename(os.getcwd())
    self.run_with_capture(builder.create, self.env_dir)
    context = builder.ensure_directories(self.env_dir)
    data = self.get_text_file_contents('pyvenv.cfg')
    self.assertEqual(context.prompt, '(%s) ' % cwd)
    self.assertIn("prompt = '%s'\n" % cwd, data)

__author__ = 'Mike Solomon'
__author_email__ = '<mas63 @t cornell d0t edu>'
__version__ = '0.7.15'
__license__ = 'BSD License'

import imp
from compiler.util import Compiler, add_common_options

class Template(object):
    def __init__(self, txt):
        self.txt = txt
        self.tmp = None

    def __call__(self, namespaces=[], *args, **kwargs):
        if not hasattr(self.tmp, 'template'):
            self.compile()

        return self.tmp.template(search_list=namespaces).main()

    def compile(self, **kwargs):
        options = {'include_path': '.', 'verbose': False, 'optimizer_flags': [], 'extract_message_catalogue': False, 'message_catalogue_file': None, 'output_file': None, 'xspt_mode': False, 'output_directory': '', 'base_extends_package': None, 'locale': '', 'version': False, 'x_psyco': True, 'ignore_optional_whitespace': True, 'normalize_whitespace': False, 'tune_gc': None, 'function_registry_file': None, 'x_psyco_profile': None, 'enable_filters': True, 'optimizer_level': 0}
        options.update(kwargs)

        compiler_args = Compiler.args_from_optparse(options)
        compiler = Compiler(**compiler_args)

        self.tmp = imp.new_module('tmp')

        src = compiler.compile_template(self.txt, 'template')

        exec src in self.tmp.__dict__

        return self.tmp.template

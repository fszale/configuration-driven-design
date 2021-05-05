import importlib


class BuildProduct:

    taskconfig = None

    def start(self, config):

        self.taskconfig = config

        for key, value in config['tasks'].items():
            # Run each task in sequence
            print('\nRunning task: ' + key + '...')
            print('----------------------------------------------------')
            namesarr = value['implementation'].split('.')
            class_name = namesarr[len(namesarr) - 1]
            namesarr.pop()
            module_name = '.'.join(namesarr)

            module = importlib.import_module(module_name)
            class_ = getattr(module, class_name)
            instance = class_(value['params'])
            instance.process()
            print('----------------------------------------------------')

        pass

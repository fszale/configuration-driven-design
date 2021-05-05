import src.common.config
import importlib


class Product:

    parameters = None

    def __init__(self, params):
        self.parameters = params
        return

    def process(self):
        print('Process method called from ' + self.__class__.__name__)

        for rule in self.parameters['rules']:
            if rule['type'] == 'match':
                left = src.common.config.data[rule['left']]
                rightarr = rule['right'].split('.')

                for value in self.parameters['products']:
                    # find the right product to build
                    if left == value[rightarr[len(rightarr) - 1]]:
                        print('Found a match, building a ' + left + '...')

                        # load the product implementation and invoke process method
                        namesarr = value['implementation'].split('.')
                        class_name = namesarr[len(namesarr) - 1]
                        namesarr.pop()
                        module_name = '.'.join(namesarr)

                        module = importlib.import_module(module_name)
                        class_ = getattr(module, class_name)
                        instance = class_(value['params'])
                        instance.process()

        return

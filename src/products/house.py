class House:

    parameters = None

    def __init__(self, params):
        self.parameters = params
        return

    def process(self):
        print('Process method called from ' + self.__class__.__name__)
        print('\tBuilding this : ' + str(self.parameters))
        return

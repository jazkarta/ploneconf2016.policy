from plone import api
from plone.indexer.decorator import indexer
from plone.supermodel import model
from Products.Five import BrowserView

class ITrainingClass(model.Schema):
    model.load('models/training_class.xml')


class TrainingClassView(BrowserView):

    def instructors(self):
        """ parse instructor set into something template can iterate over
        """        
        instructor_set = self.context.instructor
        instructors = [x for x in instructor_set]
        # XXX get instructors out of set        

        return [{'url':'something', 'name' :'P5Nina'},
                {'url':'something2', 'name' :'P5Nick'}]

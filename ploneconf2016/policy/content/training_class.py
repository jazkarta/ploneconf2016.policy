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
        instructors = [api.content.get(UID=x) for x in instructor_set]
        instructor_data = []
        for x in instructors:
            instructor_data.append({'url':x.absolute_url(), 'name': x.title})
        return instructor_data

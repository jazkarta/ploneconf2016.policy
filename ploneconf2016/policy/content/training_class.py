from plone.indexer.decorator import indexer
from plone.supermodel import model
from Products.Five import BrowserView

class ITrainingClass(model.Schema):
    model.load('models/training_class.xml')


#class TrainingClassView(BrowserView):
#    pass

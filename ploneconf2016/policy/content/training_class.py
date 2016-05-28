from plone.indexer.decorator import indexer
from plone.supermodel import model


class ITrainingClass(model.Schema):
    model.load('models/training_class.xml')

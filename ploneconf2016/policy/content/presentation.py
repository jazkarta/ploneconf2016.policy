from plone import api
from plone.indexer.decorator import indexer
from plone.supermodel import model


class IPresentation(model.Schema):
    model.load('models/presentation.xml')

from plone.indexer.decorator import indexer
from plone.supermodel import model


class IPerson(model.Schema):
    model.load('models/person.xml')

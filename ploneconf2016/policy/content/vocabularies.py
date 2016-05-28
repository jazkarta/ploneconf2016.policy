from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

PRESENTATION_DURATION_TYPES = SimpleVocabulary(
    [SimpleTerm(value=u'LongTalk', title=u'Long Talk'),
     SimpleTerm(value=u'ShortTalk', title=u'Short Talk'),
     SimpleTerm(value=u'Demo', title=u'Demo')]
    )

TRAINING_CLASS_DURATION_TYPES = SimpleVocabulary(
    [SimpleTerm(value=u'TwoDay', title=u'2 day'),
     SimpleTerm(value=u'OneDay', title=u'1 day'),
     SimpleTerm(value=u'HalfDay', title=u'1/2 day')]
    )

LEVEL_TYPES = SimpleVocabulary(
    [SimpleTerm(value=u'Beginner', title=u'Beginner'),
     SimpleTerm(value=u'Intermediate', title=u'Intermediate'),
     SimpleTerm(value=u'Expert', title=u'Expert')]
    )

AUDIENCE_TYPES = SimpleVocabulary(
    [SimpleTerm(value=u'Integrator', title=u'Integrator'),
     SimpleTerm(value=u'Developer', title=u'Developer'),
     SimpleTerm(value=u'User', title=u'User')]
    )

from five import grok
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary


@grok.provider(IContextSourceBinder)
def social_button_code_ids(context):
    registry = getUtility(IRegistry)
    items = registry['hexagonit.socialbutton.codes']
    terms = []
    if items:
        for item in items:
            terms.append(SimpleVocabulary.createTerm(item, str(item), item))
    return SimpleVocabulary(terms)
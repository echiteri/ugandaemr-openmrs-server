import graphene

from core.database import Database

db = Database()


class PersonName(graphene.ObjectType):
    def __init__(self, **entries):
        self.__dict__.update(entries)

    id = graphene.ID()

    preferred = graphene.String()
    person = graphene.String()
    prefix = graphene.String()
    given_name = graphene.String()
    middle_name = graphene.String()

    family_name_prefix = graphene.String()
    family_name = graphene.String()
    family_name2 = graphene.String()
    family_name_suffix = graphene.String()

    degree = graphene.String()
    creator = graphene.String()
    date_created = graphene.String()
    voided = graphene.String()
    voided_by = graphene.String()

    date_voided = graphene.String()
    void_reason = graphene.String()
    changed_by = graphene.String()
    date_changed = graphene.String()
    uuid = graphene.String()

    facility = graphene.String()
    state = graphene.String()

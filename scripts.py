from datacenter.models import Mark
from datacenter.models import Schoolkid
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Subject
from datacenter.models import Commendation
from random import choice


class ObjectNotFoundError(BaseException):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"'{self.name}' is not found, check the spelling"


class ObjectTooMuchResultsError(BaseException):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Too much results for '{self.name}', expected 1"


def get_schoolkid(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        return schoolkid
    except Schoolkid.DoesNotExist:
        raise ObjectNotFoundError(schoolkid_name)
    except Schoolkid.MultipleObjectsReturned:
        raise ObjectTooMuchResultsError(schoolkid_name)


def fix_marks(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for bad_mark in bad_marks:
        bad_mark.points = 5
        bad_mark.save()


def remove_chastisements(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(schoolkid_name, subject_name, commendation_text="Хвалю!"):
    schoolkid = get_schoolkid(schoolkid_name)
    try:
        subject = Subject.objects.get(title__contains=subject_name, year_of_study=schoolkid.year_of_study)
    except Subject.DoesNotExist:
        raise ObjectNotFoundError(subject_name)
    except Subject.MultipleObjectsReturned:
        raise ObjectTooMuchResultsError(subject_name)
    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject=subject
    ).order_by("?").first()
    commendation = Commendation.objects.create(
        text=commendation_text,
        created=lesson.date,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher
    )

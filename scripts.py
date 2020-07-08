from datacenter.models import Mark
from datacenter.models import Schoolkid
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Subject
from datacenter.models import Commendation
from random import choice


class SchoolkidNotFoundError(BaseException):
    def __init__(self, schoolkid_name):
        self.schoolkid_name = schoolkid_name

    def __str__(self):
        return f"'{self.schoolkid_name}' is not found, check the spelling"


class SchoolkidTooMuchResultsError(BaseException):
    def __init__(self, schoolkid_name):
        self.schoolkid_name = schoolkid_name

    def __str__(self):
        return f"Too much results for '{self.schoolkid_name}, expected 1'"


class SubjectNotFoundError(BaseException):
    def __init__(self, subject_name):
        self.subject_name = subject_name

    def __str__(self):
        return f"'{self.subject_name}' is not found, check the spelling"


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
        subject = Subject.objects.get(title=subject_name, year_of_study=schoolkid.year_of_study)
    except Subject.DoesNotExist:
        raise SubjectNotFoundError(subject_name)
    lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject=subject
    )
    lesson = choice(lessons)
    commendation = Commendation.objects.create(
        text=commendation_text,
        created=lesson.date,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher
    )

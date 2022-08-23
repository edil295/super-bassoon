from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100)
    month_to_learn = models.IntegerField()

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class AbstractPerson(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100)

    class Meta:
        abstract =True

    def save(self, *args, **kwargs):
        if self.phone_number[0] == '0':
            s = self.phone_number
            s = s.replace(s[0], '')
            self.phone_number = f'+996{s}'
        else:
            self.phone_number = self.phone_number
        super().save(*args, **kwargs)


class Student(AbstractPerson):
    work_study_place = models.CharField(max_length=100, null=True, blank=True)
    has_own_notebook = models.BooleanField()
    preferred_os = models.CharField(max_length=100, choices=[('windows', 'Windows'),
                                                             ('macos', 'MacOs'),
                                                             ('linux', 'linux')])

    def __str__(self):
        return self.name


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=100, null=True, blank=True)
    experience = models.DateField()
    cour = models.ManyToManyField(Student, through='Course')

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


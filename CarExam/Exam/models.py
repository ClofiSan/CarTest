# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Examine(models.Model):
    id = models.BigIntegerField(primary_key=True)
    em_in = models.CharField(max_length=16)
    em_pwd = models.CharField(max_length=16, blank=True, null=True)
    student = models.ForeignKey('Student', models.DO_NOTHING, db_column='student')
    answer = models.CharField(max_length=254, blank=True, null=True)
    score = models.BigIntegerField(blank=True, null=True)
    paper = models.ForeignKey('Paper', models.DO_NOTHING, blank=True, null=True)
    em_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'examine'


class Paper(models.Model):
    paper_id = models.BigIntegerField(primary_key=True)
    question_id_seq = models.CharField(max_length=1200)
    key_seq = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paper'


class Question(models.Model):
    question_id = models.BigIntegerField(primary_key=True)
    question_body = models.CharField(max_length=254, blank=True, null=True)
    question_form = models.CharField(max_length=1, blank=True, null=True)
    branch_a = models.CharField(max_length=254, blank=True, null=True)
    branch_b = models.CharField(max_length=254, blank=True, null=True)
    branch_c = models.CharField(max_length=254, blank=True, null=True)
    pic_name = models.CharField(max_length=50, blank=True, null=True)
    question_key = models.CharField(max_length=1, blank=True, null=True)
    question_type_id = models.BigIntegerField(blank=True, null=True)
    question_mark = models.BigIntegerField(blank=True, null=True)
    question_sts = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question'


class Student(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    pin = models.CharField(max_length=32, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class Users(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    user_name = models.CharField(max_length=10, blank=True, null=True)
    login_name = models.CharField(max_length=10)
    password = models.CharField(max_length=32)
    user_type = models.CharField(max_length=1)
    sts = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'users'

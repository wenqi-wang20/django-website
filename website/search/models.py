from django.db import models

# Create your models here.


# class User(models.Model):
#     email = models.EmailField(unique=True, max_length=128)
#     password = models.CharField(max_length=64)
#     c_time = models.DateTimeField(auto_now_add=True)
#     ip = models.CharField(max_length=50,null=True)
#
#     def __str__(self):
#         return self.email
#
#     class Meta:
#         ordering = ['-c_time']
#         verbose_name = "用户"
#         verbose_name_plural = "用户"
#
# class HotSpot(models.Model):
#     word = models.CharField(max_length=100,unique=True)
#     count = models.IntegerField(default=0)
#     class Meta:
#         ordering = ['-count']
#         verbose_name = "热搜"
#         verbose_name_plural = "热搜"
#     def __str__(self):
#         return self.word

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CaptchaCaptchastore(models.Model):
    id = models.BigAutoField(primary_key=True)
    challenge = models.CharField(max_length=32)
    response = models.CharField(max_length=32)
    hashkey = models.CharField(unique=True, max_length=40)
    expiration = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'captcha_captchastore'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Poem(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    model_name = models.CharField(max_length=50, blank=True, null=True)
    poem_name = models.CharField(max_length=50, blank=True, null=True)
    author_name = models.CharField(max_length=50, blank=True, null=True)
    dynasty = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poem'


class SearchHotspot(models.Model):
    id = models.BigAutoField(primary_key=True)
    word = models.CharField(unique=False, max_length=100)
    count = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'search_hotspot'


class SearchUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=64)
    c_time = models.DateTimeField()
    ip = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_user'

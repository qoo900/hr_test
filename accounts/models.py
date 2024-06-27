from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, email, name, comingday, organization, department, team, level, phonenumber, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            comingday=comingday,
            organization=organization,
            department=department,
            team=team,
            level=level,
            phonenumber=phonenumber,  
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, comingday, organization, department, team, level, phonenumber, password):
        user = self.create_user(
            email,
            name=name,
            password=password,
            comingday=comingday,
            organization=organization,
            department=department,
            team=team,
            level=level,
            phonenumber=phonenumber,  
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(verbose_name='name', max_length=30)
    
    comingday = models.DateField()
    
    organization = models.CharField(verbose_name='organization', max_length=30)
    department = models.CharField(verbose_name='department', max_length=30)
    team = models.CharField(verbose_name='team', max_length=30)
    level = models.CharField(verbose_name='level', max_length=30)
    phonenumber = models.CharField(verbose_name='phonenumber', max_length=30)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'comingday', 'organization', 'department', 'team', 'level', 'phonenumber']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail

# model managers
class MyUserManager(BaseUserManager):
  def create_user(self, email, first_name, last_name, password=None):
    if not email:
      raise ValueError('Email address must be provided for user account')
    if not first_name:
      raise ValueError('A first name must be provided')
    if not last_name:
      raise ValueError('A last name must be provided')

    user = self.model(
      email=self.normalize_email(email),
      first_name=first_name,
      last_name=last_name,
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, first_name, last_name, password=None):
    user = self.create_user(
      email,
      password=password,
      first_name=first_name,
      last_name=last_name,
    )
    user.is_staff = True
    user.is_admin = True
    user.save(using=self._db)
    return user


# models
class User(AbstractBaseUser):
  email = models.EmailField(blank=False, null=False)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  date_of_birth = models.DateField(verbose_name="DOB", blank=True, null=True)
  phone = models.CharField(max_length=11, blank=True, null=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_admin = models.BooleanField(default=False)


  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']
  EMAIL_FIELD = 'email'

  objects = MyUserManager()

  def get_full_name(self):
    full_name = f"{self.first_name} {self.last_name}"
    return full_name.strip()

  def get_short_name(self):
    return f"{self.first_name}"


  def __str__(self):
    return self.email

  def has_perm(self, perm, obj=None):
    return True

  def has_module_perms(self, app_label):
    return True


  def email_user(self, subject, message, from_email=None, **kwargs):
    send_mail(subject, message, from_email, [self.email], **kwargs)



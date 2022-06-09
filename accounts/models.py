from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.postgres.fields import CICharField, CIEmailField
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model




class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    username_validator = ASCIIUsernameValidator()

    # _________   Fields   _________ 

    username = CICharField(_("username"), max_length=150, unique=True, help_text=_("Required. 150 charactars or less. Letters, digits and @/./+/-/_ only."), validators=[username_validator], error_messages={"unique":_("A user with that username already exists."),},)

    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    
    email = CIEmailField(_("email address"), unique=True, error_messages={"unique":"A user with this email already exists",},)
    
    is_staff = models.BooleanField(_("staff status"), default=False, help_text=_("Designates whether the user can log into this admin site."),)
    
    is_active = models.BooleanField(_("active"), default=True, help_text=_("Designates whether this user shoyld be treated as active. Ucheck this instead of deleting"),)

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)


    # ______________________

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]


    # ______________________
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
    
    # ______________________

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
    
    def get_full_name(self):

        """
        Return the first_name and last_name , with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """ Returns the short name for the user """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **Kwargs):
        """ Send an email to this user """
        send_mail(subject, message, from_email, [self.email], **Kwargs)




#----------------------------------------------------------
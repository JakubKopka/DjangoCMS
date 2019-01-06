from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="Użytownik", on_delete=models.CASCADE)
    country = models.CharField(max_length=150, verbose_name="Kraj")
    date_of_birth = models.DateField(verbose_name="Data urodzenia", null=True)

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profile"

        def __str__(self):
            return str(self.title)

    def __unicode__(self):
        return self.title


User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])


@receiver(post_save, sender=User)
def add_user_profile_on_user_created(sender, **kwargs):
    if kwargs.get('created', False):
        userprofile = Profile.objects.create(user=kwargs.get('instance'))

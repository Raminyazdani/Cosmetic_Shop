from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CostumeBaseUserManager(BaseUserManager):
    use_in_migrations = True

    def save_user(self, phone_number, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not phone_number:
            raise ValueError(_('The given phone number must be set'))
        phone_number = phone_number[-10:]
        extra_fields["slug"]=phone_number
        user = self.model(phone_number=phone_number, **extra_fields)

        # Call this method for password hashing
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password, **extra_fields):
        extra_fields['is_superuser'] = False
        extra_fields['is_staff'] = False
        phone_number = phone_number[-10:]
        extra_fields["slug"] = phone_number
        return self.save_user(phone_number, password, **extra_fields)

    # Method called while creating a staff user
    def create_staffuser(self, phone_number, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = False
        phone_number = phone_number[-10:]
        extra_fields["slug"] = phone_number
        return self.save_user(phone_number, password, **extra_fields)

        # Method called while calling creatsuperuser

    def create_superuser(self, phone_number, password, **extra_fields):

        # Set is_superuser parameter to true
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser should be True')

        extra_fields['is_staff'] = True
        phone_number = phone_number[-10:]
        extra_fields["slug"] = phone_number
        return self.save_user(phone_number, password, **extra_fields)

    def get_queryset(self):
        """
        return all objects that is not deleted
        :return:
        """
        return super().get_queryset().filter(is_delete=False)

    def get_all(self):
        """
        return all objects including deleted objects
        :return:
        """
        return super().get_queryset()

    def get_deleted(self):
        """
        return all deleted objects
        :return:
        """
        return super().get_queryset().filter(is_delete=True)

    def delete(self):
        """
        soft delete objects
        :return:
        """
        return self.update(is_delete=True)

    def restore(self):
        """
        restore soft deleted objects
        :return:
        """
        return self.update(is_delete=False)

    def hard_delete(self):
        """
        hard delete objects
        :return:
        """
        return super().get_queryset().delete()

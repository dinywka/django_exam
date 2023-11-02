from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(verbose_name="Автор", to=User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=300, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение", upload_to="images/products", default=None, null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Активность поста", default=True)
    date_time = models.DateTimeField(default=now, verbose_name="Дата и время подачи")

    class Meta:
        app_label = "blog_app"
        ordering = ("-is_active", "title")
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f"<Post {self.title} {self.author.username}>"

class Comment(models.Model):
    post = models.ForeignKey(to=Post, verbose_name="К какому посту", max_length=200, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, verbose_name="Автор", max_length=200, on_delete=models.CASCADE)  # +-
    text = models.TextField("Текст комментария", default="")
    date_time = models.DateTimeField("Дата и время создания", default=now)

    class Meta:
        app_label = "blog_app"
        ordering = ("-date_time", "post")
        verbose_name = "Комментарий к посту"
        verbose_name_plural = "Комментарии к постам"

    def __str__(self):
        return f"{self.date_time} {self.author.username} {self.post.title} {self.text[:20]}"

class UserProfile(models.Model):
    user = models.OneToOneField(
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name="Модель пользователя",
        help_text='<small class="text-muted">Тут лежит "ссылка" на модель пользователя</small><hr><br>',
        to=User,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    avatar = models.ImageField(verbose_name="Аватарка", upload_to="users/avatars", default="https://vk-wiki.ru/wp-content/uploads/2019/04/male-user-profile-picture.png", null=True, blank=True)

    class Meta:
        app_label = "auth"
        ordering = ("-user", "avatar")
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"

    def __str__(self):
        return f"<UserProfile {self.user.username}>"




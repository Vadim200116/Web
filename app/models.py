from django.db import models


class Question(models.Model):
    author = models.ForeignKey('Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    pub_date=models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    author = models.ForeignKey('Profile', on_delete=models.CASCADE)
    question=models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.TextField()
    pubdate=models.DateField()



    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Tag (models.Model):
    value=models.CharField(max_length=255)
    question=models.ForeignKey('Question', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural ='Теги'

    def __str__(self):
        return self.value

class User(models.Model):
    name=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    email=models.CharField(max_length=255)

    

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name

        

class Profile (models.Model):
    avatar=models.CharField(max_length=255)
    user=models.OneToOneField('User', on_delete=models.CASCADE) 

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.avatar


class QuestionRating(models.Model):
    author=models.ForeignKey('Profile', on_delete=models.CASCADE)
    value=models.IntegerField()

    

    class Meta:
        verbose_name = 'Оценка вопроса'
        verbose_name_plural = 'Оценки вопроса'

    def __str__(self):
        return self.value

class AnswerRating(models.Model):
    author=models.ForeignKey('Profile', on_delete=models.CASCADE)
    value=models.IntegerField()

    

    class Meta:
        verbose_name = 'Оценка ответа'
        verbose_name_plural = 'Оценки ответа'

    def __str__(self):
        return self.value



   



    

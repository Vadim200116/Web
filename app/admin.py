from django.contrib import admin
from app.models import Question,Answer,Tag,User,Profile,QuestionRating,AnswerRating
# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(QuestionRating)
admin.site.register(AnswerRating)
from django.db import models

class Authors(models.Model):
    name = models.CharField("Имя автора", max_length=50)
    surname = models.CharField("Имя автора", max_length=50)
    cit = models.CharField("Гражданство", max_length=50)
    birthday = models.DateField("Дата рождения автора")


    def __str__(self):
        return format(self.surname)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Pub_house(models.Model):
    name = models.CharField("Название издательства", max_length=50)
    country = models.CharField("Страна",max_length=50)

    def __str__(self):
        return format(self.name)

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"

class Books (models.Model):
    name = models.CharField("Название книги",max_length=50)
    num_page = models.IntegerField("Количество страниц")
    seria = models.CharField("Серия книги",max_length=50,null=True)
    id_a = models.ForeignKey(Authors,on_delete=models.CASCADE)
    id_ph = models.ForeignKey(Pub_house,on_delete=models.CASCADE)

    def __str__(self):
        return format(self.name)


    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
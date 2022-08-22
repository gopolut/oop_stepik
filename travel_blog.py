# Объявите класс с именем TravelBlog и объявите в нем атрибут:
# total_blogs: 0
# Создайте экземпляр этого класса с именем tb1, сформируйте в нем два локальных свойства:
# tb1.name = 'France'
# tb1.days = 6
# Увеличьте значение атрибута total_blogs класса TravelBlog на единицу.

class TravelBlog:
    total_blogs: int = 0

if __name__ == '__main__':
    tb1 = TravelBlog()

    tb1.name = 'France'
    tb1.days = 6
    TravelBlog.total_blogs += 1

    tb2 = TravelBlog()
    tb2.name = 'Italy'
    tb2.days = 5
    TravelBlog.total_blogs += 1
    print(TravelBlog.total_blogs)

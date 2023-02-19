# Список всех комманд, запускаемых в Django shell:

# 1. Создание двух пользователей (с помощью метода User.objects.create_user('username')):

u1 = User.objects.create_user(username='Dukov')
u2 = User.objects.create_user(username='Nikita')
u3 = User.objects.create_user(username='Anton')

# 2. Создание двух объектов модели Author, связанных с пользователями:

Author.objects.create(authorUser=u1)
Author.objects.create(authorUser=u2)
Author.objects.create(authorUser=u3)

# 3. Добавление 4 категорий в модель Category:

Category.objects.create(name='psychiatry')
Category.objects.create(name='headache')
Category.objects.create(name='cold')
Category.objects.create(name='drugs')
Category.objects.create(name='neurology')

# 4. Добавление двух статей и одной новости:

author = Author.objects.get(id=1)
Post.objects.create(author=author, categoryType='NW', title='Encyclopatia',
                    text='The project has its own bar in St. Petersburg! EBM.BAR '
                         'Encyclopatia is like an encyclopedia, only an encyclopatia: '
                         'a pathological encyclopedia.')

author = Author.objects.get(id=2)
Post.objects.create(author=author, categoryType='AR', title='Primary headache',
                    text='Primary headache is the second most common disease in the world, '
                         'poisoning the lives of millions of people. This part of the article '
                         'will focus on the most common headaches - primary, of all headaches, '
                         '80% are tension headaches and 15% are migraines, and 5% are all other rare things.')

author = Author.objects.get(id=2)
Post.objects.create(author=author, categoryType='AR', title='SARS',
                    text='The common cold is a non-medical laymans term for two unrelated conditions. '
                         'However, both of them are infections. An acute respiratory viral infection or ARI '
                         'is what you get sick with every autumn and spring, sometimes its the flu.')

# 5. Присвоение им категории (в одной статье д.б. не < 2 категорий):

Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=2))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=3))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=5))

# 6. Создание 4 комментариев к разным объектам модели Post:

Comment.objects.create(commentPost=Post.objects.get(id=1),
                       commentUser=Author.objects.get(id=2).authorUser,
                       text='Cool project! Good luck!')

Comment.objects.create(commentPost=Post.objects.get(id=2),
                       commentUser=Author.objects.get(id=1).authorUser,
                       text='Great start! Very useful information, allows patients to be literate in this matter.')

Comment.objects.create(commentPost=Post.objects.get(id=3),
                       commentUser=Author.objects.get(id=1).authorUser,
                       text='Colleague, keep going! Everyone needs to know this.')

Comment.objects.create(commentPost=Post.objects.get(id=3),
                       commentUser=Author.objects.get(id=3).authorUser,
                       text='I disagree! Provide links to research!')

# 7. Корректирование рейтингов этих объектов, применяя функции like() и dislike() к статьям/новостям и комментариям:

Post.objects.get(id=1).like()
Post.objects.get(id=3).dislike()
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).dislike()

# 8. Обновление рейтингов пользователей:

Author.objects.get(id=1).update_rating()
Author.objects.get(id=1).ratingAuthor

Author.objects.get(id=2).update_rating()
Author.objects.get(id=2).ratingAuthor

Author.objects.get(id=3).update_rating()
Author.objects.get(id=3).ratingAuthor

# 9. Вывод username и рейтинга лучшего пользователя (применяя сортировку и возвращая поля первого объекта):

a = Author.objects.order_by('-ratingAuthor')[:1]
for i in a:
    i.ratingAuthor
    i.authorUser.username

# 10. Вывод даты добавления, username автора, рейтинга, заголовка и превью лучшей статьи,
#     основываясь на лайках/дислайках к этой статье:

b = Post.objects.order_by('-rating')[:1]
for i in b:
    i.author.authorUser.date_joined
    i.author.authorUser.username
    i.rating
    i.title
    i.preview()


# 11. Вывод всех комментариев (дата, пользователь, рейтинг, текст) к этой статье:

c = Comment.objects.all()
for i in c:
    i.dateCreation
    i.commentUser
    i.rating
    i.text

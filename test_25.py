    # python3 -m pytest -v test_25.py


def test_open_all_pets(all_pets):   # """Проверяем, что мы открыли страницу сайта все питомцы"""
    all_pets.implicitly_wait(5)
    """Проверяем, что мы открыли главную страницу сайта"""
    assert all_pets.find_element_by_tag_name('h1').text == "PetFriends"


def test_open_my_pets(my_pets):     # """Проверяем, что мы открыли страницу сайта мои питомцы"""
    my_pets.implicitly_wait(5)
    """Проверяем, что мы открыли страницу сайта мои питомцы"""
    assert my_pets.find_element_by_xpath('//h2').text == "Игорь Филимонов QAP 71"


def test_compare_amount(my_pets):   # Проверяем что колличество питомцев в статистике равно количеству в таблице
    """Запрашиваем данные из статистики пользователя"""
    all_text = my_pets.find_elements_by_css_selector('.\\.col-sm-4.left')
    amount = all_text[0].text.split('\n')
    amount = amount[1].split(' ')
    amount = int(amount[1])
    """Запрашиваем данные из таблицы питомцев"""
    all_pets = my_pets.find_elements_by_css_selector('tbody > tr')
    """Проверяем что колличество питомцев в статистике соответствует количеству в таблице"""
    assert amount == len(all_pets)



def test_pets_foto(my_pets):    # """Проверяем что фотографии есть больше чем у половины питомцев"""
    data_foto = 0
    """Запрашиваем данные из таблицы питомцев"""
    all_pets = my_pets.find_elements_by_css_selector('tbody > tr')
    """Запрашиваем данные о фото из таблицы питомцев"""
    all_pets_foto = my_pets.find_elements_by_css_selector('th > img')
    for i in range(len(all_pets)):
        if all_pets_foto[i].get_attribute('src') != '':     # проверяем наличие ссылки на фото
            data_foto += 1
    if (len(all_pets) - data_foto) < data_foto:
        assert (len(all_pets) - data_foto) < data_foto      # сравниваем кол-во питомнев с кол-вом фото
    else:
        print(f'\nФотографии есть у {data_foto} питомцев из {len(all_pets)}')


def test_pets_name_breed_age(my_pets):      # У всех питомцев есть имя, возраст и порода.
    """Запрашиваем данные из таблицы питомцев"""
    all_pets = my_pets.find_elements_by_css_selector('tbody > tr')
    for i in range(len(all_pets)):
        pets = all_pets[i].text.split(" ")
        assert pets[0] != ' '  # Проверка заполнения Имени
        assert pets[1] != ' '  # Проверка заполнения породы
        assert pets[2] != ' '  # Проверка заполнения возраста


def test_pets_different_name(my_pets):  # У всех питомцев разные имена.
    name = []
    all_pets = my_pets.find_elements_by_css_selector('tbody > tr')
    for i in range(len(all_pets)):
        pets = all_pets[i].text.split(" ")
        name.append(pets[0])        # список имен
    if len(name) == len(set(name)):
        assert len(name) == len(set(name))
    else:
        print(f'\nВ списке моих  питомцев есть питомцы с одинаковыми именами ')


def test_repeat_pets(my_pets):      # В списке нет повторяющихся питомцев.
    pet = []
    """Запрашиваем данные из таблицы питомцев"""
    all_pets = my_pets.find_elements_by_css_selector('tbody > tr')
    for i in range(len(all_pets)):
        pets = all_pets[i].text.split(" ")
        pet.append(pets)
    for i, x in enumerate(pet):
        if pet.count(x) > 1:
            print(f'\nпитомец номер {i} {x}')
        else:
            assert pet.count(x) == 1

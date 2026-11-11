from jinja2 import Environment, FileSystemLoader, select_autoescape
import random
import os


def main():
    os.makedirs("cards",exist_ok=True)
    cards=int(input("сколько карточек хотите добавить: "))
    for number in range(cards):
        env = Environment(
            loader=FileSystemLoader('.'),
            autoescape=select_autoescape(['html'])
        )
        template = env.get_template('template.html')
        character_name=input("введите имя вашего персонажа: ")
        races=["человек","орк","гном","эльф"]
        character_race=int(input("выберите рассу 1-человек 2-орк 3-гном 4-эльф: "))
        classes=["лучник","убийца","бард","воин","маг"]
        character_class=int(input("выберите класс 1-лучник 2-убийца 3-бард 4-воин 5-маг: "))
        clases_base={
            "лучник" : {
                "skills": ['Верный выстрел', 'Чародейский выстрел', 'Стенающая стрела', 'Стрелы ветра', 'Призыв питомца', 'Глаз зверя', 'Осветительная ракета', 'Приручение животного'],
                "strength" : random.randint(1,3),
                "agility" : 15,
                "intelligence" : random.randint(1,3),
                "luck" : random.randint(1,3),
                "temper" : random.randint(1,3),
                "image" : "../images/archer.png"
            },
            "убийца" : {
                "skills": ['Отравление', 'Взлом замка', 'Подлый трюк', 'Исчезновение', 'Ложный выпад', 'Внезапный удар', 'Ошеломление', 'Спринт'],
                "strength" : random.randint(1,3),
                "agility" : random.randint(1,3),
                "intelligence" : random.randint(1,3),
                "luck" : 15,
                "temper" : random.randint(1,3),
                "image" : "../images/assasin.png"
            },
            "бард" : {
                "skills": ['Аккорды ветра', 'Аккорды воды', 'Исцеление', 'Соната жизни', 'Пауза', 'Плач сирен', 'Песнь ветра', 'Реквием'],
                "strength" : random.randint(1,3),
                "agility" : random.randint(1,3),
                "intelligence" : random.randint(1,3),
                "luck" : random.randint(1,3),
                "temper" : 15,
                "image" : "../images/bard.webp"
            },
            "воин" : {
                "skills": ['Блок щитом', 'Казнь', 'Рывок', 'Боевой крик', 'Вихрь', 'Парирование', 'Мощный удар', 'Глубокие раны'],
                "strength" : 15,
                "agility" : random.randint(1,3),
                "intelligence" : random.randint(1,3),
                "luck" : random.randint(1,3),
                "temper" : random.randint(1,3),
                "image" : "../images/warrior.png"
            },
            "маг" : {
                "skills": ['Стрела ледяного огня', 'Снятие проклятия', 'Огненный взрыв', 'Обледенение', 'Ледяное копье', 'Конус холода', 'Прилив сил', 'Морозный доспех'],
                "strength" : random.randint(1,3),
                "agility" : random.randint(1,3),
                "intelligence" : 15,
                "luck" : random.randint(1,3),
                "temper" : random.randint(1,3),
                "image" : "../images/wizard.png"
            }
        }
        character_skills=random.sample(clases_base[classes[character_class-1]]["skills"],3)
        rendered_page = template.render(
            name=character_name,
            race=races[character_race-1],
            character_class=classes[character_class-1],
            strength=clases_base[classes[character_class-1]]["strength"],
            agility=clases_base[classes[character_class-1]]["agility"],
            intelligence=clases_base[classes[character_class-1]]["intelligence"],
            luck=clases_base[classes[character_class-1]]["luck"],
            temper=clases_base[classes[character_class-1]]["temper"],
            image=clases_base[classes[character_class-1]]["image"],
            first_skill=character_skills[0],
            second_skill=character_skills[1],
            third_skill=character_skills[2]
        )
        with open(f'cards/index{number+1}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__=="__main__":
    main()
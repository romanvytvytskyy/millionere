#                                                 lewel 1
from random import randint

from numpy import correlate
lewel_1 = [["Яка Фамілія в головного героя в 'Гусяччі історії'", "Макдак", "Макшмяк", "Макхряк", "Бігмак"],
           ["У якому році `Титанік` затонув в Атлантичному океані",
               "14 квітня 1912", "26 червня 1945", "20 липня 1832", "30 жовтня 2020"],
           ["Як називається перший в історії фільм `Carry On`, зроблений та випущений у",
               "1958", "1985", "1823", "1990"],
           ["де знаходиця найбільша технологічна компанія в Південій Кореї",
            "Samsung", "Xiomi", "aplle", "msi"],
           ["Який співак виступав у естрадній колективі Showaddywaddy 1970-х?",
            "Дейв Бартрам", "Базилевич Федір", "Іво Бобул", "Бичук Микола Андрійович"],
           ["Який тепер відомий теле шеф-кухар почав готувати у віці восьми років у пабі своїх батьків `Крикери`, у Клаверінгу, Ессекс?",
            "Джеймі Олівер", "Василий Емельяненко", "Нусрет Гьокче", "Магдалина Гесслер"],
           ["Який голландський гравець у дартс виграв чемпіонат світу з BDO 2012 року в сільському клубі Lakeside, Frimley Green, 15 січня?",
            "Крістіан Кіст", "Алі Парвін", "Ісмаїль Рашид", "Зухаїр Бахіт"],
           ["Який метал був відкритий Гансом Крістіаном Ерстедом у 1825 році?",
            "алюміній", "залізо", "золото", "бронза"],
           ["Яка столиця Португалії?", "Лісабон", "Київ", "Москва", "Лондон"],
           ["Скільки вдихів щодня робить людський організм",
            "20,000", "15,000", "40,000", "100,000"],
           ["Хто був прем'єр-міністром Великобританії з 1841 по 1846 рік?",
            "Роберт Піл", "Володимир Гройсман", "Олексій Гончарук", "Денис Шмигаль"],
           ["Хто винайшов Котячі очі в 1934 році для поліпшення безпеки дорожнього руху?",
            "Персі Шоу", "Ілон Маск", "Тарас Шевченко", "Теодора Драйзера"],
           ["Що таке хімічний символ для срібла?", "Ag", "Co2", "De", "Li"],
           ["Який найменший у світі птах?", "колібрі", "Ворона", "голуб", "синиця"],
           ["Хто грав «Боді» та «Дойла» в «Професіоналах»?", "Льюїс Коллінз та Мартін Шоу", "Мартін Шоу", "Льюїс Коллінз", "Тарас Шевченко"]]
#                                                 lewel2
lewel_2 = [["Що таке лялька, Барбі, повне ім'я?", "Барбара Робертс", "Барбара Дуранд", "Барбара Колінз", "Барбара Бартрам"],
           ["Для чого Пол Ханн утримує рекорд, який", "Найгучніша відрижка",
               "Найгучніше пердіня", "Нагучніший голос", "Найгучніше ходьба"],
           ["Якою візитною карткою Аль Капоне було його заняття?", "Продавець вживаних меблів",
               "Продавець техніки", "Продавець продуктів першої потрібності", "Продавець кофе"],
           ["Яка тривалість життя бабусі?", "24 години",
            "24 роки", "50 років", "15 років"],
           ["Який рік був зроблений перший вантажівка Тонка ",
            "1947", "1957", "1946", "1840"],
           ["Хто винайшов консервну банку для консервування їжі в 1810 році?",
            "Пітер Дуранд", "Пітер Монгерштерн", "Пітер Путін", "Пітер Гуган"],
           ["У якому році було вперше випущено Хрещеного батька?",
            "1947", "1964", "1920", "1990"],
           ["Який актор здобув найкращого актора «Оскар» за фільми «Філадельфія» (1993) та «Форест Гамп» (1994)?",
            "Том Хенкс", "Том Керсин", "Том Бокун", "Том Сліпенчук"],
           ["Скільки самореференційних камер створив Альфред Хічкок у своїх фільмах 1927-1976 рр. ",
            "37", "46", "15", "49"],
           ["Яка актриса зіграла Мері Поппінс у фільмі 1964 року Мері Поппінс?",
            "Джулі Ендрюс", "Джулі Шевченко", "Джулі Хенкс", "Джулі Макшмяк"],
           ["У якому класичному фільмі 1963 року з'явився Чарльз Бронсон?", "The Great Escape",
            "Grand Theft auto", "Grand Theft auto white citi", "Grand Theft auto San Adreas"],
           ["В якому фільмі 1995 року Сандра Баллок зіграла героїню Анжелу Беннетт - боротьба Ернеста Хемінгуея, Мережа",
            "Чистий", "Грязний", "Сирий", "Молодий"],
           ["Яка новозеландська режисерка зняла ці фільми - In the Cut (2003), The Water Diary (2006) та Bright Star (2009)?",
            "Джейн Кемпіон", "Джейн Шарайобов", "Джейн Гулд", "Джейн Стетмен"],
           ["Який актор забезпечив голос герою Немо у фільмі 2003 року в пошуку Немо?",
            "Олександр Гулд", "Олександр Білак", "Олександр Гамп", "Олександр Бронсон"],
           ["Про якого ув'язненого, якого охрестили найжорстокішим в'язнем у Великобританії, `було предметом фільму 2009 року?`", "Чарльз Бронсон", "Чарльз Стетхем", "Чарльз Рурль", "Чарльз Рурк"]]
#                                                 lewel3
lewel_3 = [["Про якого ув'язненого, якого охрестили найжорстокішим в'язнем у Великобританії`, було предметом фільму 2009 року?", "Чарльз Бронсон", "Чарльз Рурль", "Чарльз Рурк", "Чарльз Стетхем"],
           ["Американська актриса, яка зіграла роль боса підземного світу Токіо О-Рен Ішіі у фільмі KillBill Vol I & II",
               "Lucy Liu", "Lucy Lau", "Lucy Lyu", "Lucy Lou"],
           ["У якому фільмі зіграв Х'ю Джекман як суперник-маг героя, якого зіграв Крістіан Бейл?",
               "Престиж", "Престиж Білак", "Престиж Рурк", "Престиж Лайн"],
           ["У якій середземноморській країні народився режисер Френк Капра, відомий фільмом Це прекрасне життя?",
            "Карен Гіллан", "Карен Гіллен", "Карен Гіллін", "Карен Галлан"],
           ["Який британський актор відіграв роль Лі Різдва разом із Сільвестром Сталлоне у фільмі `Витратні`?",
            "Джейсон Стетхем", "Джейсон Стетхум", "Джейсон Стетхам", "Джейсон Статхем"],
           ["Який американський актор знявся разом з Кім Бассінгер у фільмі 9½ тижні?",
            "Міккі Рурк", "Міккі Рарк", "Міккі Рирк", "Міккі Рерк"],
           ["Яка колишня актриса Doctor Who зіграла роль Туманності у фільмі `Месники: Війна нескінченності`?",
            "Карен Гіллан", "Карен Галлан", "Карен Гиллан", "Карен Геллан"],
           ["Хто знявся у ролі Юнони МакГуфф проти Майкла Сера у фільмі «Юнона» 2007 року?",
            "Еллен Пейдж / Елліот Пейдж", "Еллин Пейдж / Елліот Пийдж", "Еллен Пейдж", "Елліот Пейдж"],
           ["Де американська команда з бейсболу Tampa Bay Rays проводить свої домашні ігри?",
            "Поле Тропікана", "Поле Тропіка", "Поле Тропікина", "Поле Тропікена"],
           ["Вперше відбувся в 1907 році, в якому виді спорту змагався Кубок Ватерлоо?", "Коронкові зелені миски",
            "Коронкові зелені сосіски", "Коронкові зелені огрки", "Коронкові зелині мески"],
           ["Хто був BBC «Спортивна особистість року» у 2001 році?",
            "Девід Бекхем", "Девід Бикхим", "Девід Бекхим", "Девід Бикхем"],
           ["Де проводились Ігри Співдружності в 1930 році?", "Гамільтон, Канада",
            "Гамільтон, Україна", "Гамільтон, Італія", "Гамільтон, Америка"],
           ["Скільки гравців у команді з водного поло?", "7", "13", "14", "8"],
           ["Яким видом спорту відзначився Ніл Адамс?",
            "Дзюдо", "Паркур", "Баскетбол", "Футбол"],
           ["Яка країна виграла Кубок світу в Іспанії 1982 року, перемігши Західну Німеччину 3-1?", "Italy", "Ukriane", "Amerika", "Korea"]]

cash_list = [0, 100, 200, 300, 500, 1000, 2000, 4000, 8000,
             16000, 32000, 64000, 125000, 250000, 500000, 1000000]


class Show_Quesion():
    def __init__(self, level1, level2, level3):
        self.level1 = level1
        self.level2 = level2
        self.level3 = level3
        self.player_level = 1
        self.true_answers = 0

    def get_question(self):
        if self.player_level == 1:
            q_index = randint(0, len(self.level1))
            return self.level1[q_index]
        elif self.player_level == 2:
            q_index = randint(0, len(self.level1))
            return self.level1[q_index]
        elif self.player_level == 3:
            q_index = randint(0, len(self.level1))
            return self.level1[q_index]
        else:
            print("end")

    def set_question(self):
        q = self.get_question()
        correct = q[1]
        response = [q, correct]
        return response

    def setcash(self):
        global cash_list
        text_money = cash_list[self.true_answers]
        return text_money

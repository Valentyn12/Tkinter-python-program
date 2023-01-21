import sqlite3


def connect():
    con = sqlite3.connect('store.db')
    c = con.cursor()
    c.execute("DROP TABLE IF EXISTS shop")
    c.execute("DROP TABLE IF EXISTS history")
    c.execute(""" CREATE TABLE IF NOT EXISTS shop(
    ID INTEGER PRIMARY KEY,
    names TEXT,
    amount INTEGER,
    price_non_PDW REAL,
    price REAL)
    """)
    c.execute("""CREATE TABLE IF NOT EXISTS history(
    "ID" INTEGER,
    "names_id" INTEGER,
    "names" REAL,
    "amount" INTEGER,
    "price_non_PDW" REAL,
    "price_with_pdw" INTEGER,
    "glob_price" REAL,
    PRIMARY KEY("ID" AUTOINCREMENT )
    )""")
    con.commit()
    store = [('1', 'Холодильник SAMSUNG RH62A50F1M9/UA', '10', '58 977', '70 772'),
             ('2', 'Пральна машина з сушкою SAMSUNG WD80T554CBT/UA', '7', '31 799', '38 158'),
             ('3', 'Пральна машина вузька SAMSUNG WW62J42E0HW/UA', '17', '17 499', '21 000'),
             ('4', 'Робот-пилосос Samsung Jet Bot+ VR30T85513W/EV', '8', '19 999', '24 000'),
             ('5', 'Кавомашина PHILIPS Series 5400 EP5447/90', '13', '26 999', '32 400'),
             ('6', 'Мультиварка-скороварка TEFAL Cook4me + Connect CY855830', '7', '8 699', '10 440'),
             ('7', 'Фотоепілятор PHILIPS Lumea Advanced SC1997/00', '4', '12 499', '15 000'),
             ('8', 'Машинка для стрижки Oster Barber Clipper 97-44 (чорний)', '9', '8 900', '10 680'),
             ('9', 'Фен Panasonic EH-NA65 Nanoe з дифузором', '5', '19 077', '22 892'),
             ('10', 'Смарт-ваги Xiaomi Mi Body Composition Scales 2 XMTZC05HM (NUN4048GL)', '20', '1 199', '1 444'),
             ('11', 'Плита комбінована BOSCH HXS59AI50Q', '11', '25 719', '30 862'),
             ('12', 'Гриль TEFAL OptiGrill+ XL GC724D12', '23', '9 999', '11 998'),
             ('13', 'Морозильна камера VESTFROST VD865FNW', '7', '15 555', '18 666'),
             ('14', 'Блендер TEFAL Ultrablend Vacuum Boost BL985A31', '8', '15 999', '19 198'),
             ('15', 'Термопот Breville Brita VKJ367, сріблястий', '9', '17 752', '21 102'),
             ('16', 'Ваги Brewista Smart Scale II', '14', '3 950', '4 740'),
             ('17', 'Акумуляторний пилосос PHILIPS SpeedPro Aqua FC6729/01', '4', '11 699', '14 038'),
             ('18', 'Масажна накидка BEURER MG 320', '3', '15 559', '18 670'),
             ('19', 'Електрична зубна щітка PHILIPS Sonicare 9900 Prestige з технологією SenseIQ HX9992/12', '9', '12 500', '15 000'),
             ('20', 'Кондиціонер BOSCH CL3000i RAC 5,3 kW', '17', '30 190', '36 228'),
             ('21', 'Електробритва Philips Shaver series 5000 S5585/30', '12', '4 399', '5 278'),
             ('22', 'Котел газовий IMMERGAS Eolo Star 24 4E + Коаксiальний комплект', '2', '26 277', '31 532'),
             ('23', 'Інфрачервоний обігрівач UFO Star 1900 + телескопічна ніжка UTS/UA', '5', '5 299', '6 358'),
             ('24', 'Кліматичний комплекс PANASONIC F-VXL40R-S', '3', '26 499', '31 798'),
             ('25', 'бойлер комб. навісн., верт. OKC200 теплообм. 1м2 2-6kW (110720905)', '4', '62 872', '75 446'),]
    c.executemany("INSERT INTO shop VALUES (?,?,?,?,?)",store)
    con.commit()
    con.close()
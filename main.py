from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()

# Подключаем папку с шаблонами
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,    
    })

@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/projects", response_class=HTMLResponse)
async def projects_page(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def contact_page(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/projects/{project_id}", name="project_detail")
async def project_detail(request: Request, project_id: int):
    projects = {
        1: {
            "title": "Модификация сканирующего электронного микроскопа серии Zeiss EVO",
            "image": ["main/images/product1/product1.jpg", "main/images/product1/product12.png"],
            "client": "АО «ГНЦ РФ НИИ атомных реакторов» (г.Димитровград)",
            "timeline": "Март 2023 – Декабрь 2023",
            "description": "Разработка обеспечивает управление всеми узлами микроскопа с помощью пульта, расположенного на удалённом операторском месте, а также снижение воздействия радиоактивного/ионизирующего излучения, испускаемого исследовательским образцом, размещённым на рабочем столике микроскопа, на электронные компоненты сканирующих электронных микроскопов серии Zeiss EVO.</p>"
               "<p>Элементы защиты и другие компоненты разработаны применимо к стационарному источнику излучения, активностью не более 0,25 Кюри нуклида Cs137, расположенному на столике микроскопа внутри рабочей камеры микроскопа.</p>"
               "<p><strong>Выполненные работы:</strong><br><br>"
               "1. Защита выносных электронных компонентов.<br>"
               "2. Защита не выносных электронных компонентов.<br>"
               "3. Защита аналитических приставок (волнового спектрометра WDS).<br>"
               "4. Модификация цифровой системы видеонаблюдения.<br>"
               "5. Изготовление комплекта специализированных столиков и сопутствующей оснастки.<br>"
               "6. Моторизация привода детектора обратно отражённых электронов BSE.<br>"
               "7. Моторизация привода блока апертур.</p>"
               "<strong>Патентная чистота</strong><br><br>"
                    "Устройство получения электронно-микроскопического изображения и локального элементного анализа радиоактивного образца методом электронной микроскопии в радиационно-защитной камере.<br>" 
                    "Патент на изобретение  RU 2678504 С1, 29.01.2019.<br>" 
                    "<strong>Авторы:</strong> Соболев А.А., Кирюхин В.Е., Макарычев В.В., Светухин В.В., Жуков А.В., Фомин А.Н., Власенко В.С., Ульяненков А.Г.<br>"

            },
        2: {
            "title": "Разработка управляемой дистанционно системы автоматизированной загрузки и выгрузки образцов (Системы перегрузки), содержащих радиоактивные компоненты,  для электронного микроскопа Zeiss Merlin.",
            "description": "Система радиационной защиты и загрузки образцов для электронного микроскопа предназначена для дистанционной автоматизированной загрузки/выгрузки радиоактивных образцов в микроскоп/из микроскопа и обеспечения радиационной защиты персонала при проведении работ по загрузке/выгрузке и исследованию образцов.<br><br>"
                "Категория опасности радиоактивных образцов по классификации НП-038-11: 3.<br><br>"
                "Состоит из управляемой дистанционно системы загрузки/выгрузки радиоактивных образцов; системы защиты детекторов для электронного микроскопа; управляемой дистанционно системы наблюдения за загрузкой, выгрузкой и манипуляциями с образцами  для электронного микроскопа Zeiss Merlin; устройств захвата, держателей, переноски, временного хранения и транспортировки радиоактивных образцов.<br><br>" 
                "Система интегрирована в штанную систему вентиляции и радиационного контроля.<br><br>",
            "image": ["/main/images/product2/product21.jpg","main/images/product2/product22.jpg","main/images/product2/product23.png","main/images/product2/product24.png"],
            "client": "НИЦ «Курчатовский институт»",
            "timeline": "Январь 2022 – Июль 2022"
        },
        3: {
            "title": "Робототехнический комплекс с интеллектуальной системой управления для работы в горячих камерах на предприятиях атомной отрасли.",
            "description": 
                "Экспериментальный образец робототехнического комплекса в радиационно-защитном исполнении "
                "предназначен для выполнения технологического процесса ручного и автоматизированного перемещения фрагментов массой до 10 кг "
                "в радиационно-защитных камерах и передачи их на последующий технологический участок.</p>"

                "<p>Управление манипулятором возможно на произвольном расстоянии от РЗК.</p>"

                "<p><strong>Состав экспериментального образца РТК:</strong></p>"
                "<ul>"
                "<li>роботизированная рука-манипулятор;</li>"
                "<li>джойстик-трипод с обратной тактильной связью;</li>"
                "<li>пульт управления с сенсорным экраном;</li>"
                "<li>стенд-стапель (макет радиационно-защитной камеры);</li>"
                "<li>программное обеспечение, обеспечивающее ручной и автоматический режимы управления, "
                "режимы визуализации, диагностики и протоколирования работы манипулятора.</li>"
                "</ul>"

                "<p><strong>Патентная чистота:</strong></p>"
                "<ol>"
                "<li>Патент на полезную модель №198350 от 02.07.2020 г. «Модуль ручного управления манипулятором».</li>"
                "<li>Патент на изобретение №2699703 от 09.09.2019 г. «Способ управления исполнительным механизмом робота-манипулятора "
                "с силомоментной обратной связью и устройство для его осуществления».</li>"
                "<li>Свидетельство на программу для ЭВМ №2019665313 от 21.11.2019 г. «Драйвер управления манипулятором в архитектуре ROS Control».</li>"
                "<li>Свидетельство на программу для ЭВМ №2019665314 от 21.11.2019 г. «Утилита конфигурации и управления драйверами Festo CMMP-AS».</li>"
                "<li>Свидетельство на программу для ЭВМ №2019666910 от 17.12.2019 г. «Библиотека кольцевого буфера с функцией динамической балансировки».</li>"
                "<li>Свидетельство на программу для ЭВМ №2019610021 от 09.01.2019 г. «Программная реализация драйвера управления цифровыми "
                "сервомоторами по протоколу LewanSoul Bus Servo Communication Protocol».</li>"
                "</ol>",
            "image": ["main/images/product3/product31.jpg", "main/images/product3/product32.jpg", "main/images/product3/product33.jpg", "main/images/product3/product34.png"],
            "client": " ООО НПФ «Сосны»",
            "timeline": "Апрель 2021 – Октябрь 2021"
        },
        4: {
            "title": "Разработка и изготовление внутрикамерного технологического оборудования для участка производства источников ионизирующего излучения на основе Ir-192",
            "description": (
                "<p><strong>Разработано и изготовлено технологическое оборудование в составе:</strong></p>"
                "<ul>"
                "<li>Установка сборки (источники тип I)</li>"
                "<li>Установка сборки (источники тип II)</li>"
                "<li>Установка герметизации ИИИ (тип I)</li>"
                "<li>Установка герметизации ИИИ (тип II)</li>"
                "<li>Установка контроля герметичности</li>"
                "<li>Установка дезактивации и контроля загрязненности</li>"
                "<li>Установка герметизации второго корпуса ИИИ (тип I)</li>"
                "<li>Установка сборки источника во второй (внешний) корпус (тип I)</li>"
                "<li>Установка контроля герметичности второго корпуса</li>"
                "<li>Устройство измерения МЭД готового источника</li>"
                "<li>Установка для присоединения концевой детали</li>"
                "<li>Установка испытания на разрыв (контроль прочности присоединения концевой детали)</li>"
                "</ul>"
            ),
            "image": ["main/images/product4/product41.jpg", "main/images/product4/product42.png", "main/images/product4/product43.jpg", "main/images/product4/product44.jpg", "main/images/product4/product45.jpg"],
            "client": "АО «ИРМ»",
            "timeline": "2020 – 2021"
        },
        5: {
            "title": "Автоматизированная система регистрации параметров технологических процессов, документирования и сопровождения жизненного цикла производства источников гамма-излучения на основе радионуклида иридий-192",
            "description": (
                "Автоматизированная система регистрации параметров технологических процессов, документирования и сопровождения "
                "жизненного цикла производства источников гамма-излучения на основе радионуклида иридий-192 (АСРПТП «Источник») представляет собой "
                "аппаратно-программный комплекс (АПК) для регистрации, хранения и анализа данных о технологическом процессе производства источников гамма-излучения. "
                "Данный АПК является клиент-серверным приложением, взаимодействующим с сервером базы данных по локальной сети. "
                "Клиентская часть представляет собой приложение с графическим интерфейсом, содержащим формы для ввода данных и элементы управления для подтверждения операций.</p>"

                "<p><strong>Клиентское приложение включает следующие рабочие места:</strong></p>"
                "<ul>"
                "<li><strong>«Администратор»</strong> — ввод и редактирование записей о пользователях и этапах технологического процесса.</li>"
                "<li><strong>«Сборка мишеней и облучательного устройства»</strong> — подтверждение получения чертежей, заданий и выполнения работ.</li>"
                "<li><strong>«Реакторное облучение»</strong> — подтверждение получения и выполнения заданий на облучение мишеней.</li>"
                "<li><strong>«Разборка мишеней»</strong> — подтверждение получения и выполнения заданий на разборку.</li>"
                "<li><strong>«Сборка и герметизация источника»</strong> — подтверждение получения заданий, запись параметров ТП.</li>"
                "<li><strong>«Дезактивация и контроль герметичности»</strong> — принятие и выполнение заданий на контроль герметичности, дезактивацию и запись параметров ТП.</li>"
                "<li><strong>«Паспортизация и подготовка к транспортировке»</strong> — принятие заданий на измерение активности, загрузку и герметизацию.</li>"
                "</ul>"

                "<p>Разделение на рабочие места отражает распределение этапов технологического процесса производства источников гамма-излучения на основе радионуклида иридий-192.</p>"
            ),
            "image": ["main/images/product5/product51.png"],
            "client": "АО «ИРМ»",
            "timeline": "2019 – 2020"
        },
        6: {
            "title": "Автоматизированная проботека",
            "description": (
                "<p><strong>Автоматизированная проботека</strong> предназначена для размещения перед измерением, "
                "автоматизированной доставки к детектору и измерений гамма-спектров контейнеров с облученными образцами, "
                "используемыми в нейтрон-активационном анализе (НAA).</p>"

                "<p>Область применения — нейтрон-активационный анализ (НAA). Входит в состав лаборатории НAA.</p>"
                "<p>В соответствии с НП-038-16 относится к элементам нормальной эксплуатации, не влияющим на безопасность, "
                "и имеет классификационное обозначение – <strong>3</strong>.</p>"
                "<table style='border-collapse: separate; border-spacing: 0; width: 100%; text-align: left; border-radius: 0px; overflow: hidden;'>"
                "<thead>"
                "<tr style='background-color: #003366; color: #ffffff;'>"
                "<th style='padding: 10px; border: 1px solid #ccc;'>Наименование</th>"
                "<th style='padding: 10px; border: 1px solid #ccc;'>Значение</th>"
                "</tr>"
                "</thead>"
                "<tbody>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Предельная масса единицы оборудования/изделия и/или системы (нетто), КГ</td><td style='padding: 8px; border: 1px solid #ccc;'>440</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Предельные габаритные размеры (ДхШхВ), мм</td><td style='padding: 8px; border: 1px solid #ccc;'>1835×830×20</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Максимальный угол вращения барабана, °</td><td style='padding: 8px; border: 1px solid #ccc;'>33</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Максимальное перемещение по оси x, мм</td><td style='padding: 8px; border: 1px solid #ccc;'>360</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Максимальное перемещение по оси z, мм</td><td style='padding: 8px; border: 1px solid #ccc;'>800</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Погрешность позиционирования центра ячейки барабана, мм</td><td style='padding: 8px; border: 1px solid #ccc;'>±0,5</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Погрешность позиционирования по оси x, мм</td><td style='padding: 8px; border: 1px solid #ccc;'>±0,5</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Погрешность позиционирования по оси z, мм</td><td style='padding: 8px; border: 1px solid #ccc;'>±0,5</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Количество образцов (капсул) в барабане</td><td style='padding: 8px; border: 1px solid #ccc;'>20</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Полный цикл смены образца на детекторе, не более, мин</td><td style='padding: 8px; border: 1px solid #ccc;'>1</td></tr>"
                "</tbody>"
                "</table>"
            ),
            "image": ["main/images/product6/product61.jpg", "main/images/product6/product62.png", "main/images/product6/product63.jpg", "main/images/product6/product64.png"],
            "client": "АО «ГНЦ РФ-ФЭИ» для ЦЯИТ (Боливия)",
            "timeline": "2019 – 2020"
        },
        7: {
            "title": "Система обеспечения измерения мгновенного гамма-излучения",
            "description": (
                "Система предназначена для проведения облучения исследуемого вещества тепловыми нейтронами и обеспечения условий для регистрации гамма-излучения, сопровождающего реакции нейтронов с ядрами исследуемого образца<br><br>"

                "<strong>Система обеспечения измерения мгновенного гамма-излучения</strong> состоит из коллиматора, форавакуумной камеры, стоппера нейтронного пучка и антинейтронной защиты. "
                "Относится к 3 классу безопасности по НП-038-16.<br><br>"

                "<div style='border: 1px solid #ccc; border-radius: 10px; overflow: hidden;'>"
                "<table style='border-collapse: collapse; width: 100%; text-align: left;'>"
                "<thead style='background-color: #112e5c; color: white; font-weight: bold;'>"
                "<tr>"
                "<th style='padding: 8px; border: 1px solid #ccc;'>Наименование</th>"
                "<th style='padding: 8px; border: 1px solid #ccc;'>Значение</th>"
                "</tr>"
                "</thead>"
                "<tbody>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Габаритные размеры, мм - коллиматор</td><td style='padding: 8px; border: 1px solid #ccc;'>979×201</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Габаритные размеры, мм - форавакуумная камера</td><td style='padding: 8px; border: 1px solid #ccc;'>1427×459×1841</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Габаритные размеры, мм - стоппер нейтронного пучка</td><td style='padding: 8px; border: 1px solid #ccc;'>732×801×1187</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Габаритные размеры, мм - антинейтронная защита</td><td style='padding: 8px; border: 1px solid #ccc;'></td></tr>"

                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Масса, кг - коллиматор</td><td style='padding: 8px; border: 1px solid #ccc;'>147,8</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Масса, кг - форавакуумная камера</td><td style='padding: 8px; border: 1px solid #ccc;'>135,4</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Масса, кг - стоппер нейтронного пучка</td><td style='padding: 8px; border: 1px solid #ccc;'>2329,7</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Масса, кг - антинейтронная защита</td><td style='padding: 8px; border: 1px solid #ccc;'></td></tr>"

                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Электропитание</td><td style='padding: 8px; border: 1px solid #ccc;'>3 фазная питающая сеть переменного тока напряжением 380 ± 22 В, при частоте 50 ± 5</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Количество образцов, помещаемых в форавакуумную камеру одновременно</td><td style='padding: 8px; border: 1px solid #ccc;'>4</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Устойчивость к моющим средствам, дезинфекции, дезактивации</td><td style='padding: 8px; border: 1px solid #ccc;'>Устойчивость к средству (этиловый спирт)</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Потребляемая мощность, Вт</td><td style='padding: 8px; border: 1px solid #ccc;'>550</td></tr>"
                "</tbody>"
                "</table>"
                "</div><br>"
                "<strong>Коллиматор</strong> представляет собой устройство, располагаемое в проходке шибера горизонтального канала реактора, обеспечивающее направленный поток тепловых нейтронов в нейтроновод форавакуумной камеры.<br>"
                "Корпус форавакуумной камеры с нейтроноводом выполнены из алюминия АД1, корпуса коллиматора и стоппера нейтронного пучка — из коррозионностойкой стали 12Х18Н10Т."
            ),
            "image": ["main/images/product7/product71.png","main/images/product7/product72.png","main/images/product7/product73.png"],
            "client": "АО «ИРМ»",
            "timeline": "Январь 2022 – Июль 2022"
        },
        8: {
            "title": "Автоматизированная система позиционирования к установке для обработки изделий сложной формы импульсными плазменными потоками",
"description": (
                "Система размещается в рабочей вакуумной камере установки и обеспечивает нужное положение обрабатываемого изделия относительно потока плазмы.<br><br>"
                "Сложность данной задачи обусловлена требованиями по вакууму, ограниченными размерами вакуумной камеры и высокими массогабаритными характеристиками обрабатываемого изделия.<br><br>"
                "В случае обращения с плазменными потоками также существуют риски спекания металлических узлов конструкционных элементов вследствие разогрева.<br><br>"
                "<strong>Основные технические характеристики</strong><br><br>"
                "<table style='border-collapse: separate; border-spacing: 0; width: 100%; text-align: left; border-radius: 0px; overflow: hidden;'>"
                "<thead style='background-color: #112e5c; color: white; font-weight: bold;'>"
                "<tr><th style='padding: 8px; border: 1px solid #ccc;'>Наименование</th><th style='padding: 8px; border: 1px solid #ccc;'>Значение</th></tr>"
                "</thead><tbody>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Точность, град</td><td style='padding: 8px; border: 1px solid #ccc;'>± 0</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Максимальная скорость перемещения рабочего стола по осям x, y</td><td style='padding: 8px; border: 1px solid #ccc;'>300 мм/мин</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Максимальная скорость по оси z</td><td style='padding: 8px; border: 1px solid #ccc;'>30 мм/мин</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Поворот вокруг оси z</td><td style='padding: 8px; border: 1px solid #ccc;'>100 град/мин</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Наклон вокруг оси y</td><td style='padding: 8px; border: 1px solid #ccc;'>100 град/мин</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Максимальная масса изделия на рабочем столе</td><td style='padding: 8px; border: 1px solid #ccc;'>20 кг</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Температура нагрева рабочего стола</td><td style='padding: 8px; border: 1px solid #ccc;'>до 300 °C</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Работоспособность в условиях вакуума</td><td style='padding: 8px; border: 1px solid #ccc;'>до 10⁻⁴ мбар</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Электропитание</td><td style='padding: 8px; border: 1px solid #ccc;'>220 ± 22 В, 50 ± 5 Гц (1 фаза)</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Потребляемая мощность</td><td style='padding: 8px; border: 1px solid #ccc;'>2000 Вт</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Масса блока позиционирования</td><td style='padding: 8px; border: 1px solid #ccc;'>не более 250 кг</td></tr>"
                "</tbody></table><br><br>"

                "<table style='border-collapse: separate; border-spacing: 0; width: 100%; text-align: left; border-radius: 0px; overflow: hidden;'>"
                "<thead style='background-color: #112e5c; color: white; font-weight: bold;'>"
                "<tr><th style='padding: 8px; border: 1px solid #ccc;'>Наименование</th><th style='padding: 8px; border: 1px solid #ccc;'>Значение</th></tr>"
                "</thead><tbody>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Рабочий стол с T-образными пазами</td><td style='padding: 8px; border: 1px solid #ccc;'>260×260 мм</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Линейные перемещения</td><td style='padding: 8px; border: 1px solid #ccc;'>по осям x, z и y</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Диапазон перемещений по x</td><td style='padding: 8px; border: 1px solid #ccc;'>не менее 225 мм</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>по y</td><td style='padding: 8px; border: 1px solid #ccc;'>не менее 150 мм</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>по z</td><td style='padding: 8px; border: 1px solid #ccc;'>не менее 260 мм</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Шаг перемещения</td><td style='padding: 8px; border: 1px solid #ccc;'>1 мм</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Точность позиционирования</td><td style='padding: 8px; border: 1px solid #ccc;'>±0.5 мм</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Вращение рабочего стола</td><td style='padding: 8px; border: 1px solid #ccc;'>вокруг оси z</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Диапазон вращения</td><td style='padding: 8px; border: 1px solid #ccc;'>0–360°</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Шаг вращения</td><td style='padding: 8px; border: 1px solid #ccc;'>1°</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Наклон рабочего стола</td><td style='padding: 8px; border: 1px solid #ccc;'>от электродной системы и к ней</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Диапазон наклона</td><td style='padding: 8px; border: 1px solid #ccc;'>0–90°</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Шаг наклона</td><td style='padding: 8px; border: 1px solid #ccc;'>1°</td></tr>"
                "</tbody></table>"
            ),
            "image": ["main/images/product8/product81.jpg","main/images/product8/product82.jpg","main/images/product8/product83.jpg"],
            "client": "АО «ГНЦ РФ ТРИНИТИ»",
            "timeline": "Январь 2022 – Июль 2022"
        },
        9: {
            "title": "Технология и АПК для дезактивации выведенного из эксплуатации трубного оборудования АЭС с применением озона",
            "description": (
                "Разработан образец транспортируемого стенда дезактивации в масштабе, близком к реальному, предназначен для демонстрации и испытания режимов дезактивации выведенного из эксплуатации трубного оборудования с применением концентрированного озона.<br><br>"
                "<strong>Состав системы:</strong><br>"
                "1. Газовая система: кислородный баллон, озонатор, измеритель концентрации озона, расходомер по газу, клапан, газоанализатор, поглотитель.<br>"
                "2. Циркуляционная система: насос, расходомер по воде, эжектор, краны, манометр.<br>"
                "3. Система нагрева: 3 нагревателя, датчики температуры.<br>"
                "4. Шкаф управления: ПЛК, сенсорная панель.<br>"
                "5. Установочный модуль: коллектор, поворотная рама, опоры.<br><br>"
                "<strong>Технические характеристики:</strong><br>"
                "<table style='border-collapse: separate; border-spacing: 0; width: 100%; text-align: left; border-radius: 0px; overflow: hidden;'>"
                "<thead style='background-color: #153364; color: white;'>"
                "<tr><th style='padding: 8px; border: 1px solid #ccc;'>Наименование параметра</th>"
                "<th style='padding: 8px; border: 1px solid #ccc;'>Значение</th></tr></thead><tbody>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Длина, м</td><td style='padding: 8px; border: 1px solid #ccc;'>2,7</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Ширина, м</td><td style='padding: 8px; border: 1px solid #ccc;'>1,3</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Высота, м</td><td style='padding: 8px; border: 1px solid #ccc;'>1,8</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Напряжение, В</td><td style='padding: 8px; border: 1px solid #ccc;'>220</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Мощность, кВт</td><td style='padding: 8px; border: 1px solid #ccc;'>35</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Концентрация озона, г/л</td><td style='padding: 8px; border: 1px solid #ccc;'>50</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Степень защиты</td><td style='padding: 8px; border: 1px solid #ccc;'>IP54</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Наружный диаметр труб, мм</td><td style='padding: 8px; border: 1px solid #ccc;'>10–16</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Длина труб, мм</td><td style='padding: 8px; border: 1px solid #ccc;'>300–1500</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Количество труб</td><td style='padding: 8px; border: 1px solid #ccc;'>1–12</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Температура растворов, °C</td><td style='padding: 8px; border: 1px solid #ccc;'>90…95</td></tr>"
                "</tbody></table><br>"
                "Разработан транспортируемый полнофункциональный полноразмерный образец в масштабе демонстратора для дезактивации выведенного из эксплуатации оборудования ОИАЭ с применением О₃.<br><br>"
                "<strong>Состав системы:</strong><br>"
                "1. Блок генерации озона: кислородный баллон, озонатор, измеритель концентрации озона, электронный расходомер по газу, электромагнитный клапан.<br>"
                "2. Блок дезактивации: две ванны, две съёмные корзины.<br>"
                "3. Блок приготовления газо-жидкостной смеси: аэрограф, два эжектора, распределитель.<br>"
                "4. Блок накопления: накопители для дистиллированной и отработанной жидкости.<br>"
                "5. Блок циркуляции и нагрева: два насоса, четыре нагревателя, два расходомера.<br>"
                "6. Блок безопасности: газоанализатор, поглотитель озона.<br>"
                "7. Блок управления: шкаф управления, датчики температуры, уровня и давления.<br><br>"
                "<strong>Основные технические характеристики:</strong><br>"
                "<table style='border-collapse: separate; border-spacing: 0; width: 100%; text-align: left; border-radius: 0px; overflow: hidden;'>"
                "<thead style='background-color: #153364; color: white;'>"
                "<tr><th style='padding: 8px; border: 1px solid #ccc;'>Наименование параметра</th>"
                "<th style='padding: 8px; border: 1px solid #ccc;'>Значение</th></tr></thead><tbody>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Длина, м</td><td style='padding: 8px; border: 1px solid #ccc;'>2,0</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Ширина, м</td><td style='padding: 8px; border: 1px solid #ccc;'>1,2</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Высота, м</td><td style='padding: 8px; border: 1px solid #ccc;'>1,5</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Масса (без жидкостей), кг</td><td style='padding: 8px; border: 1px solid #ccc;'>500</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Температура растворов, °C</td><td style='padding: 8px; border: 1px solid #ccc;'>20 – 95</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Рабочая температура, °C</td><td style='padding: 8px; border: 1px solid #ccc;'>90 – 95</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Поток газо-жидкостной смеси, л/мин</td><td style='padding: 8px; border: 1px solid #ccc;'>40</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Входное напряжение, В</td><td style='padding: 8px; border: 1px solid #ccc;'>3×380</td></tr>"
                "<tr><td style='padding: 8px; border: 1px solid #ccc;'>Мощность, кВт</td><td style='padding: 8px; border: 1px solid #ccc;'>60</td></tr>"
                "</tbody></table>"
            ),
            "image": ["main/images/product9/product91.jpg"],
            "client": "АО «ГНЦ РФ ТРИНИТИ»",
            "timeline": "Январь 2022 – Июль 2022"
        },
        10: {
            "title": "Технический проект АСУ ТП комплекса по наработке актиния фотоядерным способом",
            "description": (
                "Целью разработки было повышение безопасности эксплуатации программно-аппаратного комплекса по наработке актиния фотоядерным способом за счет автоматизации функций контроля и управления.<br><br>"
                "Класс безопасности: 2-й по НП-038-16.<br><br>"
                "<strong>Выполненные работы:</strong><br>"
                "<ul style='padding-left: 20px; margin-top: 10px;'>"
                "<li>Разработана архитектура системы.</li>"
                "<li>Согласованы форматы и структуры обмена данными с подсистемами.</li>"
                "<li>Согласован формат сохранения данных в журнал.</li>"
                "<li>Согласован перечень аппаратных средств системы.</li>"
                "<li>Спроектированы процессы сбора данных и их синхронизации на уровне серверов АСУ ТП.</li>"
                "<li>Спроектирован человеко-машинный интерфейс (мнемосхема).</li>"
                "<li>Разработана схема организации доступа пользователей.</li>"
                "</ul>"
            ),
            "image": ["main/images/product10/product101.jpg","main/images/product10/product102.png"],
            "client": "АО «ГНЦ РФ-ФЭИ»",
            "timeline": "Январь 2022 – Июль 2022"
        },
    }

    project = projects.get(project_id)
    return templates.TemplateResponse(
        "project_detail.html",
        {"request": request, "project": project}
    )
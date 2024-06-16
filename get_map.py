def get_map(params=None):
    map_api_server = "http://static-maps.yandex.ru/1.x/"

    response = requests.get(map_api_server, params=params)

    if not response:
        print("Ошибка выполнения запроса ", response.url)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # инициализация игры
    pygame.init()
    window = pygame.display.set_mode(600, 450)

    file_name = "map.png"
    with open(file_name, "wb") as file:
        file.write(response.content)

    window.blit(pygame.image.load(file_name), (0, 0))
    pygame.display.flip()

    # Переменные, определяющие текущий масштаб карты и изменение масштаба
    current_scale = float(spn[0])
    scale_step = 0.1

    # Обработка событий клавиш PgUp и PgDown
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                current_scale += scale_step
            elif event.key == pygame.K_PAGEDOWN:
                current_scale -= scale_step

        # Проверяем, что масштаб не выходит за пределы
        current_scale = max(0.01, min(10, current_scale))
        spn[0] = str(current_scale)

        # Собираем параметры для запроса к Static Maps API:
        map_params = {"ll": ",".join(coord), "spn": ",".join(spn), "l": "map"}

        response = get_map(map_params)

        pygame.display.flip()

    # Удаляем за собой файл с изображением.
    os.remove(file_name)

    # Преобразуем ответ в json-объект
    return response

# Название приложения
APP_NAME = "Система авторизации пользователей по голосу"
SIGN_UP_NAME = "Регистрация нового пользователя"
LOG_IN_NAME = "Авторизация по голосу"
RECORDING_MESSAGE_NAME = "Запись голоса"
RECORDING_SUCCESS = "Успех!"
RECORDING_ERROR = "Совпадение не найдено"

# Размеры стартового окна
main_width = 600
sign_up_width = 450
log_in_width = 350
main_height = 100
sign_up_height = 200
log_in_height = 50
start_postion_x = 200
start_postion_y = 200
main_geometry = f"{main_width}x{main_height}+{start_postion_x}+{start_postion_y}"
sign_up_geometry = f"{sign_up_width}x{sign_up_height}+{start_postion_x}+{start_postion_y}"
log_in_geometry = f"{log_in_width}x{log_in_height}+{start_postion_x}+{start_postion_y}"

# Тексты
MAIN_LABEL = "Войдите или зарегистрируйтесь при помощи голоса"
LOG_IN_BTN = "Войти"
SIGN_UP_BTN = "Регистрация"
BACK_TO_MAIN_MENU = "Назад в меню"
POSITION = "Должность"
FIO = "ФИО"
SMTH = "Что-то ещё"
RECORD_VOICE = 'Записать голос'
RECORDING_MESSAGE = "Как будете готовы записывать - нажмите 'ОК'"
RECORDING_MESSAGE_SUCCESS = "Вы успешно зарегистрированы"
SUCCESS = "Вы прошли авторизацию"
ERROR = "Авторизация не пройдена, возможно голоса не совпадают или различны в тоне"

fs = 44100  # Sample rate
seconds = 2  # Duration of recording
SENSIVITY = 10000.0

ENDING_DESTROY = False


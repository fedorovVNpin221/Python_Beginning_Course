import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import matplotlib.pyplot as plt
import io

# Токен бота
BOT_TOKEN = "8474167681:AAGLYptHm9_uRb087zSpbEsrvKkZdVZYals"

# Создаем бота и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Класс для построения графиков (исправленный)
class Plot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def create_plot(self):
        # Создаем фигуру и оси
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Строим график
        ax.plot(self.x, self.y, label="Функция", marker='o', linestyle='-', linewidth=2, color='blue')
        ax.set_xlabel("Ось ОX")
        ax.set_ylabel("Ось ОY")
        ax.set_title('График функции')
        ax.legend()
        ax.grid(True)
        
        # Сохраняем в буфер
        buf = io.BytesIO()
        plt.savefig(
            buf, 
            format='png', 
            dpi=100,
            bbox_inches='tight',
            facecolor='white'
        )
        buf.seek(0)
        plt.close(fig)  # Важно закрыть фигуру
        return buf

# Хранилище данных пользователей
user_data = {}

# Обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: types.Message): # Асинхронная фнукция для обработки команды 
    # пользователя "/start"
    user_id = message.from_user.id
    # Очищаем предыдущие данные пользователя
    if user_id in user_data:
        del user_data[user_id]
        
    await message.answer(
        "👋 Привет! Я бот для построения графиков.\n"
        "Отправь мне значения X через запятую (например: 1,2,3,4,5)"
    )

# Обработчик команды /help
@dp.message(Command("help"))
async def help_command(message: types.Message):  # Асинхронная фнукция для обработки команды 
    # пользователя "/help"
    await message.answer(
        "📖 Как использовать бота:\n"
        "1. Отправь значения X через запятую\n"
        "2. Отправь значения Y через запятую\n"
        "3. Получи готовый график!\n\n"
        "Пример:\n"
        "X: 1,2,3,4,5\n"
        "Y: 10,20,30,40,50\n\n"
        "/start - начать заново\n"
        "/cancel - отменить текущую операцию"
    )

# Обработчик команды /cancel для сброса
@dp.message(Command("cancel"))
async def cancel_command(message: types.Message):  # Асинхронная фнукция для обработки команды 
    # пользователя "/cancel" и сброса ввода
    user_id = message.from_user.id 
    if user_id in user_data:
        del user_data[user_id]
    await message.answer("🚫 Текущая операция отменена. Напиши /start чтобы начать заново")


# Обработчик текстовых сообщений
@dp.message()
async def handle_message(message: types.Message):  # Асинхронная фнукция для обработки 
    # любых текстовых сообщений пользователя и отправки ответа в виде графика функции
    user_id = message.from_user.id
    
    # Пропускаем команды
    if message.text.startswith('/'):
        return
    
    try:
        # Парсим числа из сообщения
        parts = message.text.split(',')
        numbers = []
        for part in parts:
            number = float(part.strip())
            numbers.append(number)
        
        if user_id not in user_data:
            # Первое сообщение - значения X
            user_data[user_id] = {'x': numbers}
            await message.answer(f"✅ Сохранены значения X: {numbers}\nТеперь отправь значения Y через запятую")
            
        elif 'x' in user_data[user_id] and 'y' not in user_data[user_id]:
            # Второе сообщение - значения Y
            user_data[user_id]['y'] = numbers
            
            # Проверяем, что количество точек совпадает
            if len(user_data[user_id]['x']) != len(user_data[user_id]['y']):
                error_msg = f"❌ Количество значений не совпадает!\nX: {len(user_data[user_id]['x'])} точек\nY: {len(user_data[user_id]['y'])} точек\nОтправь значения Y заново"
                del user_data[user_id]['y']  # Удаляем только Y, оставляя X
                await message.answer(error_msg)
                return
            
            # Создаем график
            x_data = user_data[user_id]['x']
            y_data = user_data[user_id]['y']
            
            # Используем исправленный класс Plot
            plotter = Plot(x_data, y_data)
            plot_buf = plotter.create_plot()
            
            # Отправляем график пользователю
            await message.answer_photo(photo=types.BufferedInputFile(plot_buf.getvalue(), filename="graph.png"),
                caption=f"📊 График построен!\nX: {x_data}\nY: {y_data}"
            )
            
            # Очищаем данные пользователя
            del user_data[user_id]
            
    except ValueError:
        if user_id in user_data and 'x' in user_data[user_id] and 'y' not in user_data[user_id]:
            # Ошибка при вводе Y
            await message.answer("❌ Неверный формат чисел для Y! Отправь значения Y через запятую (например: 10,20,30,40,50)")
        else:
            # Ошибка при вводе X
            await message.answer("❌ Неверный формат чисел! Отправь числа через запятую (например: 1,2,3,4,5)")

# Запуск бота
async def main():
    print("📊 Бот для построения графиков запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
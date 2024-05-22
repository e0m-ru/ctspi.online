// Получаем текущую дату и время
let currentDate = new Date();

// Округляем минуты до ближайшего 30-минутного интервала
let minutes = currentDate.getMinutes();
currentDate.setMinutes(minutes + (30 - minutes % 30));

// Округляем часы в большую сторону
let hours = currentDate.getHours();
currentDate.setHours(hours + 3);

// Форматируем дату и время в нужный формат
let formattedDate = currentDate.toISOString().slice(0, 16);

// Вставляем текущую дату и время в поле формы
document.getElementById("s_dt").value = formattedDate;

currentDate.setHours(hours + 4)
formattedDate = currentDate.toISOString().slice(0, 16);
document.getElementById("e_dt").value = formattedDate;
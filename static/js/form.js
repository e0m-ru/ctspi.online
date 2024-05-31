let s_dt = document.querySelector('#s_dt');
let e_dt = document.querySelector('#e_dt');
let t_delta = document.querySelector('#t_delta');
let currentDate = new Date();

s_dt.addEventListener('input', handleInputChange_s);
e_dt.addEventListener('input', handleInputChange_e);

// Устанавливаем фокус на первй input элемент
input_el = document.querySelector('#title')
input_el.focus();

// Округляем минуты до ближайшего 30-минутного интервала
let minutes = currentDate.getMinutes();
currentDate.setMinutes(minutes + (30 - minutes % 30));
let hours = currentDate.getHours();

// !!! костыль для timezone
currentDate.setHours(hours + 3);

let formattedDate = currentDate.toISOString().slice(0, 16);
s_dt.value = formattedDate;

// !!! костыль для timezone
currentDate.setHours(hours + 4)

formattedDate = currentDate.toISOString().slice(0, 16);
e_dt.value = formattedDate;

function handleInputChange_s() {
    const timeDifference = new Date(e_dt.value) - new Date(s_dt.value);
    const hoursDiff = Math.floor(timeDifference / (1000 * 60 * 60));
    const minutesDiff = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
    const formattedTimeDifference = `${hoursDiff}:${minutesDiff}`;
    document.querySelector('#t_delta').value = formattedTimeDifference;    
}
function handleInputChange_e() {
    const timeDifference = new Date(e_dt.value) - new Date(s_dt.value);
    const hoursDiff = Math.floor(timeDifference / (1000 * 60 * 60));
    const minutesDiff = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
    const formattedTimeDifference = `${hoursDiff}:${minutesDiff}`;
    document.querySelector('#t_delta').value = formattedTimeDifference;    
}



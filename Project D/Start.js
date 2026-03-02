// script.js
const menuToggle = document.getElementById('menuToggle');
const menuCard = document.getElementById('menuCard');
const commentToggle = document.getElementById('commentToggle');
const commentCard = document.getElementById('commentCard');
const foodAtRoomToggle = document.getElementById('foodAtRoomToggle');
const foodAtRoomCard = document.getElementById('foodAtRoomCard');
const submitBtn = document.getElementById('submitBtn');
const nameInput = document.getElementById('name');
const roomNoInput = document.getElementById('roomNo');
const doctorSlipInput = document.getElementById('doctorSlip');
const commentTextarea = document.querySelector('#commentCard textarea');
const menuData = [
    {
        day: 'Monday',
        breakfast: 'ALOO PARATHA + BUTTER + CORN FLAKES + CHANA SPROUTS',
        lunch: 'DRY ALOO GOBHI/ SEASONAL VEG + RAJMA + RICE+ DAL FRY + BUTTER MILK + CHIPS',
        snacks: 'SAMOSA + TEA/COFFEE',
        dinner: 'SHIMLA MIRCH ALOO/ BHINDI + ROTI + RICE + MASOOR DAAL+ MOTICHOOR LADDU/BOONDI'
    },
    {
        day: 'Tuesday',
        breakfast: 'UTTAPAM + SAMBHAR + DALIYA + MOONG SPROUTS + GUAVA/BANANA',
        lunch: 'MATAR ALOO CABBAGE + GRAVY CHANA MASALA + ROTI +JEERA RICE + MOONG DAL + LASSI + CHIPS',
        snacks: 'MACRONI + TEA/COFFEE',
        dinner: 'DAL MAKHANI + LAUKI KOFTA + RICE + MISSI ROTI/ PLAIN ROTI + SUJI HALWA'
    },
    {
        day: 'Wednesday',
        breakfast: 'MOONG DAL CHEELA/MIXED PARATHA + CHUTNEY + BUTTER+CORN FLAKES+MOONG SPROUTS',
        lunch: 'BAIGAN ALOO/KATHAL + DRY SOYA CHUNKS +ROTI+ PANCHRATAN DAL + RICE +BOONDI RAITA + CHIPS',
        snacks: 'POHA + TEA / COFFEE',
        dinner: 'VEG- MATAR PANEER+ RICE+ ROTI + ARHAR DAAL +2 GULAB JAMUN NON-VEG- EGG CURRY (2 EGGS)+ ARHAR DAL+ RICE+ ROTI + 1 GULAB JAMUN.'
    },
    {
        day: 'Thursday',
        breakfast: 'IDLI + SAMBHAR + COCONUT CHUTNEY + DALIA + BOILED CHANA SALTED + BANANA/GUAVA/ORANGES',
        lunch: 'KATHOL + METHI/DAL PURI+ KADDU SABJI + PULAO/LEMON RICE/ TOMATO RICE + ARHAR DAAL + MIX RAITA + PAPAD',
        snacks: 'MAGGI+ TEA/COFFEE',
        dinner: 'FRIED RICE + VEG MANCHURIAN + CHANA DAAL + RICE + ROTI + LAUNG LATA'
    },
    {
        day: 'Friday',
        breakfast: 'PANEER PARATHA + BUTTER + CORN FLAKES + CHANA',
        lunch: 'MATAR MUSHROOM DRY + KADI PAKODA + MASOOR DAL FRY +ROTI+ RICE + PAPAD',
        snacks: 'ALOO TIKKI+ TEA / COFFEE',
        dinner: 'VEG - KADAI PANEER + DAAL FRY + TANDOORI ROTI + RICE + RASMALAI NON-VEG - CHICKEN MASALA (2PCS) + TANDOORI ROTI + RICE+ DAAL FRY'
    },
    {
        day: 'Saturday',
        breakfast: 'METHI PURI + BHANDARE WALE ALOO + JALEBI + NAMKEEN DALIYA + CHANA SPROUTS',
        lunch: 'BAIGAN BHARTA + SEASONAL VEG CURRY +PAPAD + KHICHDI + CURD + JEERA RICE + ROTI + FRENCH FRIES',
        snacks: 'BREAD PAKODA/ CORN VEG SANDWICH + TEA/ COFFEE',
        dinner: 'DUM ALOO + VEG BIRYANI + CHUTNEY + RAITA+ DAL FRY + MOONG DAAL HALWA OR FIESTA/GALA DINNER *'
    },
    {
        day: 'Sunday',
        breakfast: 'MASALA DOSA + SAMBHAR + COCONUT CHUTNEY + MOONG SPROUTS',
        lunch: 'CHOLE BHATURE + JEERA ALOO + MOONG DAL + PAPAD + DAHI VADA+ROTI',
        snacks: 'DABELI/ PANI PURI+ TEA/COFFEE',
        dinner: 'MIX VEG WITH PANEER + PALAK DAL + RICE + ROTI + KHEER'
    }
];

function toggleCard(card, isOpen) {
    card.style.display = isOpen ? 'block' : 'none';
    document.querySelectorAll('.card').forEach(c => {
        if (c !== card) {
            c.style.display = 'none';
        }
    });
}

menuToggle.addEventListener('click', () => {
    toggleCard(menuCard, !menuCard.style.display || menuCard.style.display === 'none');
    populateMenuTable();
});

commentToggle.addEventListener('click', () => {
    toggleCard(commentCard, !commentCard.style.display || commentCard.style.display === 'none');
});

foodAtRoomToggle.addEventListener('click', () => {
    toggleCard(foodAtRoomCard, !foodAtRoomCard.style.display || foodAtRoomCard.style.display === 'none');
});

function validateForm() {
    const isFormValid = nameInput.value.trim() !== '' && roomNoInput.value.trim() !== '';
    submitBtn.disabled = !isFormValid;
}

nameInput.addEventListener('input', validateForm);
roomNoInput.addEventListener('input', validateForm);

commentTextarea.addEventListener('input', () => {
    if (commentTextarea.value.trim() === '') {
        commentTextarea.placeholder = 'Write your review';
    } else {
        commentTextarea.placeholder = '';
    }
});

function populateMenuTable() {
    const menuTableBody = document.querySelector('#menuCard tbody');
    menuTableBody.innerHTML = '';

    menuData.forEach(item => {
        const row = document.createElement('tr');

        const dayCell = document.createElement('td');
        dayCell.textContent = item.day;
        row.appendChild(dayCell);

        const breakfastCell = document.createElement('td');
        breakfastCell.textContent = item.breakfast;
        row.appendChild(breakfastCell);

        const lunchCell = document.createElement('td');
        lunchCell.textContent = item.lunch;
        row.appendChild(lunchCell);

        const snacksCell = document.createElement('td');
        snacksCell.textContent = item.snacks;
        row.appendChild(snacksCell);

        const dinnerCell = document.createElement('td');
        dinnerCell.textContent = item.dinner;
        row.appendChild(dinnerCell);

        menuTableBody.appendChild(row);
    });
}
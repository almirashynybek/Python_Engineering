
const num1Input = document.getElementById('num1');
const num2Input = document.getElementById('num2');
const resultDisplay = document.getElementById('result');
const historyList = document.getElementById('history-list'); 


// Функция для выполнения операций (calculate).
function calculate(operation){
    num1 = parseFloat(num1Input.value);
    num2 = parseFloat(num2Input.value);

    if (num1Input.value === '' || num2Input.value === '' || isNaN(num1) || isNaN(num2)) {
        alert('Ошибка: Пожалуйста, введите корректные числа в оба поля!');
        return;
    }

    if (operation === '/' && num2 === 0) {
        alert('Ошибка: Деление на 0 невозможно!');
        return;
    }

    let result;
    switch (operation) {
        case '+':
        result = num1 + num2;
        break;
        case '-':
        result = num1 - num2;
        break;
        case '*':
        result = num1 * num2;
        break;
        case '/':
        result = num1 / num2;
        break;
    }
    addToHistory(num1, operation, num2, result);
}



// Функция для добавления записи в историю (addHistoryItem).
function addToHistory(num1, operation, num2, result) {
    const historyItem = document.createElement('li'); 
    historyItem.textContent = `${num1} ${operation} ${num2} = ${result}`;
    historyList.appendChild(historyItem); 
}
  

// Функция для очистки истории (clearHistory).
function clearHistory() {
    historyList.innerHTML = ''; // Clears all list items
}



let buttom_add = document.getElementById('add');
let buttom_sub = document.getElementById('subtract');
let buttom_mult = document.getElementById('multiply');
let buttom_div = document.getElementById('divide');


buttom_add.addEventListener('click', () => calculate('+'));
buttom_sub.addEventListener('click', () => calculate('-'));
buttom_mult.addEventListener('click', () => calculate('*'));
buttom_div.addEventListener('click', () => calculate('/'));

document.querySelector('.clear-history').addEventListener('click', clearHistory);
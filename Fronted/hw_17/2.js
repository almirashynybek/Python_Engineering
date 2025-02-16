// Задание 3: Создание таблицы умножения

// for (let i=1; i<11; i++){
//     for (let j=1; j<11; j++){
//         console.log(`${i} * ${j} = ${i * j}`)
//     }
// }


for (let i = 1; i < 11; i++){
    row = '';
    for (let j = 1; j < 11; j++){
        multiplication = i * j;
        // row += (multiplication.toString() + '   ')
        row += multiplication.toString().padStart(5, ' ')
    }
    console.log(row)
}
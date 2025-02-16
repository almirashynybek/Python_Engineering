// Задание 6: Работа с объектами — подсчёт свойств

const student = {
    name: "Kate Smith",
    age: 20,
    course: 3,
    grades: [60, 75, 80, 55, 90]
};

let total = 0;
for (let grade of student.grades){
    total += grade;
}

let average_grade = total / student.grades.length

student.status = average_grade >= 50 ? "сдал" : "не сдал";

console.log(`Имя: ${student.name}`);
console.log(`Возраст: ${student.age}`);
console.log(`Средний балл: ${average_grade.toFixed(2)}`);
console.log(`Статус: ${student.status}`);

// Задание 2: Работа с массивами и условными операторами

let arr = [1,3,6,8,4,9,13];
let max_element = -Infinity 
let min_element =  Infinity;
let count = 0



for (let i=0; i<arr.length; i++){
    count += arr[i]

    if (max_element < arr[i]){
        max_element = arr[i]
    }
    if (min_element > arr[i]){
        min_element = arr[i]
    }

}

console.log(count)
console.log(max_element)
console.log(min_element)


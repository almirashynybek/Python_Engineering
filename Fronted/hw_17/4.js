// Задание 5: Факториал числа


function factorial(num){
    if (num <= 0){
        console.log('Enter positive number!')
    }
    else{
        let result = 1;
        let i = 1;
        while( i <= num){
            result *= i;
            i++;
        }
        console.log(result)
    }
    
}

let num = 5;
factorial(num);
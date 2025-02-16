// Задание 4: Анализ строки

// first method
let str = 'fhru id46 9348bus  3hia%&)_$*';
let count_digit = 0
let count_letter = 0;
let count_space = 0;

for (let i=0; i<str.length; i++){
    if (str[i] >= '1' && str[i] <= '9'){
        count_digit += 1;
    }
    else if (str[i] === ' '){
        count_space += 1;
    }
    else if (str[i] >= 'a' && str[i] <= 'z' || str[i] >= 'A' && str[i] <= 'Z'){
        count_letter += 1;
    }
}
console.log(count_digit)
console.log(count_space)
console.log(count_letter)




// second method
function analyzeString(str){
    let count_digit = 0
    let count_letter = 0;
    let count_space = 0;

    for (let char of str){
        if (char >= '1' && char <= '9'){
            count_digit += 1;
        }
        else if (char === ' '){
            count_space += 1;
        }
        else if (char >= 'a' && char <= 'z' || char >= 'A' && char <= 'Z'){
            count_letter += 1;
        }
    }

    return{
        letters: count_letter, digits: count_digit, spaces: count_space
    };
}


const result = analyzeString(str);
console.log(result.letters);
console.log(result.digits);
console.log(result.spaces);
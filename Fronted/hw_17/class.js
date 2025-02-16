let age = 18
let access = age >= 18 ? 'Allowed': 'Not allowed'
// access = 'allowed' if age >= 18 else 'not allowed' 

console.log(access)


let score = 65;
let grade = score >= 90
    ? 'Great'
    : score >= 75
    ? 'fine'
    : 'not fine'
    
console.log(grade)


let day = 'monday';
switch (day){
    case 'monday':
        console.log('is true')
        break;

    case 'tuesday':
        console.log('not true')
        break;

    default:
        console.log('unknowe day')

}

do {
    console.log(i);
    i++
}while (i !== 1);



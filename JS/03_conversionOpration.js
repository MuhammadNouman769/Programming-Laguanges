let score = true;

console.log(typeof score);
console.log(typeof (score));

let valueInNumber = Number(score)
console.log(valueInNumber);
console.log(typeof valueInNumber);

// "33" => 33
// "33abc" => NaN
// true => 1
// false => 0

let isLoggedIn = 1
let booleanIsLoggedIn = Boolean(isLoggedIn)
console.log(booleanIsLoggedIn);

// 1 => true
// 0 => false
// "" => false
// "abc" => true
// null => false
// undefined => false

let someNumber = 33

let stringNumber = String(someNumber)
console.log(stringNumber);
console.log(typeof stringNumber);

// ******************** oPERATORS ***********************

let value = 3
let negValue = -value
console.log(value);

console.log(2+2);
console.log(2-2);
console.log(2*2);
console.log(2/2);
console.log(2%2); // modulus operator gives the remainde
console.log(2**3); // exponentiation operator gives the power


let str = "Hello"
let str_2 = "Nouman"
let str_3 = str + str_2
console.log(str_3);

let str1 = "Hello"
let str2 = "Nouman"
let strg  = str1 + " " + str2
console.log(strg);



let num1 = 2
let num2 = 3
let str4 = num1 + num2
console.log(str4);

// when we use + operator with string 
// it will concatenate the string but when 
// we use + operator with number it will add the number
let str5 = "2"
let str6 = "3"
let str7 = str5 + str6
// console.log(str7);
// here we are using + operator with string so it will
// concatenate the string and give us "23" as output
// but when we use + operator with number it will add the number and give us 5 as output
console.log(1 + "2"); 
console.log("1" + 2);
console.log("1" + "2");
console.log("1" + 2 + 2);
console.log(1 + 2 + "2");
console.log((3 + 4) * 5);
console.log(3 + 4 * 5 );

// here we are using comparison operators
console.log(3 > 4);
console.log(3 < 4);
console.log(3 >= 4);
console.log(3 <= 4);
console.log(3 == 4);
console.log(3 != 4);

// here we are using logical operators
console.log(true && true);
console.log(true && false);
console.log(false && true);
console.log(false && false);

console.log(true || true);
console.log(true || false);
console.log(false || true);
console.log(false || false);

console.log(!true);
console.log(!false);

// here we are using type coercion
console.log(true+1)
console.log(true+true)
console.log(false+false)
console.log(false+true)
console.log(true+false)
console.log(true+true+true)
console.log(+"")
console.log(+true)

// here we are using unary plus operator to convert the string to number
let gameCounter = 100
console.log(++gameCounter); // pre increment operator
console.log(gameCounter); // 101
// here we are using pre increment operator so it will
// first increment the value of gameCounter and then return the value of gameCounter
console.log(gameCounter++); // post increment operator
console.log(gameCounter); // 102
// 1. Primitive Data Types
// 2. Non-Primitive Data Types

// 1. Primitive Data Types
// 7 types: String, Number, Boolean, Null, Undefined, Symbol, BigInt

const score = 100;
const scoreValue = 100.3;
const isLoggedIn = true;
const outsideTemp = null;
const userEmail = undefined;
const id = Symbol('123');
const bigNumber = 123456789012345678901234567890n;




// 2. Non-Primitive Data Types (Reference Types)
// 3 types: Object, Array, Function

const familyMembers = ["Usama", "Noman", "Shanzay", "Usama"];
let familyDetails = {
    name: "Usama",
    age: 22,
    city: "Farooqabad",
}
let myFunction = function(){
    console.log("Hello World");
}

console.log(typeof familyDetails);
console.log(typeof bigNumber);
console.log(typeof myFunction);
console.log(typeof familyMembers);
console.log(typeof familyDetails);
console.log(typeof score);
console.log(typeof scoreValue);
console.log(typeof isLoggedIn);
console.log(typeof outsideTemp);
console.log(typeof userEmail);
console.log(typeof id);

// #1 Only with a variable
const message: string = 'Hello World!';
console.log(message);


// #2 With a function
const greetings = (nome: string): string => {
    return `Hello World, ${nome}`;
}

console.log(greetings('Leo'));
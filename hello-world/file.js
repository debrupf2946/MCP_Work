const fs = require('fs');
const os = require('os');

// fs.writeFileSync('hello.txt', 'Hello World',(err)=>{
//     if(err){
//         console.log(err);
//     }
// });



// // const content = fs.readFileSync('hello.txt', 'utf8');
// // console.log(content);

// fs.readFile('hello.txt', 'utf8', (err, data) => {
//     if(err){
//         console.log(err);
//     }
//     console.log(data);
// });

// fs.appendFileSync('hello.txt', `${Date.now()} Hello World\n`);

console.log(os.cpus().length);
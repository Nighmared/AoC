fs = require('fs');

let cont;

try{
	cont = fs.readFileSync('input.txt','utf8');
} catch(err){
	console.log(err);
}
//Part1
let result = 0;
const lines = cont.split("\n");
for(let i = 0; i<lines.length-1; i++){
	result += calcFuel(lines[i]);
}

console.log("Fuel needed (Part1): "+result);

result = 0;
for(let i = 0; i<lines.length-1; i++){
	let tmpRes = calcFuel(lines[i]);
	let currSum = 0;
	while(tmpRes>0){
		currSum+=tmpRes;
		tmpRes = calcFuel(tmpRes);
	}
	result += currSum;
}

console.log("Fuel needed (Part 2, with regard for fuel weight): "+result);



function calcFuel(mass){
	let out = Math.floor( mass/3);
	return out-2;
}
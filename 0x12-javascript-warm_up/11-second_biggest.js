#!/usr/bin/node
/* Script finds the maximum number in the list of arguments */

let argList = [];
if (!isNaN(process.argv[2])) {
  while (process.argv[i]) {
    argList.push(process.argv[i]);
    i++;
  }
  let maxNumber = Math.max(...argList);
  let args = argList.filter(argList => argList !== maxNumber);
  console.log(Math.max(args));
} else {
    console.log(0);
}

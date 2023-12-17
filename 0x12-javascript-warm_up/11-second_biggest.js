#!/usr/bin/node
/* Script finds the maximum number in the list of arguments */

const argList = [];
if (!isNaN(process.argv[2])) {
  let i = 2;
  while (process.argv[i]) {
    argList.push(process.argv[i]);
    i++;
  }
  const maxNumber = Math.max(...argList);
  const args = argList.filter(argList => argList != maxNumber);
  console.log(Math.max(...args));
} else {
  console.log(0);
}

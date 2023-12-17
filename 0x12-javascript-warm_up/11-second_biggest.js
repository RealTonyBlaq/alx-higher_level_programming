#!/usr/bin/node
/* Script finds the maximum number in the list of arguments */

const argList = [];
if (!isNaN(process.argv[2])) {
  let i = 2;
  while (process.argv[i]) {
    argList.push(Number(process.argv[i]));
    i++;
  }
  const maxNumber = Math.max(...argList);
  const args = argList.filter(argList => argList !== maxNumber);
  const secondMax = Math.max(...args);
  console.log(secondMax);
} else {
  console.log(0);
}

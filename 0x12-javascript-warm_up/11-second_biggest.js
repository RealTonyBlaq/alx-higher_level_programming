#!/usr/bin/node
/* Script finds the maximum number in the list of arguments */

let arg_list = [];
if (!isNaN(process.argv[2])) {
  while (process.argv[i]) {
    arg_list.push(process.argv[i]);
    i++;
  }
  let maxNumber = Math.max(...arg_list);
  let args = arg_list.filter(arg_list => arg_list !== maxNumber);
} else {
    console.log(0);
}

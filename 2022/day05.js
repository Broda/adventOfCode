let txt = document.getElementById("txt");
let lbl = document.getElementById("lbl");
let inFile = document.getElementById("inFile");

inFile.addEventListener("change", function () {
  let fr = new FileReader();
  fr.onload = function () {
    getAnswer(fr.result.trim());
  };

  fr.readAsText(this.files[0]);
});

function btn_click() {
  console.log(`${[4, 5, 6].includes(6)}`);
  getAnswer(txt.value);
}

function str_split(str) {
  return [str.slice(0, str.length / 2), str.slice(str.length / 2)];
}

function getStacks(stack_in) {
  let lines = stack_in.split("\n");
  let stacks = {};
  for (let i = 1; i <= 9; i++) stacks[i] = [];

  for (let r = lines.length - 2; r >= 0; r--) {
    for (let c = 0; c < lines[r].length; c++) {
      //if ([1,5,9,13,17,21,25,29,33].includes(c))
      if (c % 4 == 1) {
        let s = (c - 1) / 4 + 1;
        if (lines[r].charAt(c) != " ") stacks[s].push(lines[r].charAt(c));
      }
    }
  }
  return stacks;
}

function processCommand(stacks, cmd) {
  let [m, num, f, src, t, dest] = cmd.split(" ");
  //console.log(`num = ${num}, src = ${src}, dest = ${dest}`);
  for (let i = 0; i < num; i++) {
    let c = stacks[src].pop();
    stacks[dest].push(c);
  }
  return stacks;
}

function processCommandPart2(stacks, cmd) {
  let [m, num, f, src, t, dest] = cmd.split(" ");
  //console.log(`num = ${num}, src = ${src}, dest = ${dest}`);
  let start_index = stacks[src].length - num;
  console.log(
    `cmd: ${cmd}, src: ${stacks[src]}, dest: ${stacks[dest]}, src[${start_index}] = ${stacks[src][start_index]}`
  );
  for (let i = start_index; i < stacks[src].length; i++)
    stacks[dest].push(stacks[src][i]);
  for (let i = 0; i < num; i++) stacks[src].pop();

  return stacks;
}

function getAnswer(input) {
  let num1 = "";
  let num2 = "";
  let [stack_input, directions] = input.split("\n\n");
  //console.log(stack_input);
  let stacks = getStacks(stack_input);
  //console.log(stacks);
  directions.split("\n").forEach(function (s) {
    stacks = processCommand(stacks, s);
  });

  for (let i = 1; i <= 9; i++) {
    if (stacks[i].length > 0) num1 += stacks[i][stacks[i].length - 1];
  }

  stacks = getStacks(stack_input);
  directions.split("\n").forEach(function (s) {
    stacks = processCommandPart2(stacks, s);
  });

  for (let i = 1; i <= 9; i++) {
    if (stacks[i].length > 0) num2 += stacks[i][stacks[i].length - 1];
  }

  lbl.innerHTML += `<br/>Num1: ${num1}<br/>Num2: ${num2}`;
}

getAnswer(
  "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2"
);

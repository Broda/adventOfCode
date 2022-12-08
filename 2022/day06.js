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

function allDifferent(str) {
  //const re = /^(?:([A-Za-z])(?!.*\1))*$/;
  const re = /^.*(.).*\1.*$/;
  return !str.match(re);
}

function getMsgStart(str, len) {
  if (allDifferent(str.substring(0, len))) {
    return len;
  }
  for (let i = len; i < str.length; i++) {
    if (allDifferent(str.substring(i - len, i))) {
      return i;
    }
  }
}

function getAnswer(input) {
  let num1 = 0;
  let num2 = 0;

  input.split("\n").forEach(function (s) {
    num1 = getMsgStart(s, 4);
    num2 = getMsgStart(s, 14);
  });

  lbl.innerHTML += `<br/>Num1: ${num1}<br/>Num2: ${num2}`;
}

getAnswer("mjqjpqmgbljsphdztnvjfqwrcgsmlb");
getAnswer("bvwbjplbgvbhsrlpgdmjqwftvncz");
getAnswer("nppdvjthqldpwncqszvftbrmjlhg");
getAnswer("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg");
getAnswer("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw");

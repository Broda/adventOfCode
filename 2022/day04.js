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

function isRangeContained(rng1, rng2) {
  for (let i = 0; i < rng1.length; i++) {
    if (!rng2.includes(rng1[i])) {
      //console.log(`rng1[${i}]: ${rng1[i]}, rng2: ${rng2}`);
      return false;
    }
  }
  //console.log(`${rng1} in ${rng2}`);
  return true;
}

function rangeContainsAny(rng1, rng2) {
  for (let i = 0; i < rng1.length; i++) {
    if (rng2.includes(rng1[i])) return true;
  }
  return false;
}

function buildRange(rng) {
  let d = [];
  let [start, stop] = rng.split("-");
  for (let i = parseInt(start); i <= parseInt(stop); i++) {
    d.push(i);
  }
  return d;
}

function getAnswer(input) {
  let num1 = 0;
  let num2 = 0;
  //input format:
  //num-num,num-num

  input.split("\n").forEach(function (s) {
    let [r1, r2] = s.split(",");
    //console.log(`r1: ${r1}, r2: ${r2}`);
    let rng1 = buildRange(r1);
    let rng2 = buildRange(r2);
    //console.log(`rng1: ${rng1}, rng2: ${rng2}`);
    if (isRangeContained(rng1, rng2) || isRangeContained(rng2, rng1)) num1++;
    if (rangeContainsAny(rng1, rng2) || rangeContainsAny(rng2, rng1)) num2++;
  });

  lbl.innerHTML += `<br/>Num1: ${num1}<br/>Num2: ${num2}`;
}

getAnswer("2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8");

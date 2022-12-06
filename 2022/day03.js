let txt = document.getElementById("txt");
let lbl = document.getElementById("lbl");
let inFile = document.getElementById("inFile");

inFile.addEventListener("change", function () {
  let fr = new FileReader();
  fr.onload = function () {
    getAnswer(fr.result);
  };

  fr.readAsText(this.files[0]);
});

function getLetterPriority(c) {
  let code = c.charCodeAt();
  if (code <= 90)
    // A-Z
    return code - 38;
  else return code - 96;
}

function str_split(str) {
  return [str.slice(0, str.length / 2), str.slice(str.length / 2)];
}

function getSackDictionary(sack) {
  let d = {};
  sack.split("").forEach((c) => {
    if (!d.hasOwnProperty(c)) d[c] = getLetterPriority(c);
  });
  return d;
}

function getPriority(sack) {
  let half1 = str_split(sack)[0];
  let half2 = str_split(sack)[1];
  //console.log("sack: " + sack + ", half1: " + half1 + ", half2: " + half2);

  let h1 = getSackDictionary(half1);
  let h2 = getSackDictionary(half2);

  //console.log(h1);

  for (const [key, value] of Object.entries(h1)) {
    if (h2.hasOwnProperty(key)) return h2[key];
  }
}

function getGroupBadgeValue(g) {
  let sack1 = getSackDictionary(g[0]);
  let sack2 = getSackDictionary(g[1]);
  let sack3 = getSackDictionary(g[2]);

  while (true) {
    for (const [key, value] of Object.entries(sack1)) {
      if (sack2.hasOwnProperty(key) && sack3.hasOwnProperty(key)) {
        console.log("same key: " + key + ", value: " + sack1[key].toString());
        return sack1[key];
      }
    }
    for (const [key, value] of Object.entries(sack2)) {
      if (sack1.hasOwnProperty(key) && sack3.hasOwnProperty(key))
        return sack2[key];
    }
    for (const [key, value] of Object.entries(sack3)) {
      if (sack2.hasOwnProperty(key) && sack1.hasOwnProperty(key))
        return sack3[key];
    }
  }
}

function getAnswer(input) {
  let num1 = 0;
  let num2 = 0;

  let data = input.split("\n");
  let groups = [];
  let group = [];
  for (let i = 0; i < data.length; i++) {
    num1 += getPriority(data[i]);

    if (group.length < 3) {
      group.push(data[i]);
    } else {
      groups.push(group);
      console.log(group);
      group = [data[i]];
    }
  }
  if (group.length > 0) groups.push(group);

  console.log(groups.length.toString() + " groups");

  for (let i = 0; i < groups.length; i++) {
    num2 += getGroupBadgeValue(groups[i]);
  }

  lbl.innerHTML +=
    "<br/>Num1: " + num1.toString() + "<br/>Num2: " + num2.toString();
}

getAnswer(
  "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw"
);

String.prototype.format = String.prototype.f = function() {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};

function ab2Str(buf)
{
    return String.fromCharCode.apply(null, new Uint16Array(buf));
}

function str2ab(str)
{
    var buf = new ArrayBuffer(str.length*2); // 2 bytes for each char
    var bufView = new Uint16Array(buf);
    for (var i=0, strLen=str.length; i < strLen; i++) {
        bufView[i] = str.charCodeAt(i);
    }
    return buf;
}

function uint16(n)
{
    return n & 0xFFFF;
}

function sortNumAsc(a, b)
{
    return a - b;
}

function sortNumDesc(a, b)
{
    return b - a;
}

function btn_click()
{
    let t = document.getElementById('txt').value.trim()
    getAnswer(t);
    
}

let pAnswer = document.getElementById("answer");
let iFile = document.getElementById("inputfile");
iFile.addEventListener('change', function() {
    let fr = new FileReader();
    fr.onload = function() {
        getAnswer(fr.result);
    }
    fr.readAsText(this.files[0]);
});

function getAnswer(input)
{
    let num1 = 0;
    let num2 = 0;
    let elves = [];
    input.split('\n\n').forEach(function(s, i) {
        let elf = 0;
        s.split('\n').forEach(function(l, j) {
            elf += parseInt(l);
        });
        elves.push(elf);
        console.log("pushed {0}".format(elf));
    });

    elves.sort(sortNumDesc);
    num1 = elves[0];
    num2 = elves[0] + elves[1] + elves[2];

    pAnswer.innerHTML = pAnswer.innerHTML.concat('<br/>\n&nbsp;&nbsp;Num1={0}<br/>\n&nbsp;&nbsp;Num2={1}<br/>\n'.format(num1, num2));
}

getAnswer("1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000");
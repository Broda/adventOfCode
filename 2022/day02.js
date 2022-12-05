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

    let vals = {};
    vals['A'] = 1;
    vals['B'] = 2;
    vals['C'] = 3;
    vals['X'] = 1;
    vals['Y'] = 2;
    vals['Z'] = 3;

    let winVal = 6;
    let tieVal = 3;
    let loseVal = 0;

    let round = 0;
    input.split('\n').forEach(function(s, i) {
        round++;

        let opp = s.split(' ')[0];
        let you = s.split(' ')[1];
        num1 += vals[you];

        if (vals[opp] == vals[you])
            num1 += tieVal;
        else if ((opp == 'A' && you == 'Z') || (opp == 'B' && you == 'X') || (opp == 'C' && you == 'Y'))
            num1 += loseVal;
        else
            num1 += winVal;
        
        let you2 = '';
        if (you == 'X') // lose
        {
            num2 += loseVal;
            if (opp == 'A')
                num2 += vals['C'];
            else if (opp == 'B')
                num2 += vals['A'];
            else
                num2 += vals['B'];
        }
        else if (you == 'Y') // draw
        {
            num2 += tieVal;
            num2 += vals[opp];
        }
        else // win
        {
            num2 += winVal;
            if (opp == 'A')
                num2 += vals['B'];
            else if (opp == 'B')
                num2 += vals['C'];
            else
                num2 += vals['A'];
        }

        console.log('round {0}: {1}, {2}'.format(round, num1, num2));
    });

    pAnswer.innerHTML = pAnswer.innerHTML.concat('<br/>\n&nbsp;&nbsp;Num1={0}<br/>\n&nbsp;&nbsp;Num2={1}<br/>\n'.format(num1, num2));
}

getAnswer("A Y\nB X\nC Z");
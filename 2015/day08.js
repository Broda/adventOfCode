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

let pAnswer = document.getElementById("answer");
let iFile = document.getElementById("inputfile");
iFile.addEventListener('change', function() {
    let fr = new FileReader();
    fr.onload = function() {
        getAnswer(fr.result);
    }
    fr.readAsText(this.files[0]);
    //fr.readAsArrayBuffer(this.files[0]);
    //fr.readAsBinaryString(this.files[0]);
});

function getAnswer(input)
{
    //console.log(input);
    //let lines = input.split('\n');
    let num1 = 0;
    let num2 = 0;
    input.split('\n').forEach(function(s, i) {
        let cc = countCodeChars(s);
        let mc = countMemChars(s);
        console.log('{0} -> {1} - {2} = {3}'.format(s, cc, mc, cc-mc));
        num1 += cc - mc;
    });

    pAnswer.innerHTML = pAnswer.innerHTML.concat('<br/>\n&nbsp;&nbsp;Num1={0}<br/>\n&nbsp;&nbsp;Num2={1}<br/>\n'.format(num1, num2));
}

function countCodeChars(s)
{
    let count = s.length;
    let re = /^".*(").*"$/g;
    //count += (s.match(re) || []).length;
    return count;
}

function countMemChars(s)
{
    let newS = s.substring(1,s.length-2);
    console.log(newS);
    newS = replaceHexChars(newS);
    let count = newS.length;
    let re = /(\\x..)/g;
    let hexCount = (s.match(re) || []).length * 3;
    re = /(\\")/g;
    let quoteCount = (s.match(re) || []).length;
    re = /(\\\\)/g;
    let dblSlashCount = 0;
    return count - hexCount - quoteCount - dblSlashCount;
}

function replaceHexChars(s)
{
    let re = /(\\x(..))/;
    console.log('{0} -> {1}'.format(s, s.replace(re, '\\u$2')));
    return s.replace(re, '\\u$2');
}

function btn_click()
{
    let t = document.getElementById('txt').value.trim()
    //pAnswer.innerHTML = pAnswer.innerHTML.concat('<br/>\n{0}'.format(t));
    getAnswer(t);
    
}

//getAnswer(document.getElementById('data').innerText.trim());

// getAnswer('""'); // 2 code chars - 0 mem chars = 2
// getAnswer('"abc"'); // 5 code chars - 3 mem chars = 2
// getAnswer('"aaa\"aaa"'); // 10 code chars - 7 mem chars = 3
// getAnswer('"\x27"'); // 6 code chars - 1 mem char = 5
// getAnswer('""\n"abc"\n"aaa\\"aaa"\n"\x27"'); // 2 + 2 + 3 + 5 = 12
// getAnswer('"v\xfb\"lgs\"kvjfywmut\x9cr"');

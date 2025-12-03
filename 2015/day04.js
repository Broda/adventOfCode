String.prototype.format = String.prototype.f = function() {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};

let pAnswer = document.getElementById("answer");

function getAnswer(input)
{
    let num = 0;
    while (true) {
        let test = md5(input + num);
        if (test.startsWith('000000')) break;
        
        num++;
    }

    pAnswer.innerHTML = pAnswer.innerHTML.concat('<br/>\n&nbsp;&nbsp;Num={0}<br/>\n<br/>\n'.format(num));
}

//getAnswer("abcdef");
//getAnswer("pqrstuv");
getAnswer("iwrupvqb"); // actual input
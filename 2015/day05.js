String.prototype.format = String.prototype.f = function() {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};

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
    let data = input.split("\n");

    for (let i = 0; i < data.length; i++)
    {
        if (stringIsNice1(data[i])) num1++;
        if (stringIsNice2(data[i])) num2++;
        
    }

    pAnswer.innerHTML = pAnswer.innerHTML.concat('<br/>\n&nbsp;&nbsp;Num1={0}<br/>\nNum2={1}<br/>\n'.format(num1, num2));
}

function stringIsNice1(s)
{
    let bad = ['ab', 'cd', 'pq', 'xy'];
    for (let b = 0; b < bad.length; b++)
    {
        if (s.includes(bad[b])) 
        {
            //console.log('{0} is bad as it includes {1}'.format(s, bad[b]));
            return false;
        }
    }

    let vowels = s.match(/[aeiou]/g) || [];
    if (vowels.length < 3) 
    {
        //console.log('{0} is bad as it doesn\'t contain 2 vowels'.format(s))
        return false;

    }
    
    let twiceInRow = s.match(/(.)\1/g) || [];
    if (twiceInRow.length == 0) 
    {
        //console.log('{0} is bad as it doesn\'t contain 2 in a row'.format(s))
        return false;
    }

    // nice so show values found
    console.log('{0} is nice'.format(s));
    console.log('vowels: [{0}]'.format(vowels));
    console.log('twiceInRow matches: {0}'.format(twiceInRow));

    return true;
}

function stringIsNice2(s)
{
    if (!findDupePairs(s)) return false;

    let repeatWithOneBetween = s.match(/((.).\2)/g) || [];
    if (repeatWithOneBetween.length == 0) return false;

    // nice so show values found
    console.log('{0} is nice'.format(s));
    console.log('repeats: {0}'.format(repeatWithOneBetween));

    return true;
}

function findDupePairs(s)
{
    //console.log('findDupePairs({0})'.format(s));
    for (let i = 0; i < s.length - 2; i++)
    {
        let pair = s.substring(i, i+2);
        let before = s.substring(0, i);
        let after = s.substring(i+2);
        //console.log('i = {3}\npair = "{0}"\nbefore = "{1}"\nafter="{2}"'.format(pair, before, after, i));

        if (before.includes(pair)) 
        {
            //console.log('{0} contains {1}'.format(before, pair));
            return true;
        }    
        if (after.includes(pair)) 
        {
            //console.log('{0} contains {1}'.format(after, pair));
            return true;
        }
    }

    return false;
}

getAnswer("qjhvhtzxzqqjkmpb"); // nice
getAnswer("xxyxx"); // nice
getAnswer("uurcxstgmygtbstg"); // naughty
getAnswer("ieodomkazucvgmuy"); // naughty
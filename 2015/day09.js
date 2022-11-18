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
    let nodes = {};

    let num1 = 0;
    let num2 = 0;
    input.split('\n').forEach(function(s, i) {
        let aSplit = s.split(' ');
        let c1 = aSplit[0];
        let c2 = aSplit[2];
        let dist = parseInt(aSplit[4]);
        nodes[c1] = {name: c1, dest: {}, visited: false};
        nodes[c1].dest[c2] = dist;
    });

    console.log(getNodesString(nodes, true));
    pAnswer.innerHTML = pAnswer.innerHTML.concat(getNodesString(nodes, true));

    pAnswer.innerHTML = pAnswer.innerHTML.concat('<br/>\n&nbsp;&nbsp;Num1={0}<br/>\n&nbsp;&nbsp;Num2={1}<br/>\n'.format(num1, num2));
}

function getNodesString(nodes, bHtml = false)
{
    let s = '';
    for (let n in nodes)
    {
        s += getNodeString(nodes[n], false) + '\n';
    }
    if (bHtml)
        s = s.replace('\n', '<br/>\n');
    return s;
}

function getNodeString(node, bHtml = false)
{
    let s = '{0}\n{1}\n'.format(node.name, getNodeDestString(node));
    if (bHtml)
        s = s.replace('\n', '<br/>\n');
    return s;
}

function getNodeDestString(node)
{
    let s = '';
    for (let k in node.dest)
    {
        s += '-> {0} = {1}\n'.format(k, node.dest[k]);
    }
    return s;
}

getAnswer("London to Dublin = 464\nLondon to Belfast = 518\nDublin to Belfast = 141");
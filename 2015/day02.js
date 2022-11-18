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
    const arr = input.split("\n");
    let sqft = 0;
    let ribbon = 0;

    for (let i = 0; i < arr.length; i++)
    {
        let vals = arr[i].split("x").map(v => {return parseInt(v);}).sort((a,b) => {return a-b;});
        
        let dims = [vals[0]*vals[1], vals[0]*vals[2], vals[1]*vals[2]].sort((a,b) => {return a-b;});
        let sa = getSurfaceArea(vals[0], vals[1], vals[2]) + dims[0];
        sqft += sa;
        
        ribbon += 2 * (vals[0] + vals[1]) + (vals[0]*vals[1]*vals[2]);
    }
    
    pAnswer.innerHTML = pAnswer.innerHTML.concat('<br/>\n&nbsp;&nbsp;sqft={0}<br/>\n&nbsp;&nbsp;ribbon={1}<br/>\n'.format(sqft, ribbon));
}

function getSurfaceArea(l, w, h)
{
    return 2 * (l * w + l * h + w * h);
}

getAnswer("2x3x4");
getAnswer("1x1x10");
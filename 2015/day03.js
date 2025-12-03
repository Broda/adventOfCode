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

class House {
    constructor(addr) {
        this.x = addr[0];
        this.y = addr[1];
        this.count = 1;
    }

    equals(h) {
        return (h.x === this.x && h.y === this.y);
    }
}

function getAnswer(input)
{
    let currAddr = [0,0];
    let currAddrRobo = [0,0];
    let houses = [new House(currAddr)];
    houses[0].count++;
    let dirs = input.split('');
    let santa = true;

    for (let i = 0; i < dirs.length; i++) {
        if (santa === true)
        {
            switch (dirs[i])
            {
                case '>':
                    currAddr[0]++;
                    break;
                case '<':
                    currAddr[0]--;
                    break;
                case '^':
                    currAddr[1]++;
                    break;
                case 'v':
                    currAddr[1]--;
                    break;
            }

            let h = getHouse(houses, currAddr);
            if (h === undefined)
                houses.push(new House(currAddr));
            else
                h.count++;
        } else {
            switch (dirs[i])
            {
                case '>':
                    currAddrRobo[0]++;
                    break;
                case '<':
                    currAddrRobo[0]--;
                    break;
                case '^':
                    currAddrRobo[1]++;
                    break;
                case 'v':
                    currAddrRobo[1]--;
                    break;
            }

            let h = getHouse(houses, currAddrRobo);
            if (h === undefined)
                houses.push(new House(currAddrRobo));
            else
                h.count++;
        }
        santa = !santa;
    }

    let numHouses = houses.length;
    pAnswer.innerHTML = pAnswer.innerHTML.concat('<br/>\n&nbsp;&nbsp;Num Houses={0}<br/>\n<br/>\n'.format(numHouses));
}

function getHouse(arrHouses, x, y)
{
    return getHouse(arrHouses, [x,y]); //arrHouses.find(h => h.equals(new Houses([x, y])));
}

function getHouse(arrHouses, addr) {
    return arrHouses.find(h => h.equals(new House(addr)));
}

getAnswer("^v");
getAnswer("^>v<");
getAnswer("^v^v^v^v^v");
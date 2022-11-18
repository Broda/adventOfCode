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

const MAX_ROWS = 1000;
const MAX_COLS = 1000;

function getAnswer(input)
{
    let grid = initGrid(MAX_ROWS, MAX_COLS);

    let instructions = input.split('\n');
    for (let i = 0; i < instructions.length; i++)
    {
        parseInstruction(grid, instructions[i]);
    }

    let num1 = countLightsOn(grid);
    let num2 = sumBrightness(grid);
    pAnswer.innerHTML = pAnswer.innerHTML.concat('<br/>\n&nbsp;&nbsp;Num1={0}<br/>\nNum2={1}<br/>\n'.format(num1, num2));
}

function parseInstruction(grid, sInstruction)
{
    let aTemp = '';
    let func = null;
    let row1 = 0, col1 = 0, row2 = 0, col2 = 0;
    if (sInstruction.startsWith('turn on '))
    {
        aTemp = sInstruction.substring('turn on '.length).split(' through ');
        func = turnOnLights;
        
    }
    else if (sInstruction.startsWith('turn off '))
    {
        aTemp = sInstruction.substring('turn off '.length).split(' through ');
        func = turnOffLights;
    }
    else if (sInstruction.startsWith('toggle '))
    {
        aTemp = sInstruction.substring('toggle '.length).split(' through ');
        func = toggleLights;
    }

    row1 = parseInt(aTemp[0].split(',')[0]);
    col1 = parseInt(aTemp[0].split(',')[1]);
    row2 = parseInt(aTemp[1].split(',')[0]);
    col2 = parseInt(aTemp[1].split(',')[1]);
    func(grid, row1, col1, row2, col2);
}

function initGrid(rows, cols)
{
    return Array(rows).fill().map(() => Array(cols).fill(0));
}

function printGrid(grid)
{
    let sGrid = '<br/>\n<br/>\n';
    for (let i = 0; i < MAX_ROWS; i++)
    {
        let sRow = '';
        for (let j = 0; j < MAX_COLS; j++)
        {
            sRow += '{0}'.format(grid[i][j]);
        }
        sGrid += sRow + '<br/>\n';
    }

    pAnswer.innerHTML = pAnswer.innerHTML.concat(sGrid);
}

function countLightsOn(grid)
{
    let sum = 0;
    for (let i = 0; i < MAX_ROWS; i++)
    {
        for (let j = 0; j <= MAX_COLS; j++)
        {
            if (grid[i][j] > 0) sum++;
        }
    }
    return sum;
}

function sumBrightness(grid)
{
    let sum = 0;
    for (let i = 0; i < MAX_ROWS; i++)
    {
        for (let j = 0; j < MAX_COLS; j++)
        {
            sum += grid[i][j];
        }
    }
    return sum;
}

function turnOnLights(grid, row1, col1, row2, col2)
{
    for (let i = row1; i <= row2; i++)
    {
        for (let j = col1; j <= col2; j++)
        {
            grid[i][j]++;
        }
    }
}

function turnOffLights(grid, row1, col1, row2, col2)
{
    for (let i = row1; i <= row2; i++)
    {
        for (let j = col1; j <= col2; j++)
        {
            grid[i][j]--;
            if (grid[i][j] < 0) grid[i][j] = 0;
        }
    }
}

function toggleLights(grid, row1, col1, row2, col2)
{
    for (let i = row1; i <= row2; i++)
    {
        for (let j = col1; j <= col2; j++)
        {
            grid[i][j] += 2;
        }
    }
}


//getAnswer('turn on 0,0 through 999,999');
//getAnswer('toggle 0,0 through 999,0');
//getAnswer('turn off 499,499 through 500,500');
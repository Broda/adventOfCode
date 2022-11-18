String.prototype.format = String.prototype.f = function() {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};

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
});

function getAnswer(input)
{
    let lines = input.split('\n');
    let wires = {};
    let values = {};
    for (let i = 0; i < lines.length; i++)
    {
        let wire = lines[i].split(' -> ');
        wires[wire[1].trim()] = wire[0].trim();
        if (isNumber(wire[0].trim()))
        {
            wires[wire[1].trim()] = parseInt(wire[0].trim());
            values[wire[1].trim()] = wires[wire[1].trim()];
        }
    }

    // part 2
    wires['b'] = 16076;
    values['b'] = 16076;

    printWires(wires);
    printWires(values);

    let c = 0;
    while (Object.keys(values).length < Object.keys(wires).length)
    {
        replaceValueWires(wires, values);
        processAvailableWires(wires, values);
        updateValueWires(wires, values);
        //printWires(wires);
        printWires(values);
        c++;
        if (c > 250) 
        {
            console.log("{0} < {1}".format(Object.keys(values).length, Object.keys(wires).length));
            console.log("BREAK!");
            break;
        }
        
    }
    
    return;

    let count = 0;
    //printWires(wires);
    while(true)
    {
        count++;
        console.log('iteration {0}'.format(count));

        let allValues = true;

        for (let k in wires)
        {
            if (hasInstruction(wires[k]))
            {
                let func = parseInstruction(wires[k]);
                func(wires, k);
            }
            if (hasInstruction(wires[k])) allValues = false;
        }

        if (allValues) break;
    }
    
    printWires(wires);

    let num1 = 0;
    pAnswer.innerHTML = pAnswer.innerHTML.concat('<br/>\n&nbsp;&nbsp;Num1={0}<br/>\n<br/>\n'.format(num1));
}

function isNumber(val)
{
    if (val == undefined) return false;
    if (isNaN(val)) return false;
    if (val == null) return false;
    if (isNaN(parseInt(val))) return false;
    return isFinite(parseInt(val));
}

function updateValueWires(sWires, sValueWires)
{
    for (let k in sWires)
    {
        if (isNumber(sWires[k]) && !(k in sValueWires))
        {
            sValueWires[k] = parseInt(sWires[k]);
            sWires[k] = parseInt(sWires[k]);
        }
    }
}

function replaceValueWires(sWires, sValueWires)
{
    for (let k in sWires)
    {
        if (!isNumber(sWires[k]))
            sWires[k] = replaceWiresInInstruction(sValueWires, sWires[k]);
    }
}

function replaceWiresInInstruction(sWires, sInstruction)
{
    let aVals = sInstruction.split(' ');
    for (let v = 0; v < aVals.length; v++)
    {
        if (aVals[v] in sWires)
            aVals[v] = sWires[aVals[v]];
    }
    return aVals.join(' '); 
}

function processAvailableWires(sWires, sValueWires)
{
    for (let k in sWires)
    {
        if (instructionHasWires(sWires, sWires[k]) || isNumber(sWires[k])) continue;

        console.log('find func for "{0}"'.format(sWires[k]));
        let func = parseInstruction(sWires[k]);
        if (func != null)
            func(sWires, k);
        else
        {
            console.log('func is null for wire[{0}] = {1}'.format(k, sWires[k]));
            throw new Error('');
        }
    }
}

function hasInstruction(sInstruction)
{
    try {
        return isNaN(parseInt(sInstruction)) || sInstruction.includes(' '); // parseInt will return an int if it starts with one
    }
    catch{
        return false;
    }
}

function isValue(sInstruction)
{
    if (isFinite(sInstruction)) return true;
    console.log('isValue({0})'.format(sInstruction));
    return !sInstruction.includes(' ') && !isNaN(parseInt(sInstruction)); // !hasInstruction(sInstruction);
}

function processWire(sWires, sWire)
{
    let instruction = sWires[sWire];
    sWires[sWire] = replaceWiresInInstruction(sWires, instruction);
}

function instructionHasWires(sWires, sInstruction)
{
    if (isNumber(sInstruction)) return false;
    let aVals = sInstruction.split(' ');
    for (let v = 0; v < aVals.length; v++)
    {
        if (aVals[v] in sWires) 
        {
            //console.log('instructionHasWires({2}) -> aVals[{0}] = {1}, in sWires'.format(v, aVals[v], sInstruction));
            return true;
        }
    }
    console.log('no wires! {0}'.format(sInstruction));
    return false;
    
}


function replaceWires(sWires)
{
    for (let k in sWires)
    {
        console.log('{0} = {1}'.format(k, sWires[k]));
        let aVals = sWires[k].split(' ');
        let sNewVal = '';
        for (let v = 0; v < aVals.length; v++)
        {
            let sVal = aVals[v];
            console.log('sVal = "{0}"'.format(sVal));
            if (sNewVal.length > 0) sNewVal += ' ';
            if (sVal in sWires)
            {
                sNewVal += '{0}'.format(sWires[sVal]);
            }
            else
            {
                sNewVal += '{0}'.format(sVal);
            }
        }
        sWires[k] = sNewVal;
    }
    //if (circuitHasWires(sWires)) replaceWires(sWires);
}

function circuitHasWires(sWires)
{
    for (let k in sWires)
    {
        if (isNumber(sWires[k])) continue;

        let aVals = sWires[k].split(' ');
        for (let v = 0; v < aVals.length; v++)
        {
            if (aVals[v] in sWires) return true;
        }
    }
    return false;
}

function parseInstruction(sInstruction)
{
    if (sInstruction.includes('AND'))
        return doAnd;
        if (sInstruction.includes('OR'))
        return doOr;
    if (sInstruction.includes('NOT'))
        return doNot;
    if (sInstruction.includes('LSHIFT'))
        return doLShift;
    if (sInstruction.includes('RSHIFT'))
        return doRShift;

    // if we get here and there is an instruction it must be [wire] = wire, so Set
    if (hasInstruction(sInstruction))
        return doSet;

    console.log('parseInstruction({0})'.format(sInstruction));
    return null;
}

function doSet(sWires, sWire)
{
    let sOrigWire = sWires[sWire];
    if (isValue(sWires[sOrigWire]))
    {
        sWires[sWire] = sWires[sOrigWire];
        return true;
    }
    else
        return false;
}

function doAnd(sWires, sWire)
{
    let aSplit = sWires[sWire].split('AND');
    let sLeft = aSplit[0].trim();
    let sRight = aSplit[1].trim();
    if (!isValue(sLeft)) sLeft = sWires[sLeft];
    if (!isValue(sRight)) sRight = sWires[sRight];
    if (isValue(sLeft) && isValue(sRight))
    {
        sWires[sWire] = parseInt(sLeft) & parseInt(sRight);
        return true;
    }
    else
        return false;
}

function doOr(sWires, sWire)
{
    let aSplit = sWires[sWire].split(' OR ');
    let sLeft = aSplit[0];
    let sRight = aSplit[1];
    if (!isValue(sLeft)) sLeft = sWires[sLeft];
    if (!isValue(sRight)) sRight = sWires[sRight];
    if (isValue(sLeft) && isValue(sRight))
    {
        sWires[sWire] = parseInt(sLeft) | parseInt(sRight);
        return true;
    }
    else
        return false;
}

function doNot(sWires, sWire)
{
    let sOrigWire = sWires[sWire].substring('NOT '.length);
    if (isValue(sOrigWire))
    {
        sWires[sWire] = uint16(~parseInt(sOrigWire));
        return true;
    }
    else
        return false;
}

function doLShift(sWires, sWire)
{
    let aSplit = sWires[sWire].split(' LSHIFT ');
    let sOrigWire = aSplit[0];
    let iShiftAmt = aSplit[1];
    if (isValue(sOrigWire))
    {
        iShiftAmt = parseInt(iShiftAmt);
        sWires[sWire] = parseInt(sOrigWire) << iShiftAmt;
    }
    else
        return false;
}

function doRShift(sWires, sWire)
{
    let aSplit = sWires[sWire].split(' RSHIFT ');
    let sOrigWire = aSplit[0];
    let iShiftAmt = aSplit[1];
    if (isValue(sOrigWire))
    {
        iShiftAmt = parseInt(iShiftAmt);
        sWires[sWire] = parseInt(sOrigWire) >> iShiftAmt;
    }
    else
        return false;
}

function printWires(wires)
{
    let sWires = '<br/>\n<br/>\n';
    for (let key in wires)
    {
        sWires += '[{0}] = {1}<br/>\n'.format(key, wires[key]);
    }
    pAnswer.innerHTML = pAnswer.innerHTML.concat(sWires);
    printNewline();
}

function printNewline()
{
    pAnswer.innerHTML = pAnswer.innerHTML.concat('<br/>\n');
}

//getAnswer('123 -> x\n456 -> y\nx AND y -> d\nx OR y -> e\nx LSHIFT 2 -> f\ny RSHIFT 2 -> g\nh -> aa\nNOT x -> h\nNOT y -> i');

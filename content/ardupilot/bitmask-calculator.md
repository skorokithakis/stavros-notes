# Bitmask calculator

<style>
    div.box{
        width: 90%;
    }
    table {
        border: 1px solid #222;
    }
</style>

<script type="text/javascript">
// 1660392804
var bitmaskDescArr = [];

function dec2bin(dec) {
    return reverse((dec >>> 0).toString(2));
}
function reverse(str) {
    return str.split("").reverse().join("");
}

async function loadBitmask(){
    // using the function:
    removeAll(document.getElementById('paramSelect'));

    url = document.getElementById("built").value;
    console.log("fetching: "+ url);
    if (url == ""){
        return;
    }

    const response = await fetch(url,{
        method: 'GET',
        headers: {
            'Content-Type': 'text/plain'
        }
    })
    .then(response => response.text())
    .then(data => {
        const parser = new DOMParser();
        const xml = parser.parseFromString(data, "application/xml");

        var params = xml.getElementsByTagName("param");
        console.log("retrieved "+ params.length +" params")
        for (var i = 0; i < params.length; i++) {
            var param = params[i].attributes.name.nodeValue;		//works, param name
            param = param.replace("ArduPlane:","");

            if(params[i].childNodes[1]){
                if( typeof params[i].childNodes[1].attributes.name == "object"){
                    if(params[i].childNodes[1].attributes.name.nodeValue && params[i].childNodes[1].attributes.name.nodeValue == "Bitmask"){

                        var bitmaskDescTxt = params[i].textContent.trim();
                        bitmaskDescArr[param] = bitmaskDescTxt.split(',');
                    }
                }
            }
        }

    })
    .catch(console.error);

    // console.log(bitmaskDescArr.length);
    drawSelect();
}


function drawSelect(){
    bitmaskDescArr.sort();
    Object.keys(bitmaskDescArr)
    .sort()
    .forEach(function(p, i) {
    // console.log(p);
        var el = document.createElement("option");
        el.textContent = p;
        el.value = p;
        document.getElementById("paramSelect").appendChild(el);

    });
}

function removeAll(selectBox) {
    while (selectBox.options.length > 0) {
        selectBox.remove(0);
    }
}

function bitbox(bit){
    dec = parseInt(document.getElementById("decimal").value);
    if(!dec ){dec = parseInt(0);}

    if(document.getElementById(bit).checked == true){
        dec += parseInt(bit);
    }else{
        dec -= parseInt(bit);
    }
    document.getElementById("decimal").value = dec;
    parseBitmask();
}

function parseBitmask() {
    console.log("found "+Object.keys(bitmaskDescArr).length+" bitmask parameters");

    document.getElementById("result").innerHTML="";
    var tbl = document.createElement('table');
    tbl.style="border: 1px solid black; width: 100%";
    var tbdy = document.createElement('tbody');

    dec = document.getElementById("decimal").value;
    binary=dec2bin(document.getElementById("decimal").value);
    if(!binary){binary = parseInt(0);}
    if(!dec ){dec = parseInt(0);}
    var param = document.getElementById("paramSelect").value;

    for (var bit = 0; bit < bitmaskDescArr[param].length; bit++) {
        var val = binary[bit];

        var tr = document.createElement('tr');

        var td = document.createElement('td');
        td.style="border: 1px solid black;";
        var singleBitDecvalue = Math.pow(2,bit);	// convert the bit to a decimal
        var checkbox = document.createElement('input');
        checkbox.type = "checkbox";
        checkbox.name = "name";
        checkbox.value = "checked";
        checkbox.id = singleBitDecvalue;
        checkbox.setAttribute("onclick","bitbox("+singleBitDecvalue+")");

        if (val == "1"){
            checkbox.checked = true;
        }else{
            checkbox.checked = false;
        }
        td.appendChild(checkbox);
        tr.appendChild(td);


        var td = document.createElement('td');
        td.appendChild(document.createTextNode(bitmaskDescArr[param][bit]));

        if (val == "1"){
            td.style  = "border: 1px solid black; color: green";
        }else{
            td.style  = "border: 1px solid black; color: red";
        }
        tr.appendChild(td);

        var td = document.createElement('td');
        td.style="border: 1px solid black; color: grey";
        td.appendChild(document.createTextNode(Math.pow(2,bit)));
        tr.appendChild(td);

        tbdy.appendChild(tr);
        tbl.appendChild(tbdy);
    }
     document.getElementById("result").appendChild(tbl);
}


</script>

<div class="box">
    <div id="input">
        <select id="built" onChange="loadBitmask();">
            <option value='https://arducustom.github.io/v/dev/ArduPlane/apm.pdef.xml'>ArduCustom Plane master</option>
            <option value='https://arducustom.github.io/v/10.0/ArduPlane/apm.pdef.xml'>ArduCustom Plane v10</option>
            <option value='https://arducustom.github.io/v/9.0/ArduPlane/apm.pdef.xml'>ArduCustom Plane v9.0</option>
        </select>
        <select id="paramSelect" onChange="parseBitmask();">
        </select>
        <input type="text" id="decimal" value="1" oninput="parseBitmask();">
    </div>
    <br>
    <div id="result">
    </div>
</div>
<script type="text/javascript">
    loadBitmask();
</script>

_(Many thanks to mfoos for writing this note.)_


* * *

<p style="font-size:80%; font-style: italic">
Last updated on August 13, 2022. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>

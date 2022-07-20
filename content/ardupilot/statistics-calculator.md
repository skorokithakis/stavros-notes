# Statistics calculator

<script type="text/javascript">
    function raw(val){
    		return val;
    	}
    	function ms_to_kph(val){
    		return parseInt(val*3.6);
    	}
    	function m_to_km(val){
    		return (val/1000).toFixed(2);
    	}
    	function sec_to_min(val){
    		return parseInt(val/60);
    	}
    
    
    	function parseStats() {
    
    		var stats = {
    			"STAT_ASPD_AVG":    { func: "ms_to_kph", "text": "Average air speed", "unit": "km/h"},
    			"STAT_ASPD_MAX":    { func: "ms_to_kph", "text": "Maximum air speed", "unit": "km/h"},
    			"STAT_GSPD_AVG":    { func: "ms_to_kph", "text": "Average ground speed", "unit": "km/h"},
    			"STAT_GSPD_MAX":    { func: "ms_to_kph", "text": "Maximum ground speed", "unit": "km/h"},
    			"STAT_WSPD_AVG":    { func: "ms_to_kph", "text": "Average wind speed", "unit": "km/h"},
    			"STAT_WSPD_MAX":    { func: "ms_to_kph", "text": "Maximum wind speed", "unit": "km/h"},
    			"STAT_TRAVEL_AIR":  { func: "m_to_km", "text": "Air distance traveled", "unit": "km"},
    			"STAT_TRAVEL_GND":  { func: "m_to_km", "text": "Ground distance traveled", "unit": "km"},
    			"STAT_HOMEALT_MAX": { func: "raw", "text": "Maximum altitude relative to home", "unit": "m"},
    			"STAT_HOMEDST_MAX": { func: "m_to_km", "text": "Maximum distance from home", "unit": "km"},
    			"STAT_CURRENT_AVG": { func: "raw", "text": "Average current", "unit": "A"},
    			"STAT_CURRENT_MAX": { func: "raw", "text": "Maximum current", "unit": "A"},
    			"STAT_POWER_AVG":   { func: "raw", "text": "Average power", "unit": "W"},
    			"STAT_POWER_MAX":   { func: "raw", "text": "Maximum power", "unit": "W"},
    			"STAT_FLT_ENERGY":  { func: "raw", "text": "Consumed energy", "unit": "Wh"},
    			"STAT_RUN_TIME":    { func: "sec_to_min", "text": "Total run time", "unit": "minutes"},
    			"STAT_FLT_TIME":    { func: "sec_to_min", "text": "Total flight time", "unit": "minutes"}
    		};
    
    		document.getElementById("result").innerHTML=""
    		var txt = document.getElementById("stats").value
    		var tbl = document.createElement('table');
    		var tbdy = document.createElement('tbody');
    
    		for (const key in stats){
    			var tr = document.createElement('tr');
    			// find the parameter in the textblock
    			var re = new RegExp(`${key}([^\D+])(.+)`,'g')
    			var matches = txt.match(re) +''
    			// extract the value
    			var value = matches.match(/\d+/)
    			var desc = stats[key]['text']
    			var unit = stats[key]['unit']
    			var func = stats[key]['func']
    			// run the defined function with the value
    			var out = window[func](value);
    
    			var td = document.createElement('td');
    			td.appendChild(document.createTextNode(desc))
    			tr.appendChild(td)
    
    			var td = document.createElement('td');
    			td.appendChild(document.createTextNode(out + " "+ unit))
    			td.style = "text-align:right"
    			tr.appendChild(td)
    
    			//save output for average calculations
    			stats[key]['out'] = out
    
    			tbdy.appendChild(tr);
    		}
    		tbl.appendChild(tbdy);

    	    var tr = document.createElement('tr');
    		var td = document.createElement('td');
            td.appendChild(document.createTextNode("Average air efficiency"))
            tr.appendChild(td)

    		var td = document.createElement('td');
            td.appendChild(document.createTextNode((stats["STAT_FLT_ENERGY"]["out"]/stats["STAT_TRAVEL_AIR"]["out"]).toFixed(2) + " Wh/km"))
    		td.style = "text-align:right"
            tr.appendChild(td)
    	    tbdy.appendChild(tr);

    	    var tr = document.createElement('tr');
    		var td = document.createElement('td');
            td.appendChild(document.createTextNode("Average flight time efficiency"))
            tr.appendChild(td)

    		var td = document.createElement('td');
            td.appendChild(document.createTextNode(((stats["STAT_FLT_TIME"]["out"]*60)/stats["STAT_FLT_ENERGY"]["out"]).toFixed(2) + " s/Wh"))
    		td.style = "text-align:right"
            tr.appendChild(td)
    	    tbdy.appendChild(tr);

			var tr = document.createElement('tr');
			var td = document.createElement('td');
    	    td.appendChild(document.createTextNode("Average flight efficiency"))
        	tr.appendChild(td)

			var td = document.createElement('td');
        	td.appendChild(document.createTextNode((stats["STAT_FLT_ENERGY"]["out"]/(stats["STAT_FLT_TIME"]["out"])).toFixed(2) + " Wh/min"))
			td.style = "text-align:right"
    	    tr.appendChild(td)
	    	tbdy.appendChild(tr);

    		document.getElementById("result").appendChild(tbl)
    	}
</script>

Paste your `STATS` items (you can get them with `parachute show -f STAT_`) here:

<div><textarea id="stats" name="text" cols="30" rows="8">
STAT_ASPD_AVG    15.243167
STAT_ASPD_MAX    36.461681
STAT_BOOT_CNT    65.000000
STAT_CURRENT_AVG 3.061170
STAT_CURRENT_MAX 11.686898
STAT_FLT_CNT     18.000000
STAT_FLT_ENERGY  118.639687
STAT_FLT_TIME    12486.000000
STAT_GSPD_AVG    14.964579
STAT_GSPD_MAX    37.131924
STAT_HOMEALT_MAX 2456.000000
STAT_HOMEDST_AVG 104.000000
STAT_HOMEDST_MAX 3796.000000
STAT_LOAD        0.000000
STAT_POWER_AVG   36.397156
STAT_POWER_MAX   136.568756
STAT_RESET       1.000000
STAT_RUN_TIME    27828.000000
STAT_TRAVEL_AIR  189796.000000
STAT_TRAVEL_GND  186942.000000
STAT_WSPD_AVG    4.371937
STAT_WSPD_MAX    18.140949
</textarea></div>

<div><input type="button" id="do" value="format" onclick="parseStats();"></div>
<div id="result"></div>


_(Many thanks to mfoos for writing this note.)_

* * *

<p style="font-size:80%; font-style: italic">
Last updated on July 20, 2022. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>

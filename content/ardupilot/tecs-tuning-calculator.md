+++
title = "TECS tuning calculator"
weight = 7
sort_by = "weight"
insert_anchor_links = "right"
+++
To use this calculator, first follow the steps in [Tuning the TECS](../../ardupilot/tuning-the-tecs).

<script>
    function kmhToMs(kmh) { return Math.round(kmh / 3.6); }
    function kmhToCms(kmh) { return Math.round(kmh / 0.036); }

	function calculateParameters(event) {
		var maxSpeed = Number(document.getElementById("maxSpeed").value);
		var maxThrottle = Number(document.getElementById("maxThrottle").value);
		var stallSpeed = Number(document.getElementById("stallSpeed").value);
		var trimSpeed = Number(document.getElementById("trimSpeed").value);
		var trimThrottle = Number(document.getElementById("trimThrottle").value);
		var downPitch = Number(document.getElementById("downPitch").value);

		var upPitch = Number(document.getElementById("upPitch").value);
		var upSpeed = Number(document.getElementById("upSpeed").value);

		var downSpeed = Number(document.getElementById("downSpeed").value);

		var downMorePitch = Number(document.getElementById("downMorePitch").value);
		var downMoreSpeed = Number(document.getElementById("downMoreSpeed").value);

		var output = document.getElementById("parachuteCommand");
        output.textContent = ("parachute set"
        + " \\\n    TRIM_ARSPD_CM=" + kmhToCms(trimSpeed)
        + " \\\n    TRIM_THROTTLE=" + trimThrottle
        + " \\\n    THR_MAX=" + maxThrottle
        + " \\\n    ARSPD_FBW_MAX=" + kmhToMs(maxSpeed * 0.95)
        + " \\\n    ARSPD_FBW_MIN=" + kmhToMs(stallSpeed * 1.05)
        + " \\\n    STAB_PITCH_DOWN=" + downPitch
        + " \\\n    TECS_PITCH_MIN=-" + downMorePitch
        + " \\\n    TECS_PITCH_MAX=" + upPitch
        + " \\\n    TECS_CLMB_MAX=" + upSpeed
        + " \\\n    TECS_SINK_MIN=" + downSpeed
        + " \\\n    TECS_SINK_MAX=" + downMoreSpeed
        + " \\\n    FBWB_CLIMB_RATE=" + upSpeed
        );
	}
</script>

<form onsubmit="calculateParameters(event); return false">

<h2>Fly straight</h2>
<p><label>Maximum speed (km/h): <input type="number" min="0" id="maxSpeed" /></label></p>
<p><label>Maximum throttle (%): <input type="number" min="0" max="100" id="maxThrottle" /></label></p>
<p><label>Slowest speed (km/h): <input type="number" min="0" id="stallSpeed" /></label></p>
<p><label>Trim speed (km/h): <input type="number" min="0" id="trimSpeed" /></label></p>
<p><label>Trim throttle percentage (%): <input type="number" min="0" max="100" id="trimThrottle" /></label></p>
<p><label>Down pitch (deg): <input type="number" min="0" max="90" id="downPitch" /></label></p>

<h2>Fly up</h2>
<p><label>Up pitch (deg): <input type="number" min="0" max="90" id="upPitch" /></label></p>
<p><label>Up speed (m/s): <input type="number" min="0" id="upSpeed" /></label></p>

<h2>Fly down</h2>
<p><label>Down speed (m/s): <input type="number" min="0" id="downSpeed" /></label></p>

<h2>Fly down more</h2>
<p><label>Down more pitch (deg): <input type="number" min="0" max="90" id="downMorePitch" /></label></p>
<p><label>Down more speed (m/s): <input type="number" min="0" id="downMoreSpeed" /></label></p>

<p>
    <button type="submit">Calculate parameters</button>
</p>

---

<p>
Run this command in a terminal, making sure you have <a href="https://gitlab.com/stavros/parachute">Parachute</a> installed:
<code>
<pre id="parachuteCommand">
(Please fill out the values above first)
</pre>
</code>
</p>
</form>


* * *

<p style="font-size:80%; font-style: italic">
Last updated on September 07, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>

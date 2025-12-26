# Current sensor calibrator

<style>
    div.box{
        /* width: 90%; */
    }
    .number {
        width: 60px;
    }
</style>

<script type="text/javascript">
// 1674123219

function precisionRoundMod(number, precision) {
    var factor = Math.pow(10, precision);
    var n = precision < 0 ? number : 0.01 / factor + number;
    return Math.round( n * factor) / factor;
    }

function apcalc() {
    scale = 100;
    const measurements = [];
    const realvalues = [];
    const coeffs = [];
    const scale_adjusted_meas = [];
    const current_offsets = [];

    for (var i = 1; i < 5; i++)
    {
        meas = parseFloat(document.getElementById('m'+i).value);
        real = parseFloat(document.getElementById('r'+i).value);
        measurements.push(meas);
        realvalues.push(real);

        if(i != 1){
            var p=i;
            p--;
            pmeas = parseFloat(document.getElementById('m'+p).value);
            preal = parseFloat(document.getElementById('r'+p).value);
            coeffs.push( (meas-pmeas)/ (real-preal) );
        }
    }

    for(var i=0, n=coeffs.length; i < n; i++)
    {
        console.log("coeff: "+parseFloat(coeffs[i]));
    }

    console.log("coeff sum: "+coeffs.reduce((partialSum, a) => partialSum + a, 0));
    const avg_coeffs = coeffs.reduce((partialSum, a) => partialSum + a, 0) / coeffs.length;
    console.log("coeff avg: "+avg_coeffs);

    for(var i=0, n=measurements.length; i < n; i++)
    {
        scale_adjusted_meas.push(measurements[i]/avg_coeffs);
        console.log("scale_adjusted_meas: "+measurements[i]/avg_coeffs);
    }

    for(var i=0, n=realvalues.length; i < n; i++)
    {
        current_offsets.push(scale_adjusted_meas[i] - realvalues[i]);
        console.log(scale_adjusted_meas[i] - realvalues[i] );
    }

    const avg_offset = current_offsets.reduce((partialSum, a) => partialSum + a, 0) / current_offsets.length;
    console.log("avg_offset: "+avg_offset);

    document.getElementById('r_offset').value = precisionRoundMod( (avg_offset / (scale / avg_coeffs)), 4 );
    document.getElementById('r_scale').value = precisionRoundMod( (scale / avg_coeffs) ,4);
}

function init() {
	document.querySelectorAll("input").forEach(input => {
		input.addEventListener("input", apcalc);
	});
}

window.onload = init;
</script>

This calculator will allow you to calibrate your current sensor better than with the mAh charged vs mAh consumed method.

You need a current meter and a way to see what current and throttle percentage the FC reports (the OSD is a good way to do this).

The steps to follow are:

0. Make sure you have capacitors on ESCs so the measurement will not be influenced by errors from ESC noise.
1. Set `BATT_AMP_PERVLT=100` and `BATT_AMP_OFFSET=0`.
3. Power your plane with propellers on and a current meter connected between FC and pack.
4. Arm and run the motor in manual mode. For four different throttle positions, note down: The throttle position (from the OSD), the reported current (from the OSD), and the actual current (from the current meter). The best throttle positions to use would be 25%, 50%, 75% and 100%. Do not check current on idle as this will be inaccurate.
5. Enter the values below, and the calculator will give you the proper BATT_AMP_PERVLT and BATT_AMP_OFFSET values that you now need to write to your plane's parameters.


<div class="box">
    <div id="input">
        <table style="border: none">
            <tr>
                <td>OSD current:</td>
                <td>
                    <input class="number" type="text" id="m1" value="1.7" placeholder="OSD value">
                    <input class="number" type="text" id="m2" value="3.4" placeholder="OSD value">
                    <input class="number" type="text" id="m3" value="7" placeholder="OSD value">
                    <input class="number" type="text" id="m4" value="10.3" placeholder="OSD value">
                </td>
            </tr>
            <tr>
                <td>
                    Real current:
                </td>
                <td>
                    <input class="number" type="text" id="r1" value="2.0" placeholder="current meter">
                    <input class="number" type="text" id="r2" value="4.0" placeholder="current meter" >
                    <input class="number" type="text" id="r3" value="8.0" placeholder="current meter" >
                    <input class="number" type="text" id="r4" value="12.0" placeholder="current meter">
                </td>
            </tr>
            <tr>
                <td>
                    <br>Results:<br>
                </td>
            </tr>
            <tr>
                <td>
                    <code>BATT_AMP_OFFSET</code>:
                </td>
                <td>
                    <input class="number" type="text" id="r_offset" value="" placeholder="offset" ><br>
                </td>
            </tr>
            <tr>
                <td>
                    <code>BATT_AMP_PERVLT</code>:
                </td>
                <td>
                    <input class="number" type="text" id="r_scale" value="" placeholder="scale" >
                </td>
            </tr>
        </table>
    </div>
    <br>
    <div id="result">
    </div>
</div>

_(Many thanks to mfoos for writing this note.)_

* * *

<p style="font-size:80%; font-style: italic">
Last updated on November 17, 2024. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>

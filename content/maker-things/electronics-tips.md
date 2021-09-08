+++
title = "Electronics tips"
weight = 2
sort_by = "weight"
insert_anchor_links = "right"
+++
This page contains various notes and tips about electronics.

## Decoupling capacitors

StackOverflow has a good answer on [why use decoupling capacitors](https://arduino.stackexchange.com/questions/51712/a4988-and-capacitors) in the context of a stepper driver:

> There are two purposes of such capacitor:
> 
> * first it supply power for short peaks in demand, so effectively enabling the 12V power source supply much more current for short time, than it can support over long time and so the driver have more stable power and works generally better. Also it protects the driver from noise of other parts.
> * the other is protect all other parts from voltage drops and noise caused by the driver. It is recomended to have capacitors as near as possible to any IC/driven circuit for this reason.
>
> So basically - if you have good power source, you can often get away even without such capacitors. But if you power also logic from the same source, it is already better to have some capacitors on power lines where posssible. Escpecially if you expect some noise around (like having motors near or lines to motors in paralel with other lines ...). Depends how much you care and how critical you see the project. Hobby project just for fun can go even without capacitors and be all good. Good industry projects have capacitors always everywhere.
>
> I had project, where it worked even without capacitors (laser printer), but now I would place some there in any case near each driver, just to be sure. 100uF is really good capacity, enables for lot power. But if you use any other value (which you have more ready), it should not hurt too. It is not about if it would work or not, it is more about if it ensures, that it would work flawlessly even in bad conditions even under unexpected conditions and would not have "sometimes strange problems, which disapear spontaneously during debugging".
>
> Also note, that for improving power are good high capacity electrolytes. For preventing noise are much better ceramic (which are fast, even if they have a lot smaler capacity) and so many people put both there (like 100uF electrolyte and 100nF ceramic in paralel).
>
> Short answer: Do as you want, it would probably work anyway. I personally would place big+small capacitors near each driver.



## LDO recommendation

Asking for a recommendation for a good 3.3V LDO, someone said:

> There's a number of good parts.  In the 500mA range I'd highly recommend the [Holtek HT7833](https://www.holtek.com.tw/documents/10179/82844a36-1633-498c-a6e3-4d99f2d0f6d7).  If you need closer to an amp at 3.3, the [Torex XC6220](https://www.torexsemi.com/file/xc6220/XC6220.pdf) is popular, but I haven't used that one myself.  Another popular part I haven't used is the [Diodes Inc. AP2112](https://www.diodes.com/assets/Datasheets/AP2112.pdf), 600mA.  The Holtek has 4uA quiescent current, the other two are around 50uA.  LCSC.com has all three parts.



## Driving a relay

David Albert said: 

> When energizing a relay, you are charging a coil (inductor). To turn the relay on, you can use an NPN transistor (e.g. 2N3904) with the collector to the coil and the emitter to ground. The other side of the relay coil will go to +5V. You will need a resistor (try 1K) between your transistor base and your 3.3v control source. You will also need a diode in parallel with the coil: cathode towards +5V, anode at the junction of the transistor collector and coil. The purpose of the diode is to prevent your transistor from being destroyed when you turn off power to the coil. When you remove power from a coil, the energy stored in the coil (as a magnetic field) collapses back into the coil inducing a current flow in the coil. The voltage will climb until the current can flow (e.g. by destroying your transistor). The reverse-biased diode gives the current a path to flow so nothing gets damaged. Also, make sure your transistor is rated to carry the current needed to energize your coil (e.g. a 2N3904 is rated to deliver at most 200mA; if you need more than that, choose a transistor with a larger current rating). 
> 
> The resistor between the control source (e.g. an ESP32 GPIO pin) and the base of the transistor is to limit current. Whatever goes into the base will flow directly through to the emitter (to ground)...the resistor limits that current. When current is flowing through the base-emitter junction, a much larger current will flow through the collector-emitter junction (energizing the relay coil).

There is more info on StackOverflow: [Selecting a switching transistor for a 5V relay](https://electronics.stackexchange.com/questions/369447/selecting-a-switching-transistor-for-a-5v-relay)

* * *

<p style="font-size:80%; font-style: italic">
Last updated on December 13, 2020. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>

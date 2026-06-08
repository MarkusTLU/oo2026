"use strict";
class Kettle {
    outsideTemperature;
    temperature;
    coolingCoefficient;
    specificHeatCapacity = 4200;
    constructor(outsideTemperature, temperature, coolingCoefficient) {
        this.outsideTemperature = outsideTemperature;
        this.temperature = temperature;
        this.coolingCoefficient = coolingCoefficient;
    }
    getTemperature() {
        return this.temperature;
    }
    cool(seconds) {
        const deltaT = (this.temperature - this.outsideTemperature)
            * this.coolingCoefficient * seconds;
        this.temperature -= deltaT;
    }
}
function arvuta() {
    const outsideTemp = parseFloat(document.getElementById("outside").value);
    const startTemp = parseFloat(document.getElementById("start").value);
    const measuredDelta = parseFloat(document.getElementById("delta").value);
    const queryTemp = parseFloat(document.getElementById("query").value);
    // Koefitsient mõõtmisest: 30 sekundi jooksul measuredDelta kraadi
    const coeff = measuredDelta / ((startTemp - outsideTemp) * 30);
    const kettle = new Kettle(outsideTemp, queryTemp, coeff);
    kettle.cool(30);
    const result = queryTemp - kettle.getTemperature();
    document.getElementById("result").innerText = result.toFixed(4);
}
window.arvuta = arvuta;

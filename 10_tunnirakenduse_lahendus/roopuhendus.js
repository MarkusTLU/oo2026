"use strict";
class Resistor {
    r = 0;
    constructor(r) {
        this.r = r;
    }
    getResistance() {
        return this.r;
    }
    getCurrent(u) {
        return u / this.r;
    }
    getPower(u) {
        return u * this.getCurrent(u);
    }
}
class ParallelCircuit {
    resistors = [];
    push(r) {
        this.resistors.push(r);
    }
    getTotalResistance() {
        let inverseSum = 0;
        this.resistors.forEach((r) => {
            inverseSum += 1 / r.getResistance();
        });
        return 1 / inverseSum;
    }
    getTotalPower(u) {
        let total = 0;
        this.resistors.forEach((r) => {
            total += r.getPower(u);
        });
        return total;
    }
}
function arvuta() {
    const u = parseFloat(document.getElementById("pinge").value);
    const r1val = parseFloat(document.getElementById("r1").value);
    const r2val = parseFloat(document.getElementById("r2").value);
    const r1 = new Resistor(r1val);
    const r2 = new Resistor(r2val);
    const pc = new ParallelCircuit();
    pc.push(r1);
    pc.push(r2);
    document.getElementById("r1-power").innerText = r1.getPower(u).toFixed(4);
    document.getElementById("r2-power").innerText = r2.getPower(u).toFixed(4);
    document.getElementById("total-power").innerText = pc.getTotalPower(u).toFixed(4);
    document.getElementById("total-resistance").innerText = pc.getTotalResistance().toFixed(4);
}
window.arvuta = arvuta;

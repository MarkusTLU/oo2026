"use strict";
class Resistor {
    constructor(r, g, startx, endx, y) {
        this.r = r;
        this.g = g;
        this.startx = startx;
        this.endx = endx;
        this.y = y;
        this.height = 80;
        this.u = 0;
        this.i = 0;
        this.p = 0;
        this.width = this.endx - this.startx;
        this.draw();
    }
    draw() {
        this.g.clearRect(this.startx, this.y - this.height * 0.75, this.width, this.height * 1.5);
        this.g.beginPath();
        this.g.moveTo(this.startx, this.y);
        this.g.lineTo(this.startx + this.width / 4, this.y);
        this.g.rect(this.startx + this.width / 4, this.y - this.height / 4, this.width / 2, this.height / 2);
        this.g.moveTo(this.startx + this.width * 3 / 4, this.y);
        this.g.lineTo(this.endx, this.y);
        this.g.stroke();
        this.g.fillText(this.r + " Ω", this.startx + this.width / 3, this.y + 3);
        this.g.fillText(this.u + " V,  " + this.i.toFixed(3) + " A", this.startx + this.width / 4, this.y - this.height / 4 - 4);
        this.g.fillText(this.p.toFixed(3) + " W", this.startx + this.width / 4, this.y + this.height / 4 + 14);
    }
    setR(r) {
        this.r = r;
        this.calculate();
        this.draw();
    }
    getR() {
        return this.r;
    }
    setU(u) {
        this.u = u;
        this.calculate();
        this.draw();
    }
    getU() {
        return this.u;
    }
    calculate() {
        this.calculateCurrent();
        this.calculatePower();
    }
    calculateCurrent() {
        this.i = this.u / this.r;
    }
    calculatePower() {
        this.p = this.u * this.i;
    }
}

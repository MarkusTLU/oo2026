"use strict";
class Resistor {
    r;
    height = 30;
    width = 70;
    parent;
    constructor(r) {
        this.r = r;
    }
    getR() { return this.r; }
    getWidth() { return this.width; }
    getHeight() { return this.height; }
    setParent(p) {
        this.parent = p;
    }
    setR(r) {
        this.r = r;
        if (this.parent) {
            this.parent.draw();
        }
    }
    draw(g, startx, y) {
        g.beginPath();
        g.moveTo(startx, y);
        g.lineTo(startx + this.width / 4, y);
        g.rect(startx + this.width / 4, y - 10, this.width / 2, 20);
        g.fillText(this.r + " \u03A9", startx + this.width / 4 + 1, y + 2);
        g.moveTo(startx + this.width * 3 / 4, y);
        g.lineTo(startx + this.width, y);
        g.stroke();
    }
}
class ParallelCircuit {
    g;
    startx;
    y;
    resistors = [];
    height = 0;
    u = 0;
    constructor(g, startx, y) {
        this.g = g;
        this.startx = startx;
        this.y = y;
    }
    push(r) {
        this.resistors.push(r);
        this.height += 40;
        r.setParent(this);
        this.draw();
    }
    setU(u) {
        this.u = u;
        this.draw();
    }
    getI() {
        let total = 0;
        this.resistors.forEach(r => {
            total += this.u / r.getR();
        });
        return total;
    }
    getR() {
        let inverseSum = 0;
        this.resistors.forEach(r => {
            inverseSum += 1 / r.getR();
        });
        return 1 / inverseSum;
    }
    draw() {
        this.g.clearRect(0, 0, 400, 250);
        const topY = this.y - (this.resistors.length - 1) * 20;
        const bottomY = topY + (this.resistors.length - 1) * 40;
        const resistorStartX = this.startx + 10;
        const resistorEndX = resistorStartX + 70;
        let currentY = topY;
        for (let i = 0; i < this.resistors.length; i++) {
            this.resistors[i].draw(this.g, resistorStartX, currentY);
            currentY += 40;
        }
        this.g.beginPath();
        this.g.moveTo(resistorStartX, topY);
        this.g.lineTo(resistorStartX, bottomY);
        this.g.moveTo(this.startx, this.y);
        this.g.lineTo(resistorStartX, this.y);
        this.g.moveTo(resistorEndX, topY);
        this.g.lineTo(resistorEndX, bottomY);
        this.g.moveTo(resistorEndX, this.y);
        this.g.lineTo(resistorEndX + 10, this.y);
        this.g.stroke();
        // Kuva pinge ja koguvool
        this.g.fillText(this.u + " V,  I=" + this.getI().toFixed(3) + " A,  R=" + this.getR().toFixed(1) + " \u03A9", this.startx, this.y + this.height / 2 + 20);
    }
}

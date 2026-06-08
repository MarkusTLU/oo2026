class Resistor {
    readonly height: number = 30;
    readonly width: number = 70;
    protected parent!: ParallelCircuit;

    constructor(protected r: number) {}

    getR(): number { return this.r; }
    getWidth(): number { return this.width; }
    getHeight(): number { return this.height; }

    setParent(p: ParallelCircuit) {
        this.parent = p;
    }

    setR(r: number) {
        this.r = r;
        if (this.parent) {
            this.parent.draw();
        }
    }

    draw(g: CanvasRenderingContext2D, startx: number, y: number) {
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
    resistors: Resistor[] = [];
    height: number = 0;
    protected u: number = 0;

    constructor(
        protected g: CanvasRenderingContext2D,
        protected startx: number,
        protected y: number
    ) {}

    push(r: Resistor) {
        this.resistors.push(r);
        this.height += 40;
        r.setParent(this);
        this.draw();
    }

    setU(u: number) {
        this.u = u;
        this.draw();
    }

    getI(): number {
        let total: number = 0;
        this.resistors.forEach(r => {
            total += this.u / r.getR();
        });
        return total;
    }

    getR(): number {
        let inverseSum: number = 0;
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
        this.g.fillText(
            this.u + " V,  I=" + this.getI().toFixed(3) + " A,  R=" + this.getR().toFixed(1) + " \u03A9",
            this.startx, this.y + this.height / 2 + 20
        );
    }
}
class Resistor {
    r: number = 0;

    constructor(r: number) {
        this.r = r;
    }

    getResistance(): number {
        return this.r;
    }

    getCurrent(u: number): number {
        return u / this.r;
    }

    getPower(u: number): number {
        return u * this.getCurrent(u);
    }
}

class ParallelCircuit {
    resistors: Resistor[] = [];

    push(r: Resistor) {
        this.resistors.push(r);
    }

    getTotalResistance(): number {
        let inverseSum: number = 0;
        this.resistors.forEach((r: Resistor) => {
            inverseSum += 1 / r.getResistance();
        });
        return 1 / inverseSum;
    }

    getTotalPower(u: number): number {
        let total: number = 0;
        this.resistors.forEach((r: Resistor) => {
            total += r.getPower(u);
        });
        return total;
    }
}

function arvuta() {
    const u = parseFloat((document.getElementById("pinge") as HTMLInputElement).value);
    const r1val = parseFloat((document.getElementById("r1") as HTMLInputElement).value);
    const r2val = parseFloat((document.getElementById("r2") as HTMLInputElement).value);

    const r1 = new Resistor(r1val);
    const r2 = new Resistor(r2val);
    const pc = new ParallelCircuit();
    pc.push(r1);
    pc.push(r2);

    document.getElementById("r1-power")!.innerText = r1.getPower(u).toFixed(4);
    document.getElementById("r2-power")!.innerText = r2.getPower(u).toFixed(4);
    document.getElementById("total-power")!.innerText = pc.getTotalPower(u).toFixed(4);
    document.getElementById("total-resistance")!.innerText = pc.getTotalResistance().toFixed(4);
}

(window as any).arvuta = arvuta;
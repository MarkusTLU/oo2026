class Kettle {
    readonly specificHeatCapacity: number = 4200;

    constructor(
        private outsideTemperature: number,
        private temperature: number,
        private coolingCoefficient: number
    ) {}

    getTemperature(): number {
        return this.temperature;
    }

    cool(seconds: number): void {
        const deltaT = (this.temperature - this.outsideTemperature)
            * this.coolingCoefficient * seconds;
        this.temperature -= deltaT;
    }
}

function arvuta() {
    const outsideTemp = parseFloat(
        (document.getElementById("outside") as HTMLInputElement).value);
    const startTemp = parseFloat(
        (document.getElementById("start") as HTMLInputElement).value);
    const measuredDelta = parseFloat(
        (document.getElementById("delta") as HTMLInputElement).value);
    const queryTemp = parseFloat(
        (document.getElementById("query") as HTMLInputElement).value);

    // Koefitsient mõõtmisest: 30 sekundi jooksul measuredDelta kraadi
    const coeff = measuredDelta / ((startTemp - outsideTemp) * 30);

    const kettle = new Kettle(outsideTemp, queryTemp, coeff);
    kettle.cool(30);

    const result = queryTemp - kettle.getTemperature();
    document.getElementById("result")!.innerText = result.toFixed(4);
}

(window as any).arvuta = arvuta;
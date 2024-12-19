int ovenTime() {
    int time{40};
    return time;
}

int remainingOvenTime(int actualMinutesInOven) {
    return ovenTime() - actualMinutesInOven;
}

int preparationTime(int numberOfLayers) {
    return numberOfLayers * 2;
}

int elapsedTime(int numberOfLayers, int actualMinutesInOven) {
    return actualMinutesInOven + preparationTime(numberOfLayers); 
}
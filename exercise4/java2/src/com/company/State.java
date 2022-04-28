package com.company;

public enum State {
    SUSCEPTIBLE, INFECTED;

    public static State initState(Float probability) {
        return Math.random() <= (probability / 100) ? INFECTED: SUSCEPTIBLE ;
    }
}

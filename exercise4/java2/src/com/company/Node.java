package com.company;


import java.util.Collection;
import java.util.concurrent.atomic.AtomicReference;

public class Node implements Comparable {
    private Integer index;
    private State state;

    public Integer getIndex() {
        return index;
    }

    public void setIndex(Integer index) {
        this.index = index;
    }

    public State getState() {
        return state;
    }

    public void setState(State state) {
        this.state = state;
    }

    public Node(Integer index, Float probability) {
        this.index = index;
        this.state = State.initState(probability);
    }

    public static Double percentInfected(Collection<Node> c) {
        AtomicReference<Integer> infecteds = new AtomicReference<>(0);
        c.forEach(n -> {
            if (n.getState() == State.INFECTED)
                infecteds.getAndSet(infecteds.get() + 1);
        });
        return infecteds.get() / (double) c.size();
    }

    @Override
    public String toString() {
        return "Index: " + this.index + "\tState: " + this.state + "\n";
    }

    @Override
    public int compareTo(Object o) {
        return this.getIndex() - ((Node) o).getIndex();
    }
}

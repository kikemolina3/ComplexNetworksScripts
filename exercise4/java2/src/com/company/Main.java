package com.company;


import com.google.common.base.Supplier;
import com.rits.cloning.Cloner;
import edu.uci.ics.jung.graph.UndirectedSparseGraph;
import edu.uci.ics.jung.io.PajekNetReader;

import java.io.FileReader;
import java.util.*;
import java.util.concurrent.atomic.AtomicReference;


public class Main {

    public static final int BEGIN_STATIONARY = 900;
    protected static final Integer NUM_REPETITIONS = 50;
    public static final int TOTAL_ITERATIONS = 1000;

    static Supplier<Node> nodeFactory;
    static Supplier<Integer> edgeFactory;

    public static void inits() {
        edgeFactory =
                new Supplier<>() {
                    Integer n = 0;

                    public Integer get() {
                        return n++;
                    }
                };
    }


    public static void main(String[] args) {

        inits();

        List<String> files = new ArrayList<>(List.of("football.net"));
        files.forEach(i -> {
            for (Float infectionProbability = 0F; infectionProbability <= 100F; infectionProbability += 2F) {
                Double simulationAverages = 0.0;
                for (int j = 0; j < NUM_REPETITIONS; j++) {
                    try {
                        Double stationaryAverages = 0.0;
                        Float initialProbabilityInfection = 20F;
                        Float recoveryProbability = 90F;
                        nodeFactory =
                                new Supplier<>() {
                                    Integer m = 0;

                                    public Node get() {
                                        return new Node(m++, initialProbabilityInfection);
                                    }
                                };
                        String file = "resources/" + i;
                        FileReader fileReader = new FileReader(file);
                        PajekNetReader<UndirectedSparseGraph<Node, Integer>, Node, Integer> pajekNetReader =
                                new PajekNetReader<>(nodeFactory, edgeFactory);
                        UndirectedSparseGraph<Node, Integer> g = new UndirectedSparseGraph<>();
                        pajekNetReader.load(fileReader, g);
                        Cloner cloner = new Cloner();
                        UndirectedSparseGraph<Node, Integer> gClone = cloner.deepClone(g);
                        ArrayList<Node> gNodeList = new ArrayList<>(g.getVertices());
                        gNodeList.sort(Node::compareTo);
                        for (int k = 0; k < TOTAL_ITERATIONS; k++) {
                            ArrayList<Node> gCloneNodeList = new ArrayList<>(gClone.getVertices());
                            gCloneNodeList.sort(Node::compareTo);
                            for (Node n : gNodeList) {
                                if (n.getState() == State.INFECTED)
                                    gCloneNodeList.get(n.getIndex()).setState(Math.random() <= (recoveryProbability / 100) ? State.SUSCEPTIBLE : State.INFECTED);
                                else {
                                    AtomicReference<Integer> infectedNb = new AtomicReference<>(0);
                                    for (Node nb : g.getNeighbors(n)) {
                                        if (nb.getState() == State.INFECTED)
                                            infectedNb.getAndSet(infectedNb.get() + 1);
                                    }
                                    double effectiveInfectionProbability = 1 - Math.pow((1 - infectionProbability), infectedNb.get());
                                    gCloneNodeList.get(n.getIndex()).setState(Math.random() <= (effectiveInfectionProbability / 100) ? State.INFECTED : State.SUSCEPTIBLE);
                                }
                            }
                            g = gClone;
                            gNodeList = new ArrayList<>(g.getVertices());
                            gNodeList.sort(Node::compareTo);
                            gClone = cloner.deepClone(g);
                            if (k >= BEGIN_STATIONARY) {
                                stationaryAverages += Node.percentInfected(gClone.getVertices());
                            }

                        }
                        stationaryAverages /= (TOTAL_ITERATIONS - BEGIN_STATIONARY);
                        simulationAverages += stationaryAverages;
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }
                simulationAverages /= NUM_REPETITIONS;
                System.out.println("Beta: " + infectionProbability + "\tInfected %: " + simulationAverages);
            }
        });
    }
}


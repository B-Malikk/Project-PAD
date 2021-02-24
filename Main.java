package com.company;

public class Main {

    public static void main(String[] args) throws Exception {
	NAO nao = new NAO();
	nao.verbind("padrick.robot.hva-robots.nl", 9559);
	//nao.verbind("localhost", 55274);
	nao.stand();
	nao.say("Hallo!");
	nao.sit();
	nao.say("Wil je hints spelen?");
    }
}

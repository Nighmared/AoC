import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Stack;
import java.util.TreeSet;

import jdk.internal.jshell.tool.resources.version;

public class AdvOfCode10 {
	public static void main(String[] args) throws FileNotFoundException {
		Scanner input = new Scanner(new File("advOfCode10.txt"));
		TreeSet<AdapterNode> graph = new TreeSet();
		int maxJolts = 0;
		while(input.hasNextInt()){
			int currVal = input.nextInt();
			maxJolts = Math.max(maxJolts,currVal);
			graph.add(new AdapterNode(currVal));
		}
		input.close();
		AdapterNode airplanePort = new AdapterNode(0);
		AdapterNode devicePort = new AdapterNode(maxJolts+3);
		graph.add(airplanePort);
		graph.add(devicePort);
		int amountOfAdapters = graph.size();

		for(AdapterNode a : graph){
			a.next = devicePort;
			for(AdapterNode c : graph){
				if(c.jolts-3 > a.jolts) break;
				if(c.jolts>a.jolts && c.jolts-a.jolts<(a.next.jolts-a.jolts)){
					a.next = c;
					c.prev = a;
				}
			}
			if(a.next == devicePort && a != devicePort){
				devicePort.prev = a;
			}
		}
		devicePort.next = null;

		int[] out = verifyandgetres(airplanePort, devicePort,amountOfAdapters);
		//PART1=========================
		System.out.println("valid solution: "+(out[0] == 1));
		System.out.println("result part 1: "+out[1]);


		//PART2==========================
		devicePort.waystodevice = 1;
		AdapterNode i = devicePort;
		while(i.prev != airplanePort){
			i.prev.waystodevice += i.waystodevice;
			if(i.jolts -i.prev.prev.jolts<=3){
				i.prev.prev.waystodevice+=i.waystodevice;
			}
			if(i.prev.prev != airplanePort && i.jolts - i.prev.prev.prev.jolts<=3){
				i.prev.prev.prev.waystodevice += i.waystodevice;
			}
			i = i.prev;
		}
		airplanePort.waystodevice += airplanePort.next.waystodevice;
		System.out.println("Solution part2: "+airplanePort.waystodevice);



	}
	private static int[] verifyandgetres(AdapterNode airplane,AdapterNode device,int adapters){
		int[] res = new int[2];
		AdapterNode currNode = airplane;
		int maxDiff = 0;
		int num1diff = 0;
		int num3diff = 0;
		int length = 1;
		while(currNode != device){
			length++;
			int diff = currNode.next.jolts - currNode.jolts;
			switch(diff){
				case 1:
					num1diff++;
					break;
				case 3:
					num3diff++;
					break;
			}
			maxDiff = Math.max(maxDiff,diff);
			currNode = currNode.next;
		}
		switch((maxDiff<=3&&length == adapters)?1 : 0){
			case 0:
				res[0] = -1;
				break;
			case 1:
				res[0] = 1;
				break;
		}
		res[1] = num1diff*num3diff;
		return res;

	}
}



class AdapterNode implements Comparable{
	long waystodevice = 0;
	AdapterNode prev;
	AdapterNode next;
	final int jolts;
	AdapterNode(int jolts){
		this.jolts = jolts;
	}

	@Override
	public int compareTo(Object o) {
		return jolts - ((AdapterNode) o).jolts;
	}

	public String toString(){
		return "=]"+jolts+"[=";
	}
}

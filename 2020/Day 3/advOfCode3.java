import java.util.LinkedList;
import java.util.Scanner;
import java.io.File;

public class advOfCode3 {

	public static void main(String[] args) {

		// input parse
		TreeSolver solver = new TreeSolver("advOfCode3.txt");

		//part 1
		printPartHeader(1);
		int treesP1 = solver.checkTrees(3, 1);
		System.out.println("Number of Trees for 3Right 1Down: "+treesP1);

		//part 2
		printPartHeader(2);
		long productOfTrees = 1;

		int[][] slopes = {
			{1,1},
			{3,1},
			{5,1},
			{7,1},
			{1,2}
		};
		for(int[] slope : slopes){
			int trees = solver.checkTrees(slope[0], slope[1]);
			productOfTrees*= (long) trees;
			System.out.println("Number of Trees for "+slope[0]+"Right "+slope[1]+"Down: "+trees);
		}
		System.out.println();
		System.out.println("Result for part 2 (product of slopes tested above): "+productOfTrees);


	}

	private static void printPartHeader(int part){
		System.out.println();
		System.out.println("=====================");
		System.out.println("Part "+part);
		System.out.println("=====================");
		System.out.println();


	}
}

class TreeSolver{
	private char[][] forest;
	private final String fName;
	private int width,height;

	TreeSolver(String fName){
		this.fName = fName;
		parseInput();
	}

	int checkTrees( int right, int down){
		if(down <= 0){
			throw new IllegalArgumentException("down has to be positive");
		}
		int numOfTrees,x,y;
		numOfTrees = x = y = 0;

		while(y+down<forest.length){
			y += down;
			x += right;
			if(hasTree(y, x)){
				numOfTrees++;
			}		
		}
		return numOfTrees;
	}

	private boolean hasTree(int a, int b){
		return safeGetElemAtPosition(a,b) == '#';
	}

	//as pattern repeats infinitely to the right, this method can be used
	private char safeGetElemAtPosition( int a, int b){
		if(a>=forest.length){
			throw new IllegalArgumentException("too far down");
		}
		return forest[a][b%width];
	}


	private void parseInput() {
		//read line to linked list, every node is string of a line
		LinkedList<String> input = readInput(fName);

		//get measurements of map
		width = input.get(0).length();
		height = input.size();

		forest = new char[height][width];

		char[] currLine;
		for (int i = 0; i < height; i++) {//iterate through input lines
			currLine = input.get(i).toCharArray();
			for (int j = 0; j < width; j++) {
				forest[i][j] = currLine[j];
			}
		}
	}

	private LinkedList<String> readInput(String filename){
		Scanner input;
		LinkedList<String> out;
		try {
			input = new Scanner(new File(filename));
		} catch (Exception e) {
			System.out.println(e);
			return null;
		}
		out = new LinkedList<>();
		while(input.hasNextLine()){
			out.add(input.nextLine());
		}
		input.close();
		return out;
	}
}
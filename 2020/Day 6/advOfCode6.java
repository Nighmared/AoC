import java.io.File;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;
import java.util.HashSet;

public class advOfCode6 {
	public static void main(String[] args) {
		HashSet<Character> answers = new HashSet<>();
		HashMap<Character,Integer> answers2 = new HashMap<>();
		File file;
		Scanner input;
		String currLine;
		int sumOfYesAnswers = 0;
		int sumOfCommonYes = 0;
		int groupSize = 0;
		try {
			file = new File("advOfCode6.txt");
			input = new Scanner(file);
		} catch (Exception e) {
			System.out.println("nope " + e.getMessage());
			return;
		}
		while (input.hasNextLine()) {
			currLine = input.nextLine();
			if (currLine.isBlank()) {
				System.out.println(groupSize);
				sumOfYesAnswers += answers.size();
				
				for(char c : answers2.keySet()){
					if(answers2.get(c)>= groupSize){
						sumOfCommonYes++;
					}
				}
				answers2.clear();
				answers.clear();
				groupSize = 0;
				continue;
			}
			groupSize++;

			char[] lineChars = currLine.toCharArray();
			for (char c : lineChars) {
				answers.add(c);
				if(answers2.keySet().contains(c)){
					answers2.put(c,answers2.get(c)+1);
				}
				else{
					answers2.put(c,1);
				}
			}

		}
		sumOfYesAnswers += answers.size();
		for(char c : answers2.keySet()){
			if(answers2.get(c)>= groupSize){
				sumOfCommonYes++;
			}
		}
		input.close();

		System.out.println("Sum of Common answers: " + sumOfYesAnswers);
		System.out.println("Sum of Common yes answers: "+sumOfCommonYes);
	}
}
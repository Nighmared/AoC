import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

public class advOfCode7 {
	public static void main(String[] args) {
		Scanner input;
		try {
			input = new Scanner(new File("advOfCode7.txt"));
		} catch (Exception e) {
			System.out.println("LOL NOPE" + e.getLocalizedMessage());
			return;
		}
		Solver solver = new Solver();
		ArrayList<Rule> rules = new ArrayList<>();
		while (input.hasNextLine()) {
			String[] currLine = input.nextLine().split("bags contain ");
			String color = currLine[0].strip();
			if (!solver.addBagType(color)) {
				System.out.println(color); // maybe find duplicate colors
			}
			String[] lineRules = currLine[1].replaceAll("(\s)? bag(s)?(,\s)", "°").replaceAll("\sbag(s)?\\.", "")
					.split("°");
			rules.add(new Rule(color, lineRules));
		}
		input.close();
		for (Rule r : rules) {
			BagNode parentBag = solver.getBagObj(r.color);
			for (String childRule : r.containments) {
				String[] splitRule = childRule.split("\s");
				if (splitRule[0].equals("no")) { // = "no other bag"
					continue;
				}
				int num = Integer.parseInt(splitRule[0]);
				String colorKey = splitRule[1] + " " + splitRule[2];
				ContainRule rule = new ContainRule(solver.getBagObj(colorKey), num);
				parentBag.addRule(rule);
			}
		}

		solver.doTransitive();
		System.out.println("== Result for part 1: " + solver.getBagObj("shiny gold").getNumOfParents());
		System.out.println("== Result for part 2: " + solver.getRequiredBags("shiny gold"));
	}
}

class Rule {
	final String color;
	final String[] containments;

	Rule(String color, String[] rest) {
		this.color = color;
		containments = rest;
	}
}

class Solver {
	private HashMap<String, BagNode> bagMap = new HashMap<>();
	private boolean transitiveDone = false;

	public int getRequiredBags(String color) {
		int res = 0;
		BagNode bag = bagMap.get(color);
		res += recursiveRequiredBags(bag);
		return res;
	}

	private int recursiveRequiredBags(BagNode bag) {
		if (bag.cacheValid) {
			return bag.requiredInside;
		}

		int res = 0;
		for (ContainRule r : bag.rules) {
			res += r.amount;
			res += r.amount * recursiveRequiredBags(r.child);
		}
		bag.setCache(res);
		return res;
	}

	void doTransitive() {
		if (transitiveDone) {
			return;
		}
		for (String key : bagMap.keySet()) {
			BagNode currBag = getBagObj(key);
			for (ContainRule rule : currBag.rules) {
				recursiveTransitivity(currBag, rule.child);
			}
		}
		transitiveDone = true;
	}

	private void recursiveTransitivity(BagNode parent, BagNode child) {
		if (parent.color.equals(child.color)) {
			throw new IllegalStateException("bruh wtf r those loops // feeling all loopy");
		}
		child.parents.add(parent);
		for (ContainRule r : child.rules) {
			recursiveTransitivity(parent, r.child);
		}
	}

	boolean addBagType(String color) {
		if (transitiveDone) {
			throw new IllegalStateException("cant add types after transitivity was created");
		}
		if (bagMap.keySet().contains(color)) {
			return false;
		} else {
			bagMap.put(color, new BagNode(color));
			return true;
		}
	}

	BagNode getBagObj(String color) {
		if (bagMap.keySet().contains(color)) {
			return bagMap.get(color);
		}
		return null;
	}
}

class BagNode {
	HashSet<ContainRule> rules = new HashSet<>();
	HashSet<BagNode> parents = new HashSet<>();
	final String color;
	int requiredInside = 0;
	boolean cacheValid = true;

	BagNode(String color) {
		this.color = color;
	}

	boolean addRule(ContainRule child) {
		cacheValid = false;
		if (rules.contains(child)) {
			return false;
		}
		rules.add(child);
		return true;
	}

	int getNumOfParents() {
		return parents.size();
	}

	void setCache(int value) {
		if (value <= 0) {
			throw new IllegalArgumentException();
		}
		cacheValid = true;
		requiredInside = value;
	}
}

class ContainRule {
	final BagNode child;
	final int amount;

	ContainRule(BagNode child, int amount) {
		this.child = child;
		this.amount = amount;
	}
}
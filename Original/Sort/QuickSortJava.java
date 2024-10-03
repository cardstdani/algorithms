import java.lang.Math;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {
	public static void main(String[] args) {
		List<Integer> myList = new ArrayList<>();
		for (int i = 0; i < 15; i++) {
			myList.add(new Random().nextInt(40));
		}
		System.out.println(myList);
		System.out.println(quickSort(myList));
	}

	public static List<Integer> quickSort(List<Integer> list) {
		if (list.size() <= 1) {
			return list;
		}
		int pivot = list.size() / 2;
		List<Integer> left = new ArrayList<>();
		List<Integer> right = new ArrayList<>();
		for (int i = 0; i < list.size(); i++) {
			if (i != pivot) {
				if (list.get(i) < list.get(pivot)) {
					left.add(list.get(i));
				} else {
					right.add(list.get(i));
				}
			}
		}

		List<Integer> joinedList = quickSort(left);
		joinedList.add(list.get(pivot));
		joinedList.addAll(quickSort(right));
		return joinedList;
	}
}

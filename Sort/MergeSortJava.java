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
		System.out.println(mergeSort(myList));
	}

	public static List<Integer> mergeSort(List<Integer> list) {
		if (list.size() <= 1) {
			return list;
		}

		int mid = list.size() / 2;
		List<Integer> l = new ArrayList<>();
		List<Integer> r = new ArrayList<>();
		for (int i = 0; i < list.size(); i++) {
			if (i < mid) {
				l.add(list.get(i));
			} else {
				r.add(list.get(i));
			}
		}
		
		List<Integer> joinedList = mergeSort(l);
		joinedList.addAll(mergeSort(r));
		Collections.sort(joinedList);
		return joinedList;
	}
}

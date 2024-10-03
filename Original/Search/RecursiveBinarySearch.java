import java.util.*;

public class RecursiveBinarySearch {

  public static int RecursiveBinSearch(List<Integer> l, int target, int start, int end) {
    if ((end - start) <= 1) {
      if (target == l.get(end)) {
        return end;
      }
      if (target == l.get(start)) {
        return start;
      }
      return -1;
    }

    int mid = (end + start) / 2;
    if (target < l.get(mid)) {
      return RecursiveBinSearch(l, target, start, mid);
    }

    if (target > l.get(mid)) {
      return RecursiveBinSearch(l, target, mid, end);
    }

    if (target == l.get(mid)) {
      return mid;
    }
    return -1;
  }

  public static void main(String args[]) {
    List<Integer> l = new ArrayList<Integer>();

    int r = (int) (Math.random() * (40));
    int target = (int) (Math.random() * (r - 1));
    for (int i = 0; i < r; i++) {
      l.add(i);
    }
    System.out.println(l);
    System.out.println("Target: " + target + " at position: " + RecursiveBinSearch(l, target, 0, l.size()-1));
  }
}

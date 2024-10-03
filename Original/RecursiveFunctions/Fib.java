import java.util.*;
import java.math.BigInteger;

public class Fib {

  public static Integer fibMem(int n, HashMap<Integer, Integer> mem) {
    if (n <= 1) {
      return 1;
    }

    if (mem.containsKey(n)) {
      return mem.get(n);
    }

    mem.put(n, fibMem(n - 1, mem) + fibMem(n - 2, mem));
    return mem.get(n);
  }

  public static int fib(int n) {
    if (n <= 1) {
      return 1;
    }
    return fib(n - 1) + fib(n - 2);
  }
  
  public static BigInteger fibMemBigInteger(BigInteger n, HashMap<BigInteger, BigInteger> mem) {
    if (n.compareTo(BigInteger.ONE) <= 0) {
      return BigInteger.ONE;
    }

    if (mem.containsKey(n)) {
      return mem.get(n);
    }

    mem.put(n, fibMemBigInteger(n.subtract(BigInteger.ONE), mem).add(fibMemBigInteger(n.subtract(new BigInteger("2")), mem)));
    return mem.get(n);
  }

  public static BigInteger fibBigInteger(BigInteger n) {
    if (n.compareTo(BigInteger.ONE) <= 0) {
      return BigInteger.ONE;
    }
    return fibBigInteger(n.subtract(BigInteger.ONE)).add(fibBigInteger(n.subtract(new BigInteger("2"))));
  }

  public static void main(String args[]) {
    System.out.println(fib(8));
    System.out.println(fibMem(40, new HashMap<Integer, Integer>()));
    
    System.out.println(fibBigInteger(new BigInteger("8")));
    System.out.println(fibMemBigInteger(new BigInteger("50"), new HashMap<BigInteger, BigInteger>()));
  }
}

import base_structure.*;

import java.util.Random;

public class Test {
    static Random random = new Random();

    public static void main(String[] args) {
        var singleArray = new SingleArray<Integer>();
//        var vectorArray = new VectorArray<Integer>();
//        IArray factorArray = new FactorArray();
//        IArray matrixArray = new MatrixArray();
        testAddArray(singleArray, 100000);
//        testAddArray(vectorArray, 1000);
//        testAddArray(factorArray, 100_000);
//        testAddArray(matrixArray, 100_000);
    }

    private static void testAddArray(IArray<Integer> data, int total) {
        for (int j = 0; j < total; j ++)
            data.add(j);

        long start = System.currentTimeMillis();

        for (int j = 0; j < total; j ++)
            data.remove(random.nextInt(data.size()));
//            data.remove(0);

        System.out.println(System.currentTimeMillis() - start);



//        System.out.println(data);
//        System.out.println(item);
//        data.remove(54);
//        System.out.println(data);
//        data.remove(data.size()-1);
//        System.out.print(data);

    }
}

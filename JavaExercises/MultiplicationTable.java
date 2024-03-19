package JavaExercises;

public class MultiplicationTable {
    void printtable() {
        parametertable(5);
    }

    void parametertable(int table) {
        function(table, 1, 10);
    }

    void function(int table, int from, int to) {
        for (int i = from; i <= to; i++) {
            System.out.printf("%d * %d = %d ", table, i, table * i).println();
        }
    }
}

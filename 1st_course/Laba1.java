/*
Автор: Потанин Лев Антонович
Группа: R3141
Вариант: 508
Оценка: 10 баллов
*/

public class Laba1 {
    public static void main(String[] args) {
        short[] a = new short[(20-4)/2 + ((20-4)+1)%2];
        for (short i = 0; i < 9; i += 1) {
            a[i] = (short)(4 + 2*i);
        }

        float[] x = new float[10];
        for (int i = 0; i < 10; i++){
            x[i] = (float)Math.random()*22 - 7;
        }

        double[][] s = new double[9][10];
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 10; j++) {
                switch (a[i]) {
                    case(20): {
                        s[i][j] = Math.atan(Math.pow(Math.E,Math.pow( ((-1.0)* Math.pow(Math.E, x[j])) , (1.0 / 3))));
                        break;
                    }
                    case(6):
                    case(10):
                    case(12):
                    case(14): {
                        s[i][j] = Math.pow((Math.pow(Math.sin(x[j]), (3.0/4)*(Math.tan(x[j])-1))),((1.0/4)/Math.asin(Math.pow(((x[j]+4.0f)/22),2))));
                        break;
                    }
                    default: {
                        s[i][j] = (Math.asin(Math.cos(Math.tan(Math.asin((x[j]+4.0f)/22)))))/2;
                        break;
                    }
                }
            }
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.printf("%.3f ", s[i][j]);
            }
            System.out.println();
        }
    }
}

public class P1_Java_Multiples_3_5{
    public static int findMultiples(int n){
        
        int Sumation = 0;
        for(int i = 0; i < n; i++){
            if ((i % 3 == 0) || (i % 5 == 0)) {
                Sumation = Sumation + i;
            }

        }
    return Sumation;
    }

public static void main(String[] args){
    int n = 1000;
    System.out.println(findMultiples(n));
}
}
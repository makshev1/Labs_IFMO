public class Main {
    public static void main(String[] args) {
        Karlson karlson = new Karlson("Karlson");
        karlson.shrug();
        System.out.println();
        Something something = new Something("something");
        something.not_look(Status.like);
        Smoker smoker = new Smoker("man with cigar");
        smoker.feel(Status.happy);
        System.out.println();
        Unknown unknown = new Unknown();
        Unknown[] they = new Unknown[2];
        they[0] = karlson;
        they[1] = unknown;
        for (Unknown value : they) {
            value.watch();
        }
        smoker.brush_off(Status.long_and_carefully);
        for (Unknown value : they) {
            value.hear();
        }
        Policeman policeman = new Policeman("policeman");
        smoker.call_for(policeman);
    }
}

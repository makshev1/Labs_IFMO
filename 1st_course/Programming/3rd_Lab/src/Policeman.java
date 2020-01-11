class Policeman extends Human {
    Policeman(String name) {
        this.name = name;
    }
    @Override
    public String toString(){
        return ("Class: Policeman; Name: " + name);
    }
}

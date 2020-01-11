class Karlson extends Unknown implements Shrug, Watch, Hear {
    Karlson(String name) {
        this.name = name;
    }

    @Override
    public void hear() {
        System.out.print(getName() + " heard that ");
    }

    @Override
    public void watch() {
        System.out.print(getName() + " watched that ");
    }

    @Override
    public void shrug() {
        System.out.print(getName() + " shrugged ");
    }

    @Override
    public String toString(){
        return ("Class: Karlson; Name: " + name);
    }
}

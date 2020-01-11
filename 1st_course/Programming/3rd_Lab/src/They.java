class They extends Human implements Watch, Hear {
    They(String name) {
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
    public String toString(){
        return ("Class: They; Name: " + name);
    }
}

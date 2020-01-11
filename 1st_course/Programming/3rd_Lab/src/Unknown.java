class Unknown extends Human implements Watch, Hear {
    Unknown() {
        this.name = "Somebody";
    }

    @Override
    public String toString(){
        return ("Class: Unknown; Name: " + name);
    }

    @Override
    public void hear() {
        //System.out.print(getName() + " heard that ");
    }

    @Override
    public void watch() {
        //System.out.print(getName() + " watched that ");
    }
}

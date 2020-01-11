class Something extends Entity implements look_like {
    Something(String name) {
        this.name = name;
    }

    @Override
    public void not_look(Status status) {
        System.out.print(getName() + " didn't look " + status + " ");
    }
    @Override
    public String toString(){
        return ("Class: Something; Name: " + name);
    }
}
